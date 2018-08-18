# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 10:24:20 2017

@author: Mir, A.
"""

# In this module, data processing functions are provided

from os import listdir, getcwd
from os.path import isfile, join, dirname, splitext, split
#from docx import Document
import numpy as np
import csv
#import time

# Convert a string list to float list
def conv_list_fl(data):
    
    temp_data = np.zeros(data.shape)
    
    # Read rows
    for i in range(data.shape[0]):
        
        # Read coloums
        for j in range(data.shape[1]):
            
            temp_data[i][j] = float(data[i][j])
            
    return temp_data

# Read data from CSV file
def read_data(filename, ignore_header=False):
    
    # Open file
    data = open(filename, 'r')
    
    # Open CSV file
    data_csv = csv.reader(data, delimiter=',')
    
    # Ignore hedaer files, because some files do not have headers.
    if ignore_header:
        
        # Store data in numpy array
        data_array = np.array(list(data_csv)) # [1:] for removing headers
        
    else:
        
        # Store data in numpy array
        data_array = np.array(list(data_csv)[1:]) # [1:] for removing headers
    
    #Close file
    data.close()
    
    # Shuffle data
    #np.random.shuffle(data_array)                        
    
    # Store tarning data
    data_train = conv_list_fl(data_array[:, 1:])                     
                         
    # Store data lables in numpy array
    data_labels = np.array([int(i) for i in data_array[:, 0]])
    
    # Get the filename
    file_name = splitext(split(filename)[-1])[0]
    
    # Training data, Class labels, Name of dataset
    return data_train, data_labels, file_name 

# Print list of aviable datasets with its number
def dataset_print(data_address, print_data=True):
    
    # Join address
    address = join(dirname(__file__), data_address)

    # Get only file names in the address
    data_files = [f for f in listdir(address) if isfile(join(address, f))]
    
    if print_data:
    
        # Print list of datasets with its numbers
        for index, file in enumerate(data_files):
            
            print("%d -> %s" % (index, file))
        
    return data_files

# Store dataset charactrestics: no. features & no. samples in dictionary
def dataset_char(data_address):
    
    # Get list of datasets in given address
    list_dataset = dataset_print(data_address, False)
    
    # Store dataset info in dict
    data_dict = {}
    
    # Read charactresitic of each dataset
    for data_set in list_dataset:
        
        # Read dataset file
        data = read_data(data_address + data_set)
        
        # Number of features and samples in dataset
        no_samp, no_feature = data[0].shape[0], data[0].shape[1]
        
        # Get number of positive and negative samples in dataset
        pos_samp, neg_samp = data[0][data[1] == 1].shape[0], data[0][data[1] == \
                                  -1].shape[0]
        
        data_dict[data[2].title()] = {'#Samples': no_samp, '#Positive': pos_samp, \
                  '#Negative': neg_samp, '#Features': no_feature}
        
                      
    return data_dict 

# Create a table in Word for dataset characteristics
#def word_table(data_dict, doc_name):
#    
#    # Get name of datasets
#    dataset_name = data_dict.keys()
#
#    # Create a Word Document
#    doc = Document(doc_name)   
#
#    # Create a table     
#    table = doc.add_table(rows=1, cols=5)
#    table.style = 'TableGrid'
#    
#    # Table headers
#    t_cells = table.rows[0].cells
#    t_cells[0].text = 'Datasets'
#    t_cells[1].text = '#Samples'
#    t_cells[2].text = '#Positive'
#    t_cells[3].text = '#Negative'
#    t_cells[4].text = '#Features'
#    
#    # Add dataset charac. to table
#    for dataset in dataset_name:
#        
#        # Store dataset charc.
#        data_char = data_dict[dataset]
#        
#        row_cells = table.add_row().cells
#        row_cells[0].text = dataset # name of dataset
#        row_cells[1].text = str(data_char['#Samples'])
#        row_cells[2].text = str(data_char['#Positive'])
#        row_cells[3].text = str(data_char['#Negative'])
#        row_cells[4].text = str(data_char['#Features'])
#    
#    
#    # Save document
#    doc.save(doc_name)

# Create a TeX table for datasets characteristics
def tex_table(data_dict, file_name):
    
    # Get name of datasets
    dataset_name = data_dict.keys()
    
    # Open a file for writing TeX code
    file_code = open(file_name, 'w')
    
    # Add dataset charac. to table
    for dataset in dataset_name:
        
        # Store dataset charc.
        data_char = data_dict[dataset]
        
        # Format: dataset name, #samples, #positive, #negative, #features
        file_code.write("{%s} & {%d} & {%d} & {%d} & {%d} \\\ \n" % (dataset, \
                        data_char['#Samples'], data_char['#Positive'], \
                                  data_char['#Negative'], data_char['#Features']))
                                            
    # Close file!
    file_code.close()                                


# Create an empty word file
def empty_word(doc_name):

    doc = Document()
    doc.save(doc_name)

    return doc_name    

# Write to a row of table in Word
def row_write(table, list_content):
    
    # Add a row for writing content
    row_cells = table.add_row().cells
    
    for i in range(len(table.columns)):
        
        row_cells[i].text = str(list_content[i])
    
    
#if __name__ == '__main__':
#    
#    # Test!
#    data_char = dataset_char(os.getcwd() + '\\Dataset\\UCI\\')
#    
#    # TeX table
#    tex_table(data_char, 'tex-table.txt')

