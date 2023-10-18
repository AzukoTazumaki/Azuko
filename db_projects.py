import datetime

from models.models import InitEngine
from sqlmodel import select, desc
from models.Artists import Artists
from models.Featurings import Featurings
from models.Albums import Albums
from models.Singles import Singles
from models.Tracks import Tracks
import locale

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
        stmt = select(Tracks).join(Tracks.single).order_by(desc(Tracks.date_release)).limit(3)
        db_last_releases = self.session.execute(stmt)
        db_last_releases_scalars = db_last_releases.scalars()
        for release in db_last_releases_scalars:
            print(release.title)


SelectProjects().select_last_releases()