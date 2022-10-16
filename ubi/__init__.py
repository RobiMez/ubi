import os
import logging
from pathlib import Path
from telethon import TelegramClient, connection
from dotenv import load_dotenv

load_dotenv(dotenv_path=Path('.env'))

APP_SESSION = "ubi"
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")

USERBOT_LOAD = []
USERBOT_NOLOAD = []

# proxy , remove if you dont need one 
u = TelegramClient(APP_SESSION, api_id=int(API_ID), api_hash=API_HASH).start()

LOG_FORMAT = "[%(asctime)s.%(msecs)03d] %(filename)s:%(lineno)s %(levelname)s: %(message)s"


logging.basicConfig(level=logging.INFO,
                    format=LOG_FORMAT,
                    datefmt='%m-%d %H:%M',)

log = logging.getLogger()
