from shared.models import User, Address
from shared.engine import session
from sqlalchemy import select

# Insert
u1 = User(name="pkrabs", fullname="Pearl Krabs")
a1 = Address(email_address="pearl.krabs@gmail.com")
u1.addresses.append(a1)

u1.name = "datikken"

session.add(u1)
# session.flush()
# session.commit()
