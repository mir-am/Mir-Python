# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 22:34:15 2018
@author: Mir, A.

This module is created to connect to Databases such as MySQL

"""

# In order to connect to MySQL, PyMySQL can be used.
# https://github.com/PyMySQL/PyMySQL
import pymysql


def connect_MySQL(host, user, passw, db_name):
    
    """
    Conntects to MySQL database and returns a DB instance for further opeartions
    like running SQL commands
    """
    
    return pymysql.connect(host, user, passw, db_name)
