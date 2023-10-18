from os import getenv
from dotenv import load_dotenv

load_dotenv()
db_driver = getenv("DB_DRIVER")
db_user = getenv("DB_USER")
db_password = getenv("DB_PASSWORD")
db_host = getenv("DB_HOST")
db_port = getenv("DB_PORT")
db_name = getenv("DB_NAME")

db_url = f'{db_driver}://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'