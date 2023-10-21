from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship


class Mastering(SQLModel, table=True):
    __tablename__ = 'mastering'

    id: Optional[int] = Field(default=None, primary_key=True)
    track_id: Optional[int] = Field(default=None, foreign_key='tracks.id')
    product_id: Optional[int] = Field(default=None, foreign_key='products.id')
    tracks: List['Tracks'] = Relationship(back_populates='mastering')
    product: Optional['Products'] = Relationship(back_populates='mastering')
