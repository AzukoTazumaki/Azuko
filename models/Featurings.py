from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship
from .FeaturingsArtists import FeaturingsArtists


class Featurings(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    track_id: Optional[int] = Field(default=None, foreign_key='tracks.id')
    artists: List['Artists'] = Relationship(back_populates='featurings', link_model=FeaturingsArtists)
    track: Optional['Tracks'] = Relationship(back_populates='featuring')
