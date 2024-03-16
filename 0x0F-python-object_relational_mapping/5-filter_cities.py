

#!/usr/bin/python3
'''
A script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
'''

if __name__ == '__main__':
    import MySQLdb
    import sys

    if len(sys.argv) >= 5:

        datab = MySQLdb.connect(host='localhost',
                                        port=3306,
                                        user=sys.argv[1],
                                        passwd=sys.argv[2],
                                        db=sys.argv[3])

        input_state = sys.argv[4]
        cur = datab.cursor()

        cur.execute('SELECT cities.name FROM cities' +
                    ' INNER JOIN states ON cities.state_id = states.id' +
                    ' WHERE BINARY states.name = %s' +
                    ' ORDER BY cities.id ASC;',
                    [input_state]
                    )

        disp_result = cur.fetchall()
        print(", ".join([row[0] for row in disp_result]))

        db_connection.close()
