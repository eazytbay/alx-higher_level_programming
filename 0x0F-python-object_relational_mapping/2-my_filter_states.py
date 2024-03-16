#!/usr/bin/python3
"""
A script that takes in an argument and displays all value
in the states table where name matches the argument

"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE BINARY name='{}' ORDER
                   BY id""".format(argv[4]))

    for row in cur.fetchall():
        print(row)
    db.close()
