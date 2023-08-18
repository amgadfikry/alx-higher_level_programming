#!/usr/bin/python3
"""module update current record in database"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from model_state import Base, State
from sys import argv


def main():
    """function that not run if script import as module"""
    engine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}\
                           @localhost:3306/{argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()
    row = session.query(State).get(2)
    row.name = "New Mexico"
    session.add(row)
    session.commit()
    session.close()


if __name__ == "__main__":
    main()
