const { src, dest, watch, series, task } = require('gulp')
let uglify = require('gulp-uglify');
let concat = require('gulp-concat');
let concatCss = require('gulp-concat-css');
const cleanCSS = require('gulp-clean-css');

function js() {
  return src([
    'src/static/js/preloader.js',
    'src/static/js/projects.js',
    'src/node_modules/amplitudejs/dist/amplitude.js',
    'src/static/js/songs.js',
    'src/static/js/main.js',
    'src/node_modules/bootstrap/dist/js/bootstrap.bundle.min.js'
  ])
    .pipe(concat('bundle.min.js'))
    .pipe(uglify())
    .pipe(dest('src/static/public/'));
}

function css() {
  return src([
    'src/static/css/*.css',
    'src/node_modules/bootstrap/dist/css/bootstrap.min.css'
  ])
    .pipe(concatCss('bundle.min.css'))
    .pipe(cleanCSS({ compatibility: 'ie8' }))
    .pipe(dest('src/static/public/'));
}

task('js', js)
task('css', css)

task('js_css_watch', function () {
  watch('css/*.css', css);
  watch('js/*.js', js)
})

task('js_css', done => {
  series('js', 'css')
  done();
})