from typing import Optional
from sqlmodel import SQLModel, Field


class ArtistsTracks(SQLModel, table=True):
    track_id: Optional[int] = Field(foreign_key='tracks.id', primary_key=True)
    artist_id: Optional[int] = Field(foreign_key='artists.id', primary_key=True)
