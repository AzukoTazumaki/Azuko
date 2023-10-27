try {
    let play_pause_icon = document.querySelector('.play_pause_icon')
    let volume_percentage = document.querySelector('.volume_percentage')

    /* INIZIALIZATION OF AMPLITUDE */
    Amplitude.init({
        songs: all_songs,
        volume: 15,
        debug: true,
        callbacks: {
            play: function () {
                play_pause_icon.classList.remove('fa-circle-play');
                play_pause_icon.classList.add('fa-circle-pause');
            },
            pause: function () {
                play_pause_icon.classList.remove('fa-circle-pause');
                play_pause_icon.classList.add('fa-circle-play');
            }
        },
        playlists: all_playlists
    });

    /* SHUFFLE BUTTON */
    let shuffle_button = document.querySelector('.shuffle_song_button')
    shuffle_button.addEventListener('click', () => {
        if (shuffle_button.style.color == 'var(--white-rgb)') {
            shuffle_button.style.color = 'var(--periwinkle-purple-rgb)'
            shuffle_button.style.textShadow = 'var(--black-shadow)'
        } else {
            shuffle_button.style.color = 'var(--white-rgb)'
            shuffle_button.style.textShadow = 'var(--white-shadow)'
        }
    })


    /* REPEAT BUTTON */
    let repeat_button = document.querySelector('.repeat_song_button')
    repeat_button.addEventListener('click', () => {
        if (repeat_button.style.color == 'var(--white-rgb)') {
            repeat_button.style.color = 'var(--periwinkle-purple-rgb)'
            repeat_button.style.textShadow = 'var(--black-shadow)'
        } else {
            repeat_button.style.color = 'var(--white-rgb)'
            repeat_button.style.textShadow = 'var(--white-shadow)'
        }
    })

    /* VOLUME BUTTON */
    let volume_slider = document.querySelector('.volume_slider')
    let volume_button = document.querySelector('.volume_song_button')
    let volume_song_icon = document.querySelector('.volume_song_icon')

    volume_slider.addEventListener('input', (el) => {
        let el_value = el.target.value
        let classes = ['fa-volume-xmark', 'fa-volume-off', 'fa-volume-low', 'fa-volume-high']
        volume_percentage.innerText = el_value
        if (el_value == 0) {
            volume_song_icon.classList.remove(...classes)
            volume_song_icon.classList.add(classes[0])
        } else if (el_value > 0 && el_value < 25) {
            volume_song_icon.classList.remove(...classes)
            volume_song_icon.classList.add(classes[1])
        } else if (el_value >= 25 && el_value < 60) {
            volume_song_icon.classList.remove(...classes)
            volume_song_icon.classList.add(classes[2])
        } else {
            volume_song_icon.classList.remove(...classes)
            volume_song_icon.classList.add(classes[3])
        }
    })

    volume_button.addEventListener('click', () => {
        if (!volume_song_icon.classList.contains('fa-volume-xmark')) {
            volume_song_icon.classList.add('fa-volume-xmark')
        } else {
            volume_song_icon.classList.remove('fa-volume-xmark')
        }
    })


    let song_lyrics = document.querySelectorAll('.song_lyrics')
    window.onclick = function () {
        song_lyrics.forEach(elem => {
            let active_song = document.querySelector('.active_song')
            let data_title = document.querySelector('.song_title_name').innerText
            let data_lyrics = elem.dataset.lyricsSong
            if (data_title == data_lyrics) {
                elem.style.display = 'block'
            } else {
                elem.style.display = 'none'
            }
        })
    }

} catch (error) {

};

