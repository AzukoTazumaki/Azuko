from typing import Set
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .AlbumsArtists import AlbumsArtists
from .ArtistsTracks import ArtistsTracks
from .Base import Base
from .FeaturingsArtists import FeaturingsArtists
from .SinglesArtists import SinglesArtists


class Artists(Base):
    __tablename__ = 'Artists'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64), unique=True)
    albums: Mapped[Set['Albums']] = relationship(secondary=AlbumsArtists, back_populates="artists")
    singles: Mapped[Set['Singles']] = relationship(secondary=SinglesArtists, back_populates='artists')
    featurings: Mapped[Set['Featurings']] = relationship(secondary=FeaturingsArtists, back_populates='artists')
    tracks: Mapped[Set['Tracks']] = relationship(secondary=ArtistsTracks, back_populates='artists')
