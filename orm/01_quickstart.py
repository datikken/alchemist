from sqlalchemy import select
from definitions import engine
from definitions import User, Address
from sqlalchemy.orm import Session

session = Session(engine)


# Simple SELECT
stmt = select(User).where(User.name.in_(["spongebob", "sandy"]))
for user in session.scalars(stmt):
    print(user)


# SELECT with JOIN
stmt = (
    select(Address)
    .join(Address.user)
    .where(User.name == "sandy")
    .where(Address.email_address == "sandy_cheeks@sqlalchemy.org")
)
sandy_address = session.scalars(stmt).one()


# Make Changes
stmt = select(User).where(User.name == "patrick")
patrick = session.scalars(stmt).one()
patrick.addresses.append(Address(email_address="patrickstar@sqlalchemy.org"))
sandy_address.email_address = "sandy_cheeks@sqlalchemy.org"


# Some Deletes
sandy = session.get(User, 2)
sandy.addresses.remove(sandy_address)

session.commit()