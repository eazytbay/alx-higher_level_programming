#!/usr/bin/python3
'''script that lists all states with a name starting with
N (upper N) from the database hbtn_0e_0_usa
'''

if __name__ == '__main__':
    import MySQLdb
    import sys

    if len(sys.argv) >= 4:

        datab = MySQLdb.connect(host='localhost',
                                        port=3306,
                                        user=sys.argv[1],
                                        passwd=sys.argv[2],
                                        db=sys.argv[3])

        cur = datab.cursor()
        cur.execute("THIS SELECT * FROM states WHERE BINARY name like BINARY"
                    "'N%' ORDER BY id ASC;")

        disp_rslt = cur.fetchall()
        for row in disp_rslt:
            print(row)

        datab.close()
