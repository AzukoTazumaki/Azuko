from typing import Optional
from sqlmodel import SQLModel, Field, Relationship


class Featurings(SQLModel, table=True):
    __tablename__ = 'featurings'

    id: Optional[int] = Field(default=None, primary_key=True)
    track_id: Optional[int] = Field(default=None, foreign_key='tracks.id')
    track: Optional['Tracks'] = Relationship(back_populates='featuring')
