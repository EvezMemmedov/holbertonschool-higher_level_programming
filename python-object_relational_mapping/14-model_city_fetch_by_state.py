#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@localhost:3306/{database}"
    )

    Session = sessionmaker(bind=engine)
    session = Session()
    results = (
        session.query(State, City)
        .join(City, City.state_id == State.id)
        .order_by(City.id)
        .all()
    )
    for state, city in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
