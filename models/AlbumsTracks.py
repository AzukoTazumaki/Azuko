from typing import Optional
from sqlmodel import SQLModel, Field


class AlbumsTracks(SQLModel, table=True):
    album_id: Optional[int] = Field(foreign_key='albums.id', primary_key=True)
    track_id: Optional[int] = Field(foreign_key='tracks.id', primary_key=True)

