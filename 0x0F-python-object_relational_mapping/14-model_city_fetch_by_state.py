#!/usr/bin/python3
""" lists all State objects from the database """
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sys import argv
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)

    session = Session()

    for city in session.query(City, State.name).join(State).filter(
            State.id == City.state_id).order_by(City.id).all():
        print("{}: ({}) {}".format(city[1], city[0].id, city[0].name))

    session.close()
