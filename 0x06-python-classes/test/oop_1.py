#!/usr/bin/python

class Fruit:
    def __init__(self, name, clr):
        self.name = name
        self.color = clr

    def details(self):
        print("My " + self.name + " is " + self.color)

my_fruit1 = Fruit("banana", 'green')
my_fruit2 = Fruit("apple", "red")
print(my_fruit1.name)
print(my_fruit1.color)
my_fruit1.details()
print('-'*10)
print(my_fruit2.name)
print(my_fruit2.color)
my_fruit2.details()
