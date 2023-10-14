from sqlalchemy import Table, Column, ForeignKey
from .Base import Base

SinglesArtists = Table(
    "SinglesArtists",
    Base.metadata,
    Column("SingleID", ForeignKey("Singles.id")),
    Column("ArtistID", ForeignKey("Artists.id"))
)
