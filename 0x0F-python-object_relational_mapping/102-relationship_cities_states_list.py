#!/usr/bin/python3
"""module list all city objects from databases"""
from relationship_city import City
from relationship_state import State, Base
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """function prevent code from run if module imported"""
    engine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}\
                           @localhost:3306/{argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(City).order_by(City.id).all()
    for row in rows:
        print(f"{row.id}: {row.name} -> {row.state.name}")
    session.close()


if __name__ == "__main__":
    main()
