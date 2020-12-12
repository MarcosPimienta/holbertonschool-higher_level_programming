#!/usr/bin/python3
"""Lists all states"""

import MySQLdb
from sys import argv

db = MySQLdb.connect(host="localhost", user="{}".format(argv[1]),
                     passwd="{}".format(argv[2]),
                     db="{}".format(argv[3]), port=3306)
cur = db.cursor()

cur.execute("SELECT * FROM states ORDER BY id;")
selects = cur.fetchall()
for i in selects:
    print("{}".format(i))
cur.close()
db.close()
