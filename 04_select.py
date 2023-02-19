from sqlalchemy import select
from sqlalchemy.orm import Session
from shared.engine import engine
from shared.tables import user_table
from shared.tables import address_table
from shared.models import User
from shared.models import Address


stmt = select(user_table).where(user_table.c.name == "spongebob")

with engine.connect() as conn:
    for row in conn.execute(stmt):
        pass

stmt = select(User).where(User.name == "spongebob")
with Session(engine) as session:
    for row in session.execute(stmt):
        pass
        # print(row)

# Return sql expression
# print(select(User))


with Session(engine) as session:
    row = session.execute(select(User)).first()
    print(row)

users_with_adresses = session.execute(
    select(User.name, Address).where(User.id == Address.user_id).order_by(Address.id)
).all()

print(users_with_adresses, type(users_with_adresses)) # Returns list 

# The WHERE clause
# print(user_table.c.name == "squidward")
# print(address_table.c.user_id > 10)