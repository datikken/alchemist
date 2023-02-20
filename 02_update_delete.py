from shared.models import User
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import select

engine = create_engine("sqlite:///database.sqlite", echo=True)

session = Session(engine)

sandy = session.execute(select(User).filter_by(name="sandy")).scalar_one()

print(sandy)

# Delete
patrick = session.get(User, 3)

session.delete(patrick)
session.flush()
# session.commit() patrick will stay in db until commit