from models.Products import Products
from models.models import InitEngine
from sqlmodel import select, desc
from models.Albums import Albums
from models.Tracks import Tracks
from models.Genres import Genres
from models.Beats import Beats


class SelectProjects(InitEngine):
    def __init__(self):
        super().__init__()
        self.all_singles = self.session.execute(
            select(Tracks).join(Tracks.single).join(Tracks.artists).join(Tracks.text).group_by(Tracks)
        ).scalars()
        self.all_albums = self.session.execute(
            select(Albums).join(Albums.tracks).join(Albums.artists).group_by(Albums)
        ).scalars()
        self.all_featurings = self.session.execute(
            select(Tracks).join(Tracks.featuring).join(Tracks.artists).group_by(Tracks)
        ).scalars()
        self.all_products = self.session.execute(select(Products).order_by(Products.id)).scalars()
        self.all_genres = self.session.execute(select(Genres)).scalars()

    def select_albums(self, album_id: int | None):
        if album_id is None:
            result = [
                {
                    'id': album.id, 'title': album.title, 'description': album.description,
                    'date_release': album.date_release.strftime('%d %B %Y'),
                    'cover': album.cover, 'artists': album.artists, 'tracks': [
                    {
                        'position': track.track_position_in_album, 'title': track.title,
                        'duration': f'{str(track.duration).split(":")[0]}:{str(track.duration).split(":")[1]}',
                        'artists': track.artists
                    } for track in album.tracks
                ]
                } for album in self.all_albums
            ]
            return result
        else:
            db_albums_scalars = self.session.execute(
                select(Albums).join(Albums.tracks).join(Albums.artists).where(Albums.id == album_id)).scalars()
            result = None
            for album in db_albums_scalars:
                result = {
                    'id': album.id, 'title': album.title, 'date_release': album.date_release.strftime('%d %B %Y'),
                    'cover': album.cover, 'artists': album.artists, 'tracks': [
                        {
                            'position': track.track_position_in_album, 'title': track.title,
                            'duration': f'{str(track.duration).split(":")[0]}:{str(track.duration).split(":")[1]}',
                            'artists': track.artists, 'text': track.text
                        } for track in album.tracks
                    ]
                }
            return result

    def select_singles(self):
        result = [
            {
                'id': single.id,
                'title': single.title,
                'date_release': single.date_release.strftime('%d %B %Y'),
                'artists': single.artists,
                'duration': f'{str(single.duration).split(":")[0]}:{str(single.duration).split(":")[1]}',
                'text': single.text
            } for single in self.all_singles
        ]
        return result

    def select_featurings(self):
        result = [
            {
                'id': featuring.id,
                'title': featuring.title,
                'date_release': featuring.date_release.strftime('%d %B %Y'),
                'artists': featuring.artists,
                'duration': f'{str(featuring.duration).split(":")[0]}:{str(featuring.duration).split(":")[1]}',
                'text': featuring.text
            } for featuring in self.all_featurings
        ]
        return result

    def select_last_releases(self):
        last_releases = []
        db_last_albums_scalars = self.session\
            .execute(select(Albums).join(Albums.artists).order_by(desc(Albums.date_release)).limit(3)).scalars()
        db_last_singles_scalars = self.session\
            .execute(select(Tracks).join(Tracks.single).join(Tracks.artists).group_by(Tracks)
                     .order_by(desc(Tracks.date_release)).limit(3)).scalars()
        for release in db_last_singles_scalars:
            last_releases.append({
                'id': release.id, 'title': release.title,
                'artists': release.artists, 'date_release': release.date_release
            })
        for release in db_last_albums_scalars:
            last_releases.append({
                'id': release.id, 'title': release.title, 'artists': release.artists,
                'date_release': release.date_release, 'is_album': True
            })
        last_releases.sort(key=lambda item: item['date_release'], reverse=True)
        return last_releases[:3]

    @staticmethod
    def match_product_name(product_id: int):
        match product_id:
            case 1:
                return select(Products).join(Products.beats)
            case 2:
                return select(Products).join(Products.mixing)
            case 3:
                return select(Products).join(Products.mastering)
            case 4:
                return select(Products).join(Products.mixing_and_mastering)
            case 5:
                return select(Products).join(Products.ghostwriting)

    def select_products(self, product_id: int | None):
        if product_id is None:
            return self.all_products.all()
        else:
            db_product_all = self.session.execute(self.match_product_name(product_id)).scalars().all()
            if not db_product_all:
                return 'Coming soon'
            return db_product_all

    def select_genres(self):
        result = self.all_genres.all()
        return result
