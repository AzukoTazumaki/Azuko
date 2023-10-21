from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship
from .AlbumsArtists import AlbumsArtists
from .ArtistsTracks import ArtistsTracks


class Artists(SQLModel, table=True):
    __tablename__ = 'artists'

    id: Optional[int] = Field(primary_key=True)
    name: str = Field(unique=True)
    albums: List['Albums'] = Relationship(back_populates='artists', link_model=AlbumsArtists)
    tracks: List['Tracks'] = Relationship(back_populates='artists', link_model=ArtistsTracks)
