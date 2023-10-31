<div id="header" align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdDFxdjIwZDcwa3JpdDFmOGYxcHFwbmI0bnV3bXg0OXdmaWhiZHZ0bCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/oV7m7OaPe86aJzZwRC/giphy.gif" width="500"/>
</div>

# Welcome to Azuko!

Azuko is a static artist website with the ability to listen to all his tracks

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

## Databases (default: `Postgres`)

If you are using Postgres, you will first need to create a database with the name (`db_name`) you added to your `.env` file (if you use MySQL or SQLite, you don't need to create the database manually, as it will be created automatically). This code will make all things:

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

Open terminal & run command below

```bash
python project.py
```

Well done!

```bash
(Azuko) <???>@<???> Azuko % python3 project.py 
INFO:     Will watch for changes in these directories: ['/<your_path_to_project>/Azuko']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [11855] using WatchFiles
INFO:     Started server process [11857]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

## Updates
Updates coming soon!


## Contributing

Forks are welcome.