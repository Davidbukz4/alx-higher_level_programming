#!/usr/bin/python3

import csv

with open('names.csv', 'r') as f:
    content = csv.reader(f)

    with open('new_names.csv', 'w') as nf:
        data = csv.writer(nf, delimiter='-')
    
        for line in content:
            data.writerow(line)
        print(type(line))
