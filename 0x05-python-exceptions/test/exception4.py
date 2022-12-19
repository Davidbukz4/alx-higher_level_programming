#!/usr/bin/python3

try:
    f = open("test.txt")
except FileNotFoundError as e:
    print("That file was not found")
    print(e.args)
else:
    print("File: ", f.read())
    f.close()
finally:
    print("Finished working with file")
