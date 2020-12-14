#!/usr/bin/python3
""" SQLALCHEMY Session query update by id"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(State).filter(State.id == 2).update({"name": "New Mexico"})
    session.commit()
    session.close()
