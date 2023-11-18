#!/usr/bin/python3

"""
    Takes in the name of a state as an argument and
    lists all cities of that state, using the database hbtn_0e_4_usa.
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    qry = "SELECT cities.name FROM cities\
    INNER JOIN states ON cities.state_id = states.id\
    WHERE states.name LIKE BINARY %s ORDER BY cities.id ASC"
    match = (argv[4],)
    cursor.execute(qry, match)
    cities = cursor.fetchall()
    cityList = ", ".join([city[0] for city in cities])
    print(cityList)

    cursor.close()
    db.close()
