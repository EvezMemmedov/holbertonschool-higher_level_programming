#!/usr/bin/python3
"""
 that prints the State object with the name passed as argument
"""


import sys
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@localhost:3306/{database}"
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()
    states = (
        session.query(State)
        .filter(func.binary(State.name) == state_name)
        .order_by(State.id).first()
    )
    if states:
        print(states.id)
    else:
        print("Not found")
