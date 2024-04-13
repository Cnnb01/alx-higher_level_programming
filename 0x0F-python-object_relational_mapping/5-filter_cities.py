#!/usr/bin/python3
"""
a script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    
    #imports
    import MySQLdb
    from sys import argv

    #connecting mysql database(making a connection to the db)
    mydb = MySQLdb.connect(host='localhost', user=argv[1], password=argv[2], db=argv[3], port=3306)
    #creating  a cursor object
    mycurs = mydb.cursor()
    #executing queries using the cursor object
    mycurs.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN states WHERE states.name =%s AND states.id = cities.state_id  ORDER BY cities.id ASC;",(argv[4],))
    #collects all the results
    myrows = mycurs.fetchall()
    for i in myrows:
        print (i)
    #close cursor and db
    mycurs.close()
    mydb.close()
