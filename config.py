from pydantic import BaseSettings
from dotenv import load_dotenv
import os


load_dotenv()


class Settings(BaseSettings):
    DB_URL = os.getenv("SQLALCHEMY_DATABASE_URL")


settings = Settings()