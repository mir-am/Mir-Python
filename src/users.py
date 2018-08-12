# Login and register process will be implemented here

from hashlib import md5
from person import Person


def user_register():

    print("Please enter carefully following required information")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    city = input("City: ")
    user_name = input("Username: ")
    # Hash the user's password with MD5! It's not safe but it's fine for
    # this educational project
    password = md5(input("Password: ").encode("utf-8")).hexdigest()
    email_address = input("Email address: ")

    return Person(first_name, last_name, city, email_address, user_name, password)

