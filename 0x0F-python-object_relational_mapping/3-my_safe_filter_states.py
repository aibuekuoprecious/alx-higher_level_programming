#!/usr/bin/python3
"""
python script that lists all states from the database hbtn_0e_0_usa with a
given name and is safe from MySQL injections
"""

import MySQLdb
import sys

mysql_user = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        charset="utf8",
        user=mysql_user,
        passwd=mysql_password,
        db=database_name)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
                   (sys.argv[4],))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
