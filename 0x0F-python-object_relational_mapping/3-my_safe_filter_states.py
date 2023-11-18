#!/usr/bin/python3

"""
    Takes in arguments and displays all values in the states table of
    hbtn_0e_0_usa where name matches the argument.
    But this time, write one that is safe from MySQL injections!.
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    qry = "SELECT * FROM states WHERE name LIKE BINARY %s\
    ORDER BY states.id ASC"
    match = (argv[4],)
    cursor.execute(qry, match)
    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()
