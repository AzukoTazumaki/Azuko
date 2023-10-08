/* PRELOADER */
document.addEventListener("DOMContentLoaded", function () {
    setTimeout(function () {
        document.querySelector("body").classList.add("loaded");
    }, 500)
})

/* SINGLES SHOW MORE BUTTON */

const show_more_singles_btn = document.getElementById('show_more_singles_button')
const singles_cards_row = document.getElementById('singles_cards')
const disabled_single_cards = document.querySelectorAll('.disabled_single_card')

show_more_singles_btn.addEventListener('click', () => {
    let singles_array = [show_more_singles_btn, singles_cards_row]
    disabled_single_cards.forEach((card) => {
        common_show_more_function(card, singles_array)
    });
})

/* FEATURINGS SHOW MORE BUTTON */

const show_more_featurings_btn = document.getElementById('show_more_featurings_button')
const featurings_cards_row = document.getElementById('featurings_cards')
const disabled_featuring_cards = document.querySelectorAll('.disabled_featuring_card')

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

