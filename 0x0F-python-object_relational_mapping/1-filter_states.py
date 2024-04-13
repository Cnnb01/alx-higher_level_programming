#!/usr/bin/python3
"""
a script that lists all states from the database hbtn_0e_0_usa
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
    mycurs.execute("SELECT * FROM states WHERE states.name LIKE 'N%' ORDER BY states.id ASC;")
    #collects all the results
    myrows = mycurs.fetchall()
    for i in myrows:
        print (i)
    #close cursor and db
    mycurs.close()
    mydb.close()