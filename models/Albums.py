from typing import List, Optional
from .AlbumsArtists import AlbumsArtists
from .AlbumsTracks import AlbumsTracks
from sqlmodel import SQLModel, Field, Relationship
from datetime import date


class Albums(SQLModel, table=True):
    __tablename__ = 'albums'

    id: Optional[int] = Field(primary_key=True)
    title: str = Field(unique=True)
    description: str
    date_release: date
    cover: str = Field(unique=True)
    artists: List['Artists'] = Relationship(back_populates='albums', link_model=AlbumsArtists)
    tracks: List['Tracks'] = Relationship(back_populates='albums', link_model=AlbumsTracks)
