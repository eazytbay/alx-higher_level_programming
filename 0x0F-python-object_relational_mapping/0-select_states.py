#!/usr/bin/python3
'''
This is a script that lists all states from the database hbtn_0e_0_usa.
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
        cur.execute('SELECT * FROM states ORDER BY id ASC;')

        disp_rslt = cur.fetchall()
        for row in disp_rslt:
            print(row)

        datab.close()
