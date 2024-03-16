#!/usr/bin/python3
"""
A script that lists all states with a name starting with N from the database
    user, password and database are passed on as command line arguments
    example: ./1-filter_states.py root root hbtn_0e_0_usa
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT id, name FROM states WHERE name LIKE
                BINARY 'N%' ORDER BY id""")

    for row in cur.fetchall():
        print(row)
    db.close()
