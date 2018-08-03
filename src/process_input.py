# In this module, user input will be processed.

from users import user_register
from db_quries import add_usr_db
import sys


def process_user_choice(menu_selection, db_cursor):

    # Register
    if menu_selection == '1':

        usr_info = user_register()
        add_usr_db(usr_info, db_cursor)


    # Login
    elif menu_selection == '2':

        pass

    # Exit
    elif menu_selection == '3':

        sys.exit(0)
