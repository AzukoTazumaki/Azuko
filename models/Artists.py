from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship
from .AlbumsArtists import AlbumsArtists
from .ArtistsTracks import ArtistsTracks
from .FeaturingsArtists import FeaturingsArtists


class Artists(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    name: str = Field(unique=True)
    albums: List['Albums'] = Relationship(back_populates='artists', link_model=AlbumsArtists)
    featurings: List['Featurings'] = Relationship(back_populates='artists', link_model=FeaturingsArtists)
    tracks: List['Tracks'] = Relationship(back_populates='artists', link_model=ArtistsTracks)
