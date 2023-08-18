#!/usr/bin/python3
"""script list all state with cities though relatioship"""
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def main():
    """function not run if module is imported"""
    engine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}\
                           @localhost:3306/{argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(State).order_by(State.id).all()
    for row in rows:
        print(f"{row.id}: {row.name}")
        for c in row.cities:
            print(f"    {c.id}: {c.name}")
    session.close()


if __name__ == "__main__":
    main()
