# A simple class to model a person as on object


class Person:

    def __init__(self, first_name, last_name, email, address, city, zipcode):

        self.first_name = first_name
        self.last_name = last_name
        self.email_addr = email
        self.address = address
        self.city = city
        self.zip_code = zipcode

    def get_person_tuple(self):

        return (self.first_name, self.last_name, self.email_addr, self.address,
                self.city, self.zip_code)
