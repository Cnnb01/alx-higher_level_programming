#!/usr/bin/python3

"""
a script that lists all State objects from the database hbtn_0e_6_usa
"""
if __name__ == "__main__":

    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True)
    my_sessionn = sessionmaker(bind=engine)
    my_session = my_sessionn()
    for state in my_session.query(State):
        if argv[4] == state.name:
            print("{}".format(state.id))
        else:
            print("Not found")

    my_session.close()
