from typing import Optional
from sqlmodel import SQLModel, Field


class FeaturingsArtists(SQLModel, table=True):
    featuring_id: Optional[int] = Field(default=None, foreign_key='featurings.id', primary_key=True)
    artist_id: Optional[int] = Field(default=None, foreign_key='artists.id', primary_key=True)
