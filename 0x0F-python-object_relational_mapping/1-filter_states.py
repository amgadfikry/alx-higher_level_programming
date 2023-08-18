#!/usr/bin/python3
""" module to get all state from dtatbases with filter """
import MySQLdb
import sys


def main():
    """mian function not excuted when import as module"""
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                         passwd=sys.argv[2], db=sys.argv[3])
    start = db.cursor()
    start.execute("""SELECT * FROM states WHERE states.name LIKE 'N%'
                        ORDER BY states.id""")
    rows = start.fetchall()
    for row in rows:
        print(row)
    start.close()
    db.close()


if __name__ == "__main__":
    main()
