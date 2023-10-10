/* PRELOADER */
document.addEventListener("DOMContentLoaded", function () {
    setTimeout(function () {
        document.querySelector("body").classList.add("loaded");
    }, 500)
})

try {
    /* SINGLES SHOW MORE BUTTON */

    let show_more_singles_btn = document.getElementById('show_more_singles_button')
    let singles_cards_row = document.getElementById('singles_cards')
    let disabled_single_cards = document.querySelectorAll('.disabled_single_card')

    show_more_singles_btn.addEventListener('click', () => {
        let singles_array = [show_more_singles_btn, singles_cards_row]
        disabled_single_cards.forEach((card) => {
            common_show_more_function(card, singles_array)
        });
    })

    /* FEATURINGS SHOW MORE BUTTON */

    let show_more_featurings_btn = document.getElementById('show_more_featurings_button')
    let featurings_cards_row = document.getElementById('featurings_cards')
    let disabled_featuring_cards = document.querySelectorAll('.disabled_featuring_card')

    show_more_featurings_btn.addEventListener('click', () => {
        let featurings_array = [show_more_featurings_btn, featurings_cards_row]
        disabled_featuring_cards.forEach((card) => {
            common_show_more_function(card, featurings_array)
        });
    })

    /* COMMON SHOW MORE FUNCTION */

    function common_show_more_function(card, array) {
        if (card.style.display === 'block') {
            card.style.display = 'none';
            array[1].classList.add('vh-100')
            array[1].style.paddingTop = '0'
            array[0].innerHTML = 'SHOW MORE'
        } else {
            card.style.display = 'block';
            array[1].classList.remove('vh-100')
            array[1].style.paddingTop = '17vh'
            array[0].innerHTML = 'SHOW LESS'
        }
    }

} catch (error) {
    console.log(error)
}

const audio_albums_path = 'static/audio/albums'
const with_love_from_azuko_audio_dir = audio_albums_path + '/with_love_from_azuko'


/*
  When the bandcamp link is pressed, stop all propagation so AmplitudeJS doesn't
  play the song.
*/
let bandcampLinks = document.getElementsByClassName('bandcamp-link');

for (var i = 0; i < bandcampLinks.length; i++) {
    bandcampLinks[i].addEventListener('click', function (e) {
        e.stopPropagation();
    });
}


let songElements = document.getElementsByClassName('song');

for (var i = 0; i < songElements.length; i++) {
    /*
      Ensure that on mouseover, CSS styles don't get messed up for active songs.
    */
    songElements[i].addEventListener('mouseover', function () {
        this.style.backgroundColor = '#00A0FF';

        this.querySelectorAll('.song-meta-data .song-title')[0].style.color = '#FFFFFF';
        this.querySelectorAll('.song-meta-data .song-artist')[0].style.color = '#FFFFFF';

        if (!this.classList.contains('amplitude-active-song-container')) {
            this.querySelectorAll('.play-button-container')[0].style.display = 'block';
        }

        this.querySelectorAll('img.bandcamp-grey')[0].style.display = 'none';
        this.querySelectorAll('img.bandcamp-white')[0].style.display = 'block';
        this.querySelectorAll('.song-duration')[0].style.color = '#FFFFFF';
    });

    /*
      Ensure that on mouseout, CSS styles don't get messed up for active songs.
    */
    songElements[i].addEventListener('mouseout', function () {
        this.style.backgroundColor = '#FFFFFF';
        this.querySelectorAll('.song-meta-data .song-title')[0].style.color = '#272726';
        this.querySelectorAll('.song-meta-data .song-artist')[0].style.color = '#607D8B';
        this.querySelectorAll('.play-button-container')[0].style.display = 'none';
        this.querySelectorAll('img.bandcamp-grey')[0].style.display = 'block';
        this.querySelectorAll('img.bandcamp-white')[0].style.display = 'none';
        this.querySelectorAll('.song-duration')[0].style.color = '#607D8B';
    });

    /*
      Show and hide the play button container on the song when the song is clicked.
    */
    songElements[i].addEventListener('click', function () {
        this.querySelectorAll('.play-button-container')[0].style.display = 'none';
    });
}


Amplitude.init({
    "songs": [
        {
            "name": "Моя Вина",
            "artist": "Azuko",
            "album": "with love from Azuko",
            "url": with_love_from_azuko_audio_dir + '/my_fault.wav',
        },
        {
            "name": "Ничего Лишнего",
            "artist": "Azuko",
            "album": "with love from Azuko",
            "url": with_love_from_azuko_audio_dir + '/nothing_else.wav',
        },
        {
            "name": "Занят",
            "artist": "Azuko",
            "album": "with love from Azuko",
            "url": with_love_from_azuko_audio_dir + '/busy.wav',
        },
        {
            "name": "Время Летит",
            "artist": "Azuko",
            "album": "with love from Azuko",
            "url": with_love_from_azuko_audio_dir + '/time_is_gone.wav',
        },
        {
            "name": "Babe <3",
            "artist": "Azuko",
            "album": "with love from Azuko",
            "url": with_love_from_azuko_audio_dir + '/babe.wav',
        },
        {
            "name": "Маньяк",
            "artist": "Azuko",
            "album": "with love from Azuko",
            "url": with_love_from_azuko_audio_dir + '/maniac.wav',
        },
        {
            "name": "Время Покажет",
            "artist": "Azuko",
            "album": "with love from Azuko",
            "url": with_love_from_azuko_audio_dir + '/time_will_show.wav',
        },
        {
            "name": "Может Быть",
            "artist": "Azuko",
            "album": "with love from Azuko",
            "url": with_love_from_azuko_audio_dir + '/maybe.wav',
        }
    ],
    "default_album_art": with_love_from_azuko_audio_dir + '/cover.jpg'
});

