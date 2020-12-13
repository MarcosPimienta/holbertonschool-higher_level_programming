#!/usr/bin/python3
"""Lists all cities with states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user="{}".format(argv[1]),
                         passwd="{}".format(argv[2]),
                         db="{}".format(argv[3]), port=3306)
    cur = db.cursor()

    cur.execute("SELECT cities.name\
                 FROM cities INNER JOIN states ON cities.state_id = states.id\
                 WHERE states.name = %s", (argv[4], ))
    selects = cur.fetchall()
    stringpr = ""
    for i in selects:
        stringpr += str(*i) if stringpr == "" else ", " + str(*i)
    print("{}".format(stringpr))
    cur.close()
    db.close()
