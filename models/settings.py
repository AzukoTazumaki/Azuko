from os import getenv
from os.path import join
from dotenv import load_dotenv


class Settings:
    def __init__(self):
        self.dotenv_path = join('environment', '.env')
        self.load_dotenv_file()

    def load_dotenv_file(self):
        load_dotenv(self.dotenv_path)

    @staticmethod
    def get_database_url():
        db_driver = getenv("DB_DRIVER")
        db_user = getenv("DB_USER")
        db_password = getenv("DB_PASSWORD")
        db_host = getenv("DB_HOST")
        db_port = getenv("DB_PORT")
        db_name = getenv("DB_NAME")
        return f'{db_driver}://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
