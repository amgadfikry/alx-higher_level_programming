#!/usr/bin/python3
"""module to get all cities from databases"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from model_state import Base, State
from model_city import City
from sys import argv


def main():
    """function prevent from running if imported as module"""
    engine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}\
                           @localhost:3306/{argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(State.name, City.id, City.name)\
        .join(State, State.id == City.state_id).order_by(City.id)
    for row in rows:
        print(f"{row[0]}: ({row[1]}) {row[2]}")
    session.close()


if __name__ == "__main__":
    main()
