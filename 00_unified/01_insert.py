from shared.models import User
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

engine = create_engine("sqlite:///database.sqlite", echo=True)

session = Session(engine)

squidward = User(name="squidward", fullname="Squidward Tentacles")
krabs = User(name="ehkrabs", fullname="Eugene H. Krabs")

session.add(squidward)
session.add(krabs)

# print(session.new)

session.flush()
session.commit()