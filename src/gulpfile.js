const { src, dest, watch, series, task } = require('gulp')
let uglify = require('gulp-uglify');
let concat = require('gulp-concat');
let concatCss = require('gulp-concat-css');
const cleanCSS = require('gulp-clean-css');

task('js', done => {
  src([
    'static/js/preloader.js',
    'static/js/projects.js',
    'node_modules/amplitudejs/dist/amplitude.js',
    'static/js/songs.js',
    'static/js/main.js',
    'node_modules/bootstrap/dist/js/bootstrap.bundle.min.js'
  ])
    .pipe(concat('bundle.min.js'))
    .pipe(uglify())
    .pipe(dest('static/public/'));
  done();
})

task('css', done => {
  src([
    'static/css/*.css',
    'node_modules/bootstrap/dist/css/bootstrap.min.css'
  ])
    .pipe(concatCss('bundle.min.css'))
    .pipe(cleanCSS({ compatibility: 'ie8' }))
    .pipe(dest('static/public/'));
  done();
})

task('js_css_watch', function () {
  watch('css/*.css', css);
  watch('js/*.js', js)
})

task('js_css', done => {
  series('js', 'css')
  done();
})