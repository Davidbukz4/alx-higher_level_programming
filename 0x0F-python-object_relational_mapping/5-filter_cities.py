#!/usr/bin/python3
"""
Accessing a database
using MySQLdb
"""


import sys
import MySQLdb

if __name__ == '__main__':
    uname = sys.argv[1]
    pwd = sys.argv[2]
    dbName = sys.argv[3]
    # connect to database
    db = MySQLdb.connect(host='localhost', user=uname, passwd=pwd,
                         db=dbName, port=3306)

    # get a cursor
    query = db.cursor()

    # execute MySQL queries
    query.execute("SELECT cities.id, cities.name, states.name FROM cities\
                  INNER JOIN states ON states.id=cities.state_id\
                  WHERE states.name=%s\
                  ORDER BY cities.id ASC", (sys.argv[4],))

    # obtain query
    data = query.fetchall()
    delim = ""
    for x in data:
        print(delim + x[1], end="")
        delim = ", "
    print()

    # close the cursor
    query.close()
    # close the database
    db.close()
