from sqlalchemy import select
from definitions import engine
from definitions import User, Address
from sqlalchemy.orm import Session

# Simple SELECT
session = Session(engine)

stmt = select(User).where(User.name.in_(["spongebob", "sandy"]))

for user in session.scalars(stmt):
    print(user)


# SELECT with JOIN
stmt = (
    select(Address)
    .join(Address.user)
    .where(User.name == "sandy")
    .where(Address.email_address == "sandy@sqlalchemy.org")
)
sandy_address = session.scalars(stmt).one()
sandy_address