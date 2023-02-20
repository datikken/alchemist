from sqlalchemy import create_engine
from sqlalchemy.orm import Session


engine = create_engine("sqlite:///unified/database.sqlite", echo=True)

session = Session(engine)
