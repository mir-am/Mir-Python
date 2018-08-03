# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 22:40:16 2018

@author: Mir, A.
"""

from db import connect_MySQL
from ui import launch_ui
from process_input import process_user_choice


def main():
    
    # MySQL DB information
    hostname = 'localhost'
    username = 'MySQL_User'
    password = '123456789'
    database_name = 'acme'
    
    mysql_db = connect_MySQL(hostname, username, password, database_name)

    print("Successfully connected to database...")

    user_choice = launch_ui()

    process_user_choice(user_choice, mysql_db)

    mysql_db.close()


if __name__ == '__main__':
    
    main()
