/* PRELOADER */
document.addEventListener("DOMContentLoaded", function () {
    setTimeout(function () {
        document.querySelector("body").classList.add("loaded");
    }, 500)
});

/* MAIN 2 BACKGROUND */
const main_2_div = document.querySelector('.main_2');
let images_main_2 = document.querySelectorAll('col-3');
images_main_2.forEach((image) => {
    image.addEventListener('mouseenter', (e) => {
        main_2_div.style.backgroundImage = "url(../../static/images/last_releases/0.jpg)";
    });
    image.addEventListener('mouseleave', (e) => {
        main_2_div.style.backgroundImage = ''
    });
})
