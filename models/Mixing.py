from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship


class Mixing(SQLModel, table=True):
    __tablename__ = 'mixing'

    id: Optional[int] = Field(default=None, primary_key=True)
    track_id: Optional[int] = Field(default=None, foreign_key='tracks.id')
    product_id: Optional[int] = Field(default=None, foreign_key='products.id')
    tracks: List['Tracks'] = Relationship(back_populates='mixing')
    product: Optional['Products'] = Relationship(back_populates='mixing')
