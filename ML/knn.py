#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 14:50:22 2018
@author: Mir, A.

Using KD-tree in Sckit-learn

"""

from dataproc import read_data
from sklearn.neighbors import KDTree
import time

# Read dataset
train_data, train_targets, filename = read_data('/home/mir/mir-projects/Dataset/cod-rna.csv')

start_t = time.time()

# KD-Tree
k = 5
tree = KDTree(train_data)

dist, ind = tree.query(train_data, k)

print("Computing neighbors: %.2f ms" % ((time.time() - start_t) * 1000))