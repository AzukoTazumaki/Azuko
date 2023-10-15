from typing import Set
from sqlalchemy import Date, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .AlbumsArtists import AlbumsArtists
from .AlbumsTracks import AlbumsTracks
from .Base import Base


class Albums(Base):
    __tablename__ = 'Albums'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(64), nullable=False, unique=True)
    date_release: Mapped[Date] = mapped_column(Date())
    cover: Mapped[str] = mapped_column(String(64), nullable=False, unique=True)
    artists: Mapped[Set['Artists']] = relationship(secondary=AlbumsArtists, back_populates='albums')
    tracks: Mapped[Set['Tracks']] = relationship(secondary=AlbumsTracks, back_populates='albums')
