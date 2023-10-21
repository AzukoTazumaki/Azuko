from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship


class Beats(SQLModel, table=True):
    __tablename__ = 'beats'

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    bpm: int
    key_id: Optional[int] = Field(default=None, foreign_key='keys.id')
    genre_id: Optional[int] = Field(default=None, foreign_key='genres.id')
    product_id: Optional[int] = Field(default=None, foreign_key='products.id')
    key: Optional['Keys'] = Relationship(back_populates='beat')
    genre: Optional['Genres'] = Relationship(back_populates='beat')
    product: Optional['Products'] = Relationship(back_populates='beats')
