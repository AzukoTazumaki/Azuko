from datetime import time
from sqlmodel import SQLModel, create_engine, insert, Session
from .ArtistsTracks import ArtistsTracks
from .AlbumsArtists import AlbumsArtists
from .Artists import Artists
from .Featurings import Featurings
from .Albums import Albums
from .Singles import Singles
from .Tracks import Tracks
from .AlbumsTracks import AlbumsTracks
from .Products import Products
from .Lyrics import Lyrics
from .Data import albums, artists, singles, tracks, albums_tracks, albums_artists, artists_tracks, featurings, products, \
    lyrics
from .settings import db_url


class InitEngine:
    def __init__(self):
        self.engine = create_engine(db_url)
        self.session = Session(bind=self.engine)


class InitDatabase(InitEngine):
    def __init__(self):
        super().__init__()

    def create_db_and_tables(self):
        with self.engine.connect() as connection:
            connection.execution_options(isolation_level='AUTOCOMMIT')
            SQLModel.metadata.create_all(connection)

    def create_projects(self):
        self.session.execute(insert(Albums), albums)
        self.session.commit()
        for track in tracks:
            self.session.add(Tracks(title=track['title'], duration=time.fromisoformat(track['duration']),
                                    date_release=track['date_release'],
                                    track_position_in_album=track['track_position_in_album']))
        self.session.commit()
        self.session.execute(insert(Lyrics), lyrics)
        self.session.commit()
        self.session.execute(insert(Artists), artists)
        self.session.commit()
        self.session.execute(insert(Singles), singles)
        self.session.commit()
        self.session.execute(insert(Featurings), featurings)
        self.session.commit()
        self.session.execute(insert(AlbumsTracks), albums_tracks)
        self.session.commit()
        self.session.execute(insert(AlbumsArtists), albums_artists)
        self.session.commit()
        self.session.execute(insert(ArtistsTracks), artists_tracks)
        self.session.commit()
        self.session.execute(insert(Products), products)
        self.session.commit()

    def close_session(self):
        self.session.close()
