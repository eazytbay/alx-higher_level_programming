#!/usr/bin/python3
'''
a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
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

        cur = db_connection.cursor()
        input_state = sys.argv[4]
        cur.execute("SELECT * FROM states WHERE name=%s"
                    "ORDER BY states.id ASC;", [state_input])

        disp_rslt = cur.fetchall()
        for row in disp_result:
            print(row)

        datab.close()
