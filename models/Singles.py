from typing import Set
from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .Base import Base
from .SinglesArtists import SinglesArtists


class Singles(Base):
    __tablename__ = 'Singles'

    id: Mapped[int] = mapped_column(primary_key=True)
    TrackID = mapped_column(ForeignKey('Tracks.id'))
    artists: Mapped[Set['Artists']] = relationship(secondary=SinglesArtists, back_populates='singles')
    track: Mapped['Tracks'] = relationship(back_populates='single')
