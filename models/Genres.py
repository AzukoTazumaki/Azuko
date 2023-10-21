from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship


class Genres(SQLModel, table=True):
    __tablename__ = 'genres'

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    beat: Optional['Beats'] = Relationship(back_populates='genre')
