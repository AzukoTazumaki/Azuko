from sqlalchemy import Table, Column, ForeignKey
from .Base import Base

AlbumsTracks = Table(
    "AlbumsTracks",
    Base.metadata,
    Column("AlbumID", ForeignKey("Albums.id")),
    Column("TrackID", ForeignKey("Tracks.id")),
)
