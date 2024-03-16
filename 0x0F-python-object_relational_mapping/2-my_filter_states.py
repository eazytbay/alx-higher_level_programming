#!/usr/bin/python3
'''
a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
Safe from MySQL injection
'''

if __name__ == '__main__':
    import MySQLdb
    import sys

    if len(sys.argv) >= 4:

        datab = MySQLdb.connect(host='localhost',
                                        port=3306,
                                        user=sys.argv[1],
                                        passwd=sys.argv[2],
                                        datab=sys.argv[3])

        cur = datab.cursor()
        cur.execute("SELECT * FROM states WHERE name like BINARY '{}'"
                    "ORDER BY states.id ASC;".format(sys.argv[4]))

        disp_result = cur.fetchall()
        for row in disp_result:
            print(row)

        datab.close()
