from sqlalchemy import Table, Column, ForeignKey
from .Base import Base

AlbumsArtists = Table(
    "AlbumsArtists",
    Base.metadata,
    Column("AlbumID", ForeignKey("Albums.id")),
    Column("ArtistID", ForeignKey("Artists.id"))
)
