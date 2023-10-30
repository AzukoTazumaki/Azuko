from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship


class Products(SQLModel, table=True):
    __tablename__ = 'products'

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: int
    old_price: int | None = None
    beats: List['Beats'] = Relationship(back_populates='product')
    mixing: Optional['Mixing'] = Relationship(back_populates='product')
    mastering: Optional['Mastering'] = Relationship(back_populates='product')
    mixing_and_mastering: Optional['MixingAndMastering'] = Relationship(back_populates='product')
    ghostwriting: Optional['Ghostwriting'] = Relationship(back_populates='product')
