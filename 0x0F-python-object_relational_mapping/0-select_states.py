#!/usr/bin/python3


import sys
import MySQLdb

if __name__ == '__main__':
    uname = sys.argv[1]
    pwd = sys.argv[2]
    dbName = sys.argv[3]
    # connect to database
    db = MySQLdb.connect(host='localhost', user=uname, passwd=pwd, db=dbName, port=3306)

    # get a cursor
    query = db.cursor()

    # execute MySQL queries
    query.execute("SELECT * FROM states ORDER BY states.id ASC")

    # obtain query
    data = query.fetchall()
    for x in data:
        print(x)

    # close the cursor
    query.close()
    # close the database
    db.close()
