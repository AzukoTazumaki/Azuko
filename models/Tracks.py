from typing import Set
from sqlalchemy import Time, String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .AlbumsTracks import AlbumsTracks
from .ArtistsTracks import ArtistsTracks
from .Base import Base


class Tracks(Base):
    __tablename__ = 'Tracks'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(64), nullable=False)
    duration: Mapped[Time] = mapped_column(Time())
    date_release: Mapped[Date] = mapped_column(Date())
    artists: Mapped[Set['Artists']] = relationship(secondary=ArtistsTracks, back_populates='tracks')
    albums: Mapped[Set['Albums']] = relationship(secondary=AlbumsTracks, back_populates='tracks')
    single: Mapped['Singles'] = relationship(back_populates='track')
    featurings: Mapped['Featurings'] = relationship(back_populates='tracks')
