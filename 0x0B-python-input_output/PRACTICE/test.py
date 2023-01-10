#!/usr/bin/python3

with open('file.txt', encoding="utf-8") as f:
    data = f.read(7)
    print(data)
    f.seek(31)
    print(f.tell())
    data = f.read()
    print(data)
