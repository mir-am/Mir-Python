#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date: Aug 10 17:15:44 2018
Developer: Mir, A.

Python's NumPy benchmark
ver: 0.1

This module is created for benchmarking the performance of NumPy package installed
on system.
"""

from datetime import datetime
import numpy as np
import platform
import psutil
import functools
import timeit


# Program constants
__version__ = '0.1'
DASHED_LINES = 35 * "-"
rep_bench = 3 # number of times that a test will be performed

program_header = """Python's NumPy benchmark v. %s
Developer: Mir, A.
%s
""" % (__version__, DASHED_LINES)


# Functions definition

def blas_info():
    
    """
    Returns BLAS library which is linked with NumPy package on user system
    """
    
    blas_libs_name = ('blas_mkl', 'blas', 'openblas', 'blas_opt', 'lapack_mkl',\
                      'openblas_lapack', 'lapack_opt')
    
    for lib in blas_libs_name:
        
        blas_lib_info = np.__config__.get_info(lib)
        
        if bool(blas_lib_info) == True:
            
            return blas_lib_info['libraries'][0]
            

def sys_info():
    
    """
    Prints user's system info such as CPU model, RAM, OS, Numpy Version and etc.
    """
    
    # Software info such OS name and Python version
    numpy_ver = "%s (Linked with %s)" % (np.__version__, blas_info())
    python_ver = platform.python_version()
    os_info = "%s %s" % (platform.system(), platform.release())
    
    # Hardware info
    cpu_info = "(%s Cores, %.2f GHz)" % (psutil.cpu_count(), psutil.cpu_freq().max / 1000)
    total_memory = "%d MB" % int(psutil.virtual_memory().total / 1024 / 1024)
    
    sys_info_msg = """
System Info:
Python Version: %s
NumPy Version: %s 
OS: %s
CPU: %s
RAM: %s
%s
"""
    
    return sys_info_msg % (python_ver, numpy_ver, os_info, cpu_info, total_memory, \
                           DASHED_LINES)
    
    
def start_bench():
    
    """
    NumPy's benchmark
    Tests with different matrix sizes (512, 1024, 2048, 4096, 8192)
    Performs matrix multiplication
    """
    
    mat_sizes = (512, 1024, 2048, 4096, 8192)
    
    # Appeding benchmark result to a string
    result_bench_str = 'Operation: Dense Matrix Multiplication\n'
    
    test_str = "Test %d: Matrix of size %d x %d - Time: %.3f Seconds\n"
    
    print(result_bench_str, end='')
    
    for t, size in enumerate(mat_sizes):
        
        # Create two random square matrix for multiplication
        mat_A = np.random.rand(size, size)
        mat_B = np.random.rand(size, size)
        
        bench_time = round(timeit.Timer(functools.partial(np.dot, mat_A, \
                           mat_B)).timeit(rep_bench) / rep_bench, 3)
        
        test_result = test_str % (t + 1, mat_A.shape[0], mat_B.shape[0], bench_time)
        
        print(test_result, end='')
        
        result_bench_str += test_result

    print(DASHED_LINES)
    
    result_bench_str += DASHED_LINES + '\n'
    
    return result_bench_str
    
    
def save_result_file(bench_result):
    
    """
    It saves benchmark result in a file
    """
    
    file_name = "NumPy benchmark result - %s " % datetime.now().strftime('%Y-%m-%d %H-%M')
 
    result_file = open(file_name, 'w')
    
    for section in bench_result:
        
        result_file.write(section)
    
    result_file.close()
    
########################


if __name__ == '__main__':
    
    print(program_header)
    
    system_spec = sys_info()
    
    print(system_spec)
    
    input("Press Enter to start the benchmark... \n")
    
    result = start_bench()
    
    finished_date = "Benchmark compeleted " + datetime.now().strftime("on %b %m, %Y at %H:%M %p")
    
    # Time and date of benchmark completion
    print(finished_date)
    
    save_result_file([program_header, system_spec, result, finished_date])
