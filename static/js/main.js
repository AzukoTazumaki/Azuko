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

/* PLAY_PAUSE BUTTON */
const play_pause_button = document.querySelector('.play_pause_song_button')
const play_pause_icon = document.querySelector('.play_pause_icon')

/* INIZIALIZATION OF AMPLITUDE */
Amplitude.init({
    bindings: {
        39: 'next',
        37: 'prev'
    },
    songs: all_songs,
    volume: 35,
    debug: true,
    callbacks: {
        play: function () {
            play_pause_icon.classList.remove('fa-play');
            play_pause_icon.classList.add('fa-pause');
        },
        pause: function () {
            play_pause_icon.classList.remove('fa-pause');
            play_pause_icon.classList.add('fa-play');
        }
    }
});

/* SHUFFLE BUTTON */
const shuffle_button = document.querySelector('.shuffle_song_button')
shuffle_button.addEventListener('click', () => {
    if (shuffle_button.style.color == 'var(--white-rgb)') {
        shuffle_button.style.color = 'var(--periwinkle-purple-rgb)'
        shuffle_button.style.textShadow = 'var(--periwinkle-purple-shadow)'
    } else {
        shuffle_button.style.color = 'var(--white-rgb)'
        shuffle_button.style.textShadow = 'var(--white-shadow)'
    }
})

/* REPEAT BUTTON */
const repeat_button = document.querySelector('.repeat_song_button')
repeat_button.addEventListener('click', () => {
    if (repeat_button.style.color == 'var(--white-rgb)') {
        repeat_button.style.color = 'var(--periwinkle-purple-rgb)'
        repeat_button.style.textShadow = 'var(--periwinkle-purple-shadow)'
    } else {
        repeat_button.style.color = 'var(--white-rgb)'
        repeat_button.style.textShadow = 'var(--white-shadow)'
    }
})


