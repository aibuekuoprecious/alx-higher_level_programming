#!/usr/bin/python3
"""
Python script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

mysql_user = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                         user=mysql_user, passwd=mysql_password, db=database_name)

    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities \
                    INNER JOIN states ON cities.state_id = states.id \
                    ORDER BY cities.id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
