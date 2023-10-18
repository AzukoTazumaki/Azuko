import datetime

from models.models import InitEngine
from sqlalchemy import select
from models.ArtistsTracks import ArtistsTracks
from models.AlbumsArtists import AlbumsArtists
from models.Artists import Artists
from models.Featurings import Featurings
from models.FeaturingsArtists import FeaturingsArtists
from models.Albums import Albums
from models.Singles import Singles
from models.Tracks import Tracks
from models.AlbumsTracks import AlbumsTracks
import locale
from datetime import datetime

locale.setlocale(locale.LC_ALL)


class SelectProjects(InitEngine):
    def __init__(self):
        super().__init__()

    def select_one_album(self, album_id: int):
        stmt = select(Albums).join(Albums.tracks).join(Albums.artists).where(Albums.id == album_id)
        db_albums = self.session.execute(stmt)
        db_albums_scalars = db_albums.scalars()
        result = None
        for album in db_albums_scalars:
            result = {
                'id': album.id,
                'title': album.title,
                'date_release': album.date_release.strftime('%d %B %Y'),
                'cover': album.cover,
                'artists': album.artists,
                'tracks': [
                    {
                        'position': track.track_position_in_album,
                        'title': track.title,
                        'duration': f'{str(track.duration).split(":")[0]}:{str(track.duration).split(":")[1]}',
                        'artists': track.artists
                    }
                    for track in album.tracks
                ]
            }
        return result

    def select_all_albums(self):
        stmt = select(Albums).join(Albums.tracks).join(Albums.artists).group_by(Albums)
        db_albums = self.session.execute(stmt)
        db_albums_scalars = db_albums.scalars()
        result = []
        for album in db_albums_scalars:
            result.append({
                'id': album.id,
                'title': album.title,
                'date_release': album.date_release.strftime('%d %B %Y'),
                'cover': album.cover,
                'artists': album.artists,
                'tracks': [
                    {
                        'position': track.track_position_in_album,
                        'title': track.title,
                        'duration': f'{str(track.duration).split(":")[0]}:{str(track.duration).split(":")[1]}',
                        'artists': track.artists
                    }
                    for track in album.tracks
                ]
            })
        return result

    def select_singles(self):
        stmt = select(Tracks).join(Tracks.single).join(Tracks.artists).group_by(Tracks)
        db_singles = self.session.execute(stmt)
        db_singles_scalars = db_singles.scalars()
        result = []
        for single in db_singles_scalars:
            result.append(
                {
                    'id': single.id,
                    'date_release': single.date_release,
                    'title': single.title,
                    'artists': single.artists
                }
            )
        return result

    def select_featurings(self):
        pass

    def select_last_releases(self):
        pass

    def select_one_single(self):
        stmt = select(Tracks).join(Tracks.artists).where(Tracks.id == 101)
        db_single = self.session.execute(stmt)
        db_singles_scalars = db_single.scalars()
        for a in db_singles_scalars:
            print(a.artists)


# SelectProjects().select_one_single()
