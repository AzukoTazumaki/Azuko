from typing import Optional
from sqlmodel import SQLModel, Field, Relationship, text


class Lyrics(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    lyrics: str | None = None
    track_id: Optional[int] = Field(foreign_key='tracks.id')
    track: Optional['Tracks'] = Relationship(back_populates='text')
