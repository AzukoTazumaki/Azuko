const { src, dest, watch } = require('gulp')
let uglify = require('gulp-uglify');
let concat = require('gulp-concat');
let concatCss = require('gulp-concat-css');
const cleanCSS = require('gulp-clean-css');

function js() {
  return src([
    'js/preloader.js',
    'js/projects.js',
    'node_modules/amplitudejs/dist/amplitude.js',
    'node_modules/amplitudejs/dist/visualizations/circular-equalizer.js',
    'js/songs.js',
    'js/main.js',
    'node_modules/bootstrap/dist/js/bootstrap.bundle.min.js'
  ])
    .pipe(concat('bundle.min.js'))
    .pipe(uglify())
    .pipe(dest('dist/'));
}

function css() {
  return src([
    'css/*.css',
    'node_modules/bootstrap/dist/css/bootstrap.min.css'
  ])
    .pipe(concatCss('bundle.min.css'))
    .pipe(cleanCSS({ compatibility: 'ie8' }))
    .pipe(dest('dist/'));
}

exports.js_css = function () {
  watch('css/*.css', css);
  watch('js/*.js', js)
}