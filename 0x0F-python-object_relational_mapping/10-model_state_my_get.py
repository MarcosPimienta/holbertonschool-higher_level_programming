#!/usr/bin/python3
""" SQLALCHEMY Session query filter_by"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).filter_by(name=argv[4]):
        print("{}".format(state.id))
        exit()
    session.close()
