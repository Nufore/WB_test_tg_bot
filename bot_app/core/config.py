import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")


class Settings(BaseSettings):
    bot_key: str = BOT_TOKEN


settings = Settings()
