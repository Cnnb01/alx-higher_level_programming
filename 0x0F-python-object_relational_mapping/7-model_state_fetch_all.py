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
    my_session = sessionmaker(bind=engine)
    for state in my_session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))

    my_session.close()
