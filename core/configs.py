from sqlalchemy.ext.declarative import declarative_base
from fastapi.templating import Jinja2Templates
from pydantic import BaseSettings
from decouple import config
from pathlib import Path


class Settings(BaseSettings):
    DB_URL: str = config('DB_URL')
    DBBaseModel = declarative_base()
    TEMPLATES = Jinja2Templates(directory='templates')
    MEDIA = Path('media')

    class Config:
        case_sensitive = True

settings: Settings = Settings()
