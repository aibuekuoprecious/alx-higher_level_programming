#!/usr/bin/python3
"""
python script that lists all states from the database hbtn_0e_0_usa with a name
starting with N
"""

import MySQLdb
import sys

mysql_user = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, 
    user=mysql_user, passwd=mysql_password, db=database_name)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)
    cursor.close()
    db.close()
