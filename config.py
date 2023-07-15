from pydantic import BaseSettings
from dotenv import load_dotenv
import os


load_dotenv()


class Settings(BaseSettings):
    # DB_USER:str =  os.getenv('DB_USER')
    # DB_PASSWORD:str = os.getenv('DB_PASSWORD')
    # DB_HOST:str = os.getenv('DB_HOST')
    # DB_PORT:str = os.getenv('DB_PORT')
    # DB_NAME:str = os.getenv('DB_NAME')
    # DB_SSL_MODE:str = os.getenv('DB_SSL_MODE')

    # DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?sslmode={DB_SSL_MODE}"
    DB_URL:str = os.getenv("SQLALCHEMY_DATABASE_URL")

settings = Settings()