# A simple class to model a person as on object


class Person:

    def __init__(self, first_name, last_name, city, user_name, password, email):

        self.first_name = first_name
        self.last_name = last_name
        self.city = city

        self.email_addr = email
        self.username = user_name
        self.password = password

    def get_person_tuple(self):

        return (self.first_name, self.last_name, self.city,  self.email_addr,
                self.username, self.password)
