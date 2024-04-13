#!/usr/bin/python3

"""
a script that lists all State objects from the database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    
    from model_state import Base, State
    from sqlalchemy import <>
    import MySQLdb
    from sys import argv

    #connecting mysql database(making a connection to the db)
    mydb = MySQLdb.connect(host='localhost', user=argv[1], password=argv[2], db=argv[3], port=3306)
    #creating  a cursor object
    mycurs = mydb.cursor()
    #executing queries using the cursor object
    mycurs.execute("SELECT * FROM states ORDER BY states.id ASC;")
    myrows = mycurs.fetchall()
    print (myrows)
    mycurs.close()
    mydb.close()
