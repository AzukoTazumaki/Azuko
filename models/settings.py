from os import getenv
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join('environment', '.env')
load_dotenv(dotenv_path)

db_driver = getenv("DB_DRIVER")
db_user = getenv("DB_USER")
db_password = getenv("DB_PASSWORD")
db_host = getenv("DB_HOST")
db_port = getenv("DB_PORT")
db_name = getenv("DB_NAME")

db_url = f'{db_driver}://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
