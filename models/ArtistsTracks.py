from sqlalchemy import Table, Column, ForeignKey
from .Base import Base

ArtistsTracks = Table(
    "ArtistsTracks",
    Base.metadata,
    Column("TrackID", ForeignKey("Tracks.id")),
    Column("ArtistID", ForeignKey("Artists.id")),
)
