from sqlalchemy import insert
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import MetaData
from shared.engine import engine


metadata_obj = MetaData()

user_table = Table(
    "user_account",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("fullname", String),
)

metadata_obj.create_all(engine)

stmt = insert(user_table).values(name="spongebob", fullname="Spongebob Squarepants")

# compiled = stmt.compile() // SQL expression

with engine.connect() as conn:
    result = conn.execute(stmt)
    conn.commit()