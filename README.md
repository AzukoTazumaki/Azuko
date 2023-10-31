<div id="header" align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdDFxdjIwZDcwa3JpdDFmOGYxcHFwbmI0bnV3bXg0OXdmaWhiZHZ0bCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/oV7m7OaPe86aJzZwRC/giphy.gif" width="500"/>
</div>

# Welcome to Azuko!

`Azuko` is a static (for now) artist website with the ability to listen to all his tracks

## Clone the repository

### Open terminal:

Go to the directory where site `Azuko` will be

```bash
cd <name_of_your_directory>
```

Clone repository

```bash
git clone https://github.com/AzukoTazumaki/Azuko.git
```

Go to the `Azuko`

```bash
cd Azuko/
```

## Make an environment & install requirements

### `Pip`:

```bash
python -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

### `Pipenv`:

```bash
python -m pipenv shell

pipenv install
```

## Install requirements from `package.json`

In terminal:

```bash
cd static/

npm install
```

If you want to make some changes in `.css` or `.js` files, run command below in this directory:

```bash
npm run gulp
```

You must see:

```bash
<???>:static ???$ npm run gulp

> static@1.0.0 gulp
> gulp js_css

[??:??:??] Using gulpfile ~/<your_path_to_project>/Azuko/static/gulpfile.js
[??:??:??] Starting 'js_css'...
```

This means that `Gulp` now looks at all `js` and `css` files, so that when you change anything in styles or scripts, `Gulp` will automatically save everything into bundle (`bundle.min.css` and `bundle.min.js`) files. When you clone a project, the compiled files are there in advance, so you don’t need to create a bundle initially.

## Create `.env` file with example in `.dev.env`

```python
# CREATE YOUR OWN .env FILE & SET THE PREFERENCES

DB_DRIVER='db_driver'
DB_USER='user'
DB_PASSWORD='password'
DB_HOST='host'
DB_PORT='port'
DB_NAME='db_name'
```

## Databases (only `Postgres` for now)

For using Postgres, you will first need to create a database with the name (`db_name`) you added to your `.env` file. This code will make all things:

```python
@asynccontextmanager
async def startup(app: FastAPI):
    yield
    try:
        init_db = InitDatabase()
        init_db.create_tables()
        init_db.create_projects()
        init_db.close_session()
    except IntegrityError:
        pass
```

When installing dependencies, supporting package for connecting driver are automatically installed (`psycopg2` for Postgres, full `db_driver` is `postgresql+psycopg2`). Before using Postgres, don't forget to export the paths to Postgres like this:

```bash
# .zshrc file

export PATH="/usr/local/opt/postgresql@16/bin:$PATH"
```

After completing all preparations open terminal & run command below

```bash
python project.py
```

Well done!

```bash
(Azuko) <???>@<???> Azuko % python3 project.py 
INFO:     Will watch for changes in these directories: ['/<your_path_to_project>/Azuko']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [?????] using WatchFiles
INFO:     Started server process [?????]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

## Updates
Updates coming soon!


## Contributing

Forks are welcome.