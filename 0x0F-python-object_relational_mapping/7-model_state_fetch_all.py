#!/usr/bin/python3
"""module that retrive states from database"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from model_state import State, Base
from sys import argv


def main():
    """function that not start if imported"""
    engine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}\
                           @localhost:3306/{argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(State).order_by(State.id).all()
    for row in rows:
        print(f"{row.id}: {row.name}")


if __name__ == "__main__":
    main()
