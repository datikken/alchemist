from database.config import Base
from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Parent(Base):
    __tablename__ = "parent_table"
    id: Mapped[int] = mapped_column(primary_key=True)
    # bidirectional - back_populates="parent"
    children: Mapped[List["Child"]] = relationship(back_populates="parent")
    # children: Mapped[Set["Child"]] = relationship(back_populates="parent")


class Child(Base):
    __tablename__ = "child_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    parent_id: Mapped[int] = mapped_column(ForeignKey("parent_table.id"))
    parent: Mapped["Parent"] = relationship(back_populates="children")
