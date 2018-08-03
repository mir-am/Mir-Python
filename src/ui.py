# A command line interface

welcome_msg = "Welcome! Please register or If you've signed up before, login."


def launch_ui():

    print(welcome_msg)

    print("1- Register\n"
          "2- Login\n"
          "3- Exit\n")

    user_choice = input("-> ")

    return user_choice

