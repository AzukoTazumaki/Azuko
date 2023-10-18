from datetime import time

from sqlmodel import SQLModel, Session, create_engine, insert, text
from .ArtistsTracks import ArtistsTracks
from .AlbumsArtists import AlbumsArtists
from .Artists import Artists
from .Featurings import Featurings
from .FeaturingsArtists import FeaturingsArtists
from .Albums import Albums
from .Singles import Singles
from .Tracks import Tracks
from .AlbumsTracks import AlbumsTracks
from .Data import albums, artists, singles, tracks, albums_tracks, albums_artists, artists_tracks, \
    featurings, featurings_artists
from .settings import db_url, db_name


class InitEngine:
    def __init__(self):
        self.engine = create_engine(db_url, echo=True)
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
            track_iter = Tracks(
                    title=track['title'],
                    duration=time.fromisoformat(track['duration']),
                    date_release=track['date_release'],
                    track_position_in_album=track['track_position_in_album']
                )
            self.session.add(track_iter)
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
        self.session.execute(insert(FeaturingsArtists), featurings_artists)
        self.session.commit()

    def close_session(self):
        self.session.close()


if __name__ == '__main__':
    init_db = InitDatabase()
    init_db.create_db_and_tables()
    init_db.create_projects()
    init_db.close_session()
