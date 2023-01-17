#!/usr/bin/python3

import csv

with open('names.csv', 'r') as f:
    content = csv.DictReader(f)

    for line in content:
        print(line['email'])
