import datetime

from models.models import InitEngine
from sqlalchemy import select
from models.SinglesArtists import SinglesArtists
from models.ArtistsTracks import ArtistsTracks
from models.AlbumsArtists import AlbumsArtists
from models.Artists import Artists
from models.Featurings import Featurings
from models.FeaturingsArtists import FeaturingsArtists
from models.Albums import Albums
from models.Base import Base
from models.Singles import Singles
from models.Tracks import Tracks
from models.AlbumsTracks import AlbumsTracks
import locale
from datetime import datetime

locale.setlocale(locale.LC_ALL)


class SelectProjects(InitEngine):
    def __init__(self):
        super().__init__()

    def select_albums(self):
        stmt = select(Albums).join(Albums.tracks).join(Albums.artists).group_by(Albums)
        db_albums = self.session.execute(stmt)
        db_albums_scalars = db_albums.scalars()
        result = []
        for album in db_albums_scalars:
            result.append({
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
        stmt = select(Singles).join(Singles.track).join(Singles.artists).group_by(Singles.id)
        db_singles = self.session.execute(stmt)
        db_singles_scalars = db_singles.scalars()
        result = []
        for single in db_singles_scalars:
            result.append(
                {
                    'id': single.track.id,
                    'date_release': single.track.date_release,
                    'title': single.track.title,
                    'artists': single.track.artists
                }
            )
        return result

    def select_featurings(self):
        pass
