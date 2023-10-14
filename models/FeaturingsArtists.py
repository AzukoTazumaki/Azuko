from sqlalchemy import Table, Column, ForeignKey
from .Base import Base

FeaturingsArtists = Table(
    "FeaturingsArtists",
    Base.metadata,
    Column("FeaturingID", ForeignKey("Featurings.id")),
    Column("ArtistID", ForeignKey("Artists.id"))
)
