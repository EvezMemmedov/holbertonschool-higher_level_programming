#!/usr/bin/python3
"""
that deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa
"""


import sys
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@localhost:3306/{database}"
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()
    states = (
    session.query(State)
    .filter(func.binary(State.name).like("%a%"))
    .order_by(State.id).all()
    )
    for state in states:
        session.delete(state)
    session.commit()
