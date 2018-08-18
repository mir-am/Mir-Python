#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 15:40:10 2018

@author: Mir, A.

Using K-means in Scikit-learn

"""

from dataproc import read_data
from sklearn.cluster import KMeans
import time

# Read dataset
train_data, train_targets, filename = read_data('/home/mir/mir-projects/Dataset/cod-rna.csv')

start_t = time.time()

# KD-Tree
clusters = 5
tree = KMeans(clusters, algorithm='full')
tree.fit(train_data)

ind_clusters = tree.labels_

print("Computing clusters: %.2f ms" % ((time.time() - start_t) * 1000))

