from sqlalchemy import create_engine, select, insert, text
from sqlalchemy.orm import Session

from .SinglesArtists import SinglesArtists
from .ArtistsTracks import ArtistsTracks
from .AlbumsArtists import AlbumsArtists
from .Artists import Artists
from .Featurings import Featurings
from .FeaturingsArtists import FeaturingsArtists
from .Albums import Albums
from .Base import Base
from .Singles import Singles
from .Tracks import Tracks
from .AlbumsTracks import AlbumsTracks
from .data import albums, artists, singles, tracks, albums_tracks, albums_artists, singles_artists, artists_tracks, \
    featurings, featurings_artists
from .settings import db_driver, db_user, db_password, db_host, db_port, db_name


class InitEngine:
    def __init__(self):
        self.engine = create_engine(f'{db_driver}://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
        self.session = Session(bind=self.engine)


class InitDatabase(InitEngine):
    def __init__(self):
        super().__init__()

    def create_db_and_tables(self):
        # drop_db_query = f'drop database if exists {db_name}'
        # create_db_query = f'create database {db_name}'
        # use_db_query = f'use {db_name}'
        with self.engine.begin() as connection:
            # connection.execute(text(drop_db_query))
            # connection.execute(text(create_db_query))
            # connection.execute(text(use_db_query))
            Base.metadata.create_all(connection)

    def create_projects(self):
        self.session.execute(insert(Albums), albums)
        self.session.execute(insert(Tracks), tracks)
        self.session.execute(insert(Singles), singles)
        self.session.execute(insert(Artists), artists)
        self.session.execute(insert(Featurings), featurings)
        self.session.execute(insert(AlbumsTracks), albums_tracks)
        self.session.execute(insert(AlbumsArtists), albums_artists)
        self.session.execute(insert(SinglesArtists), singles_artists)
        self.session.execute(insert(ArtistsTracks), artists_tracks)
        self.session.execute(insert(FeaturingsArtists), featurings_artists)
        self.session.commit()

    def close_session(self):
        self.session.close()
