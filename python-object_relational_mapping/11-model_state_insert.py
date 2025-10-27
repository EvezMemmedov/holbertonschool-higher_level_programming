#!/usr/bin/python3
"""
that adds the State object “Louisiana” to the database hbtn_0e_6_usa
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
    states = State(name="Louisiana")
    session.add(states)
    session.commit()
    print(states.id)
