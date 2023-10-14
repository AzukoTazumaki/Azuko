from typing import Set
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .Base import Base
from .FeaturingsArtists import FeaturingsArtists


class Featurings(Base):
    __tablename__ = 'Featurings'

    id: Mapped[int] = mapped_column(primary_key=True)
    TrackID: Mapped[int] = mapped_column(ForeignKey('Tracks.id'))
    artists: Mapped[Set['Artists']] = relationship(secondary=FeaturingsArtists, back_populates='featurings')
    tracks: Mapped['Tracks'] = relationship(back_populates='featurings')
