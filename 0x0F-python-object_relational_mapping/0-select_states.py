#!/usr/bin/python3
""" module to select from all list of states in mysql databases """
import MySQLdb
import sys


def main():
    """ function now start when imported """
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                         passwd=sys.argv[2], db=sys.argv[3])
    start = db.cursor()
    start.execute("""SELECT * FROM states ORDER BY states.id""")
    rows = start.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
