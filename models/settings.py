from os import getenv
from os.path import join
from dotenv import load_dotenv


class Settings:
    def __init__(self):
        self.dotenv_path = join('environment', '.env')
        self.load_dotenv_file()
        self.db_driver = getenv("DB_DRIVER")
        self.db_user = getenv("DB_USER")
        self.db_password = getenv("DB_PASSWORD")
        self.db_host = getenv("DB_HOST")
        self.db_port = getenv("DB_PORT")
        self.db_name = getenv("DB_NAME")

    def load_dotenv_file(self):
        load_dotenv(self.dotenv_path)

    def get_database_url(self):
        return f'{self.db_driver}://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}'
