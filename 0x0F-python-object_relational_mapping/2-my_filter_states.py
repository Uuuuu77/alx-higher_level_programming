#!/usr/bin/python3

"""
    Module for listing states from database.
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    qry = "SELECT * FROM states WHERE name LIKE BINARY '{}'\
    ORDER BY states.id ASC".format(argv[4])
    cursor.execute(qry)
    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()
