const audio_albums_path = '/static/audio/albums'
const audio_singles_path = '/static/audio/singles'
const audio_featurings_path = '/static/audio/featurings'
const singles_covers_path = '/static/images/projects/singles'
const featurings_covers_path = '/static/images/projects/featurings'

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
    tc_songs : {
        track_name: ['Время Перемен', 'Не Отпускай Меня', 'Молчание', 'Ночь', 'Одинокий', 'Нужна Она', 'Ранен', 'Опоздал', 
        'Между Нами', 'Мгновенье', 'Внимание', 'Не Могу'],
        track_number: 12,
        track_artist: ['Azuko, Kaneki', 'Azuko, Kaneki', 'Azuko, Kaneki', 'Azuko, Kaneki feat. Flipboy', 'Azuko, Kaneki', 
        'Azuko, Kaneki feat. YslBby, CHATTY', 'Azuko, Kaneki', 'Azuko, Kaneki', 'Azuko, Kaneki', 'Azuko, Kaneki', 
        'Azuko, Kaneki', 'Azuko, Kaneki feat. Foreign Beep'],
        album_title: 'ВРЕМЯ ПЕРЕМЕН',
        audio_dir: audio_albums_path + '/time_for_change',
        cover: audio_albums_path + '/time_for_change' + '/cover.jpg'
    }, 
    hofd_songs : {
        track_name: ['Who Needs Love?', 'Tell Me Bout That Night', 'Highway Of Love', 'Love Games', 'Scars', "I'm In love", 
        'Baby Wants', 'Лишь Ложь', 'Настоящий Ты', 'Свет Небес', 'Разбуди Меня', 'Остался Прежним', 'Мир Грёз', 'За Мечтами'],
        track_number: 14,
        track_artist: 'Azuko',
        album_title: 'Highway Of Love (Deluxe)',
        audio_dir: audio_albums_path + '/highway_of_love_deluxe',
        cover: audio_albums_path + '/highway_of_love_deluxe' + '/cover.jpg'
    }, 
    hof_songs : {
        track_name: ['Intro', 'Long Way', 'Live In Dreams', 'Breakdown', 'Playin In Love', 'Can We Be Together?', 'Bad Memories', 
        'Workin Hard', 'What You Want From Love?', 'I Was Need A Break', 'Wassup From The Gap', 'Tryin Be The Best', 'Early Bird 3', 
        'How Am I Lost?', "Don't Leave Me Alone", 'Far From Home', 'Why Not?', 'Chasing The Money', 'I Will No Hate You', 'Tonight', 
        'Under Purple Rain', 'Deadmans', 'Visions', 'Bad Bad Bad', 'Outro'],
        track_number: 25,
        track_artist: ['Azuko', 'Azuko', 'Azuko, ICYWAVE', 'Azuko', 'Azuko', 'Azuko', 'Azuko', 'Azuko', 'Azuko, Bobby D', 'Azuko', 
        'Azuko', 'Azuko', 'Azuko, Bobby D', 'Azuko', 'Azuko', 'Azuko', 'Azuko', 'Azuko', 'Azuko', 'Azuko', 'Azuko', 'Azuko', 
        'Azuko, YUNG ROUZY', 'Azuko', 'Azuko', ],
        album_title: 'Highway Of Love',
        audio_dir: audio_albums_path + '/highway_of_love',
        cover: audio_albums_path + '/highway_of_love' + '/cover.jpg'
    }, 
    mv_songs : {
        track_name: ['Mileran Vibes', 'Money Kill', 'Pray For My Family', 'Early Bird 2', 'No Lonely', "Fake Talkin'", 'Stop Love', 'No Time'],        
        track_number: 8,
        track_artist: 'Azuko',
        album_title: 'Mileran Vibes',
        audio_dir: audio_albums_path + '/mileran_vibes',
        cover: audio_albums_path + '/mileran_vibes' + '/cover.jpg'
    }, 
    lfl2_songs : {
        track_name: ['Intro', 'Stop Love', 'Spend All Night', 'Through The Sky', 'We Are Put Our Heart In The Phone', 'Go In The Gap', 
        'Heart Is a Full Of Lies', 'You Just A Hoe', 'Closed Door', 'Bang 2', 'My Feelings', 'Pray For My Family', 'Hate That World', 
        'Swag!', 'Time Is Sad With Every Day', "You're So Fuckin' Bad, Bae", 'Outro'],        
        track_number: 17,
        track_artist: 'Azuko',
        album_title: 'Life Is Full Of Lies 2 (Before Love Story)',
        audio_dir: audio_albums_path + '/life_is_full_of_lies_2',
        cover: audio_albums_path + '/life_is_full_of_lies_2' + '/cover.jpg'
    }
}

const singles = {
    track_name: [
        'FADED.', 'Supposed To Be', 'For Another', 'Dead For You', 'Лавина', 'Эйфория', 'Секси!', 'Киборг', 'Highway Of Love',
        'Время', 'Тени', 'Я Скучаю', 'Первый Снег', 'Make Choice', 'Believe', 'Stars', 'Out The Way', 'Kill Me Now', 'Reason',
        'Quarantine', 'Long Way', 'Breakdown', 'Can We Be Together?', 'What You Want From Love?', 'I Was Need A Break', 'How Am I Lost?', 
        'Far From Home', 'Tonight', 'Deadmans', 'Bad Bad Bad', 'Starry Sky', 'Do You Love Me?', 'Slatt Talk', 'Happy New Year', 
        'I Got Some Move', 'Что ты сделал?', 'wassup, girl', 'Не Сдавайся', 'momma tell me', 'Heart Is a Full Of Lies', 'Time Is Sad With Every Day', 
        '730, oh yeah', 'dr. stone', 'never want dat kind of love', 'diamonds dance', 'in the space', '448!', 'Before', 'where we go?', 'smith & wesson', 
        "takin 'n' takin", 'look like pearl', "that's for love", 'meet the girl', 'You No Lit'
    ],        
    track_number: 55,
    track_artist: [
        'Azuko', 'Azuko', 'Azuko', 'Azuko', 'Azuko, 88Ringo', 'Azuko', 'Azuko, 88Ringo', 'Azuko, 88Ringo', 'Azuko, 88Ringo', 'Azuko, 88Ringo', 
        'Azuko, СЭТ ГРАНЖ', 'Azuko, 88Ringo', 'Azuko', 'Azuko, 88Ringo, Noicat', 'Azuko', 'Azuko, 88Ringo', 'Azuko', 'Azuko, 88Ringo', 'Azuko, 88Ringo', 
        'Azuko, 88Ringo', 'Azuko, 88Ringo', 'Azuko, 88Ringo', 'Azuko', 'Azuko', 'Azuko', 'Azuko, Bobby D', 'Azuko', 'Azuko', 'Azuko', 'Azuko', 'Azuko', 'Azuko', 
        'Azuko', 'Azuko', 'Azuko', 'Azuko, FARO', 'Azuko', 'Azuko', 'Azuko', 'Azuko', 'Azuko', 'Azuko', 'Azuko', 'Azuko', 'Azuko', 'Azuko', 'Azuko', 'Azuko, Brayke', 
        'Azuko', 'Azuko', 'Azuko', 'Azuko', 'Azuko', 'Azuko', 'Azuko', 
    ],
    album_title: 'Singles',
    audio_dir: audio_singles_path,
    cover: [
        singles_covers_path + '/1.jpg', singles_covers_path + '/4.jpg', singles_covers_path + '/13.jpg', singles_covers_path + '/15.jpg', singles_covers_path + '/16.jpg', 
        singles_covers_path + '/29.jpg', singles_covers_path + '/31.jpg', singles_covers_path + '/34.jpg', singles_covers_path + '/35.jpg', singles_covers_path + '/36.jpg', 
        singles_covers_path + '/37.jpg', singles_covers_path + '/38.jpg', singles_covers_path + '/39.jpg', singles_covers_path + '/42.jpg', singles_covers_path + '/43.jpg', 
        singles_covers_path + '/44.jpg', singles_covers_path + '/45.jpg', singles_covers_path + '/46.jpg', singles_covers_path + '/47.jpg', singles_covers_path + '/48.jpg', 
        singles_covers_path + '/65.jpg', singles_covers_path + '/67.jpg', singles_covers_path + '/69.jpg', singles_covers_path + '/72.jpg', singles_covers_path + '/73.jpg', 
        singles_covers_path + '/77.jpg', singles_covers_path + '/79.jpg', singles_covers_path + '/83.jpg', singles_covers_path + '/85.jpg', singles_covers_path + '/87.jpg',
        singles_covers_path + '/89.jpg', singles_covers_path + '/90.jpg', singles_covers_path + '/91.jpg', singles_covers_path + '/92.jpg', singles_covers_path + '/99.jpg', 
        singles_covers_path + '/100.jpg', singles_covers_path + '/101.jpg', singles_covers_path + '/102.jpg', singles_covers_path + '/104.jpg', singles_covers_path + '/111.jpg',
        singles_covers_path + '/119.jpg', singles_covers_path + '/122.jpg', singles_covers_path + '/123.jpg', singles_covers_path + '/124.jpg', singles_covers_path + '/125.jpg',
        singles_covers_path + '/126.jpg', singles_covers_path + '/127.jpg', singles_covers_path + '/128.jpg', singles_covers_path + '/129.jpg', singles_covers_path + '/130.jpg', 
        singles_covers_path + '/131.jpg', singles_covers_path + '/132.jpg', singles_covers_path + '/133.jpg', singles_covers_path + '/134.jpg', singles_covers_path + '/135.jpg',
    ]
}

const featurings = {
    track_name: [
        'Супермен', 'Мы не играем в любовь (Remix)', 'Bitch Live In Texas', 'Половина обезбола', 'МЫ НЕ ИГРАЕМ В ЛЮБОВЬ', 
        'Тсукуёми', 'Bad Bitch', 'Марихуана', 'Космос 2', 'Tanjiro Kamado (Remix)'
    ],        
    track_number: 10,
    track_artist: [
        'ICYWAVE, Azuko', 'ICYWAVE, Azuko', 'Flipboy, Azuko', 'Flipboy, Azuko', 'ICYWAVE, Azuko', 'Blant, Azuko', 
        'YUNG ROUZY, Azuko', 'YUNG ROUZY, Azuko', 'Свиридов, ICYWAVE, Azuko', 'YUNG ROUZY, Azuko'
    ],
    album_title: 'Featurings',
    audio_dir: audio_featurings_path,
    cover: [
        featurings_covers_path + '/2.jpg', featurings_covers_path + '/3.jpg', featurings_covers_path + '/14.jpg',
        featurings_covers_path + '/30.jpg', featurings_covers_path + '/32.jpg', featurings_covers_path + '/33.jpg',
        featurings_covers_path + '/40.jpg', featurings_covers_path + '/41.jpg', featurings_covers_path + '/49.jpg',
        featurings_covers_path + '/103.jpg',
    ]
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
    'ВРЕМЯ ПЕРЕМЕН': {
        songs: [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
        title: 'ВРЕМЯ ПЕРЕМЕН',
        author: 'Azuko, Kaneki'
    }, 
    'Highway Of Love (Deluxe)': {
        songs: [43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56],
        title: 'Highway Of Love (Deluxe)',
        author: 'Azuko'
    }, 
    'Highway Of Love': {
        songs: [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81],
        title: 'Highway Of Love',
        author: 'Azuko'
    }, 
    'Mileran Vibes': {
        songs: [82, 83, 84, 85, 86, 87, 88, 89],
        title: 'Mileran Vibes',
        author: 'Azuko'
    },
    'Life Is Full Of Lies 2 (Before Love Story)': {
        songs: [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106],
        title: 'Life Is Full Of Lies 2 (Before Love Story)',
        author: 'Azuko'
    },
    'Singles': {
        songs: [
            107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 
            124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 
            141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 
            158, 159, 160, 161
        ],
        title: 'Singles',
        author: 'Azuko'
    },
    'Featurings': {
        songs: [
            162, 163, 164, 165, 166, 167, 168, 169, 170, 171
        ],
        title: 'Featurings',
        author: 'Azuko'
    }
}
    
for (album in albums) {
    for (let i = 0; i < albums[album].track_number; i++) {
        if (albums[album].track_artist instanceof Array) {
            all_songs.push({
                "name": albums[album].track_name[i],
                "artist": albums[album].track_artist[i],
                "album": albums[album].album_title,
                "url": albums[album].audio_dir + '/' + `${i}` + '.mp3',
                "cover_art_url": albums[album].cover
            })
        } else {
            all_songs.push({
                "name": albums[album].track_name[i],
                "artist": albums[album].track_artist,
                "album": albums[album].album_title,
                "url": albums[album].audio_dir + '/' + `${i}` + '.mp3',
                "cover_art_url": albums[album].cover
            })
        }
    }
}

for (let index = 0; index < singles.track_number; index++) {
    all_songs.push({
        "name": singles.track_name[index],
        "artist": singles.track_artist[index],
        "url": singles.audio_dir + '/' + `${index}` + '.mp3',
        "cover_art_url": singles.cover[index]
    })
}

for (let index = 0; index < featurings.track_number; index++) {
    all_songs.push({
        "name": featurings.track_name[index],
        "artist": featurings.track_artist[index],
        "url": featurings.audio_dir + '/' + `${index}` + '.mp3',
        "cover_art_url": featurings.cover[index]
    })
}
