#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 15:21:39 2018
@author: Mir, A.

In this module, a set of functions for linear algebra operations is defined
in Python. IT IS ONLY FOR EDUCATIONAL PURPOSE. Do not use this code for real
applications.

Use NumPy package which is implemented in C. It's blazing fast!

"""

import numpy as np
import time


def timeit(method):
    
    """
    A function decorator to measure the execution time of arbitraray functions
    """
    
    def timed(*args, **kw):
        
        start_t = time.time()
        result = method(*args, **kw)
        elapsed_t = time.time()
        
        print("%r %2.2f ms" % (method.__name__, (elapsed_t -start_t) * 1000))
        
        return result
    
    return timed
        

@timeit
def add_matrix(A, B):
    
    """
    Adding elements of two matrix - Element wise
    """
    
    # Make sure that the input is a 2D array
    assert len(A.shape) == 2
    # Two matrices must have same shape
    assert A.shape == B.shape
    
    # copy matrix A
    C = A.copy()
    
    for i in range(A.shape[0]):
        for j in range(B.shape[0]):
            
            C[i, j] = A[i, j] + B[i, j]
            
    return C
    
    # NumPy equivalent
    #return A + B


@timeit
def add_matrix_vector(mat_X, vec_Y):
    
    """
    Addes a matrix of size M x N with a vector of size N
    """
    
    # Some checks before add operation
    assert len(mat_X.shape) == 2
    assert len(vec_Y.shape) == 1
    assert mat_X.shape[1] == vec_Y.shape[0]

    mat_result = mat_X.copy()
    
    for i in range(mat_X.shape[0]):
        for j in range(mat_X.shape[1]):
            
            mat_result[i, j] = mat_X[i, j] + vec_Y[j]
            
    return mat_result


#@timeit
def vector_dot(vec_A, vec_B):
    
    """
    Adds two vector - Element wise
    """
    
    # Dimension of two vector must be same
    assert len(vec_A.shape) == 1
    assert len(vec_B.shape) == 1
    assert vec_A.shape[0] == vec_B.shape[0]
    
    z = 0
    for i in range(vec_A.shape[0]):
        
        z += vec_A[i] * vec_B[i]
        
    return z


@timeit
def matrix_vector_dot(mat_X, vec_Y):
    
    """
    Dot product of matrix x and Vector y
    """
    
    assert len(mat_X.shape) == 2
    assert len(vec_Y.shape) == 1
    assert mat_X.shape[1] == vec_Y.shape[0]
    
    z = np.zeros(mat_X.shape[0])
    
    for i in range(mat_X.shape[0]):
        
        z[i] = vector_dot(mat_X[i, :], vec_Y)
        
    return z
    

@timeit
def matrix_dot(mat_A, mat_B):
    
    """
    Dot product of two matrix.
    size of mat_A: M x K
    size of mat_B: K x N
    """
    
    # For matrix multiplication, number of colums of mat_A should be same as
    # number of rows of mat_B
    assert len(mat_A.shape) == 2
    assert len(mat_B.shape) == 2
    assert mat_A.shape[1] == mat_B.shape[0]
    
    z = np.zeros((mat_A.shape[0], mat_B.shape[1]))
    
    for i in range(mat_A.shape[0]):
        for j in range(mat_B.shape[1]):
            
            ith_row = mat_A[i, :]
            jth_col = mat_B[j, :]
            
            z[i, j] = vector_dot(ith_row, jth_col)
            
    return z


if __name__ == '__main__':
    
    DIM = 512
    
    mat_A = np.random.rand(DIM, DIM)
    mat_B = np.random.rand(DIM, DIM)
    vec_A = np.random.rand(DIM)
    vec_B = np.random.rand(DIM)
    
    mat_C = add_matrix(mat_A, mat_B)
    
    add_mat_vec = add_matrix_vector(mat_A, vec_A)
    
    vector_dot(vec_A, vec_B)
    
    matrix_vector_dot(mat_A, vec_A)
    
    matrix_dot(mat_A, mat_B)
    