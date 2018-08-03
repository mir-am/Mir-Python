# Login and register process will be implemented here

from person import Person


def user_register():

    print("Please enter carefully following required information")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    email_address = input("Email address: ")
    address = input("Address: ")
    city = input("City: ")
    zip_code = input("Zip code: ")

    return Person(first_name, last_name, email_address, address, city, zip_code)

