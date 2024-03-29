#!/usr/bin/python3
""" module that delete all record name contain 'a' in database"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sys import argv
from model_state import Base, State


def main():
    """function not run if script imported as module"""
    engine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}\
                           @localhost:3306/{argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(State).filter(State.name.like("%a%"))\
        .delete(synchronize_session='fetch')
    session.commit()
    session.close()


if __name__ == "__main__":
    main()
