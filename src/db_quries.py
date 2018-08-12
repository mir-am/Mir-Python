# Queries for login and register


# Add registered user to Database
def add_usr_db(user_info, db_connection):

    """

    :param user_info: An instance of Person class
    :param db_connection: An instance of database connection
    :return:
    """

    # SQL query for adding a new user to database
    sql_add_usr = "INSERT INTO user_info(firstName, lastName, city, username, " \
                  "password, email) VALUES(%s, %s, %s, %s, %s, %s);"

    db_cursor = db_connection.cursor()
    db_cursor.execute(sql_add_usr, user_info.get_person_tuple())
    db_connection.commit()
