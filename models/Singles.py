from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship


class Singles(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    track_id: Optional[int] = Field(default=None, foreign_key='tracks.id')
    track: Optional['Tracks'] = Relationship(back_populates='single')
