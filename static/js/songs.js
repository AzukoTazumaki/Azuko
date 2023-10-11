const audio_albums_path = 'static/audio/albums'
const albums = {
    fbn_songs: {
        track_name: ['HONESTLY.', 'MEROCK.', 'THEATER.', 'FADED.', 'ALL YEAR.', 'NO CHANGE.', 'WHERE DREAMS LEAD.', 
        'UP DOWN.', 'PILGRIM.', 'IN MY SOUL.', 'WE LOVE.', 'NEW SEASON.', 'COLD.', 'A LONG TIME AGO.', 'BOBBY FISCHER.', 
        'IDOL.', 'REAL.', 'STRANGERS.', 'WEEKEND.', 'BANKROLL.', 'SUPPOSED TO BE.', 'HARD FOR ME.', 'FORGIVENESS.'],
        track_number: 23,
        track_artist: 'Azuko',
        album_title: 'FUNNY but NOBODY',
        audio_dir: audio_albums_path + '/funny_but_nobody',
        cover: audio_albums_path + '/funny_but_nobody' + '/cover.jpg'
    },
    wlfa_songs : {
        track_name: ['Моя Вина', 'Ничего Лишнего', 'Занят', 'Время Летит', 'Babe <3', 'Маньяк', 'Время Покажет', 'Может Быть'],
        track_number: 8,
        track_artist: 'Azuko',
        album_title: 'with love from Azuko',
        audio_dir: audio_albums_path + '/with_love_from_azuko',
        cover: audio_albums_path + '/with_love_from_azuko' + '/cover.jpg'
    },  
}

const all_songs = []
const all_playlists = {
    'FUNNY but NOBODY': {
        songs: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22],
        title: 'FUNNY but NOBODY',
        author: 'Azuko'
    },
    'with love from Azuko': {
        songs: [23, 24, 25, 26, 27, 28, 29, 30],
        title: 'with love from Azuko',
        author: 'Azuko'
    }, 
}

/* function get_numbers_array(track_number) {
    let numbers_array = []
    for (let num = 0; num < track_number; num++) {
        numbers_array.push(num)
    }
    return numbers_array
} */


for (album in albums) {
    for (let i = 0; i < albums[album].track_number; i++) {
        all_songs.push({
            "name": albums[album].track_name[i],
            "artist": albums[album].track_artist,
            "album": albums[album].album_title,
            "url": albums[album].audio_dir + '/' + `${i}` + '.mp3',
            "cover_art_url": albums[album].cover
        })
    }
}

