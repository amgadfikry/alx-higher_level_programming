#!/usr/bin/python3
""" module that get all cities of given state"""
import MySQLdb
from sys import argv


def main():
    """function that not run if import as module"""
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])
    start = db.cursor()
    query = """SELECT cities.name FROM cities
            WHERE cities.state_id = (SELECT states.id
            FROM states WHERE states.name LIKE BINARY %s)
            ORDER BY cities.id"""
    start.execute(query, (argv[4],))
    rows = start.fetchall()
    for i in range(len(rows)):
        if i == len(rows) - 1:
            print(rows[i][0])
        print(rows[i][0], end=", ")
    start.close()
    db.close()


if __name__ == "__main__":
    main()
