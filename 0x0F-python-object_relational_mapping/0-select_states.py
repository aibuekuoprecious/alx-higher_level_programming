#!/usr/bin/python3
"""
python script that lists all states from the database hbtn_0e_0_usa
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
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    
    cursor.close()
    db.close()
