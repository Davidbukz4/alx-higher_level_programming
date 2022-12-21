#!/usr/bin/python3
import datetime


class User:
    """ This is a docstring test """
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday #yyyymmdd
        # extract first and last names
        name_pieces = full_name.split(' ')
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    def age(self):
        """ Returns the age of the user in years. """
        today = datetime.date(2022, 12, 20)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd) #date of birth
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)

user1 = User("David Egwuatu", "19990927")
print(user1.name)
print(user1.first_name)
print(user1.last_name)
print(user1.birthday)
print("Age: ", user1.age())
