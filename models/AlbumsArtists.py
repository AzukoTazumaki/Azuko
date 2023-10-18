from typing import Optional
from sqlmodel import SQLModel, Field


class AlbumsArtists(SQLModel, table=True):
    album_id: Optional[int] = Field(foreign_key='albums.id', primary_key=True)
    artist_id: Optional[int] = Field(foreign_key='artists.id', primary_key=True)
