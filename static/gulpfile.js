const { src, dest, watch } = require('gulp')
let uglify = require('gulp-uglify');
let concat = require('gulp-concat');
let concatCss = require('gulp-concat-css');
const cleanCSS = require('gulp-clean-css');
function js() {
  return src([
    'node_modules/bootstrap/dist/js/bootstrap.min.js',
    'js/preloader.js',
    'js/projects.js',
    'node_modules/amplitudejs/dist/amplitude.js',
    'js/songs.js',
    'js/main.js'
  ])
    .pipe(concat('bundle.min.js'))
    .pipe(uglify())
    .pipe(dest('public/'));
}
function css() {
  return src([
    'css/*.css',
    'node_modules/bootstrap/dist/css/bootstrap.min.css'
  ])
    .pipe(concatCss('bundle.min.css'))
    .pipe(cleanCSS({ compatibility: 'ie8' }))
    .pipe(dest('public/'));
}
exports.js_css = function () {
  watch('css/*.css', css);
  watch('js/*.js', js)
}