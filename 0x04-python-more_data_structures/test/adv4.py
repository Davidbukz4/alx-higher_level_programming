#!/usr/bin/python3

def random_func(name: str, age: int, weight: float) -> str:
    print("Name: ", name)
    print("Age: ", age)
    print("Weight: ", weight)

    return "{} is {} years old and weighs {}".format(name, age, weight)

print(random_func("Derek", 23, 65.5))
print(random_func(44, "Derek", 'Turtle'))
print(random_func.__annotations__)
