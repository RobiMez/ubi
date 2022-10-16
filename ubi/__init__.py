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
u = TelegramClient(APP_SESSION, api_id=int(API_ID), api_hash=API_HASH,
                   connection=connection.ConnectionTcpMTProxyRandomizedIntermediate,
                   proxy=('russia-dd.proxy.digitalresistance.dog',
                          443, 'ddd41d8cd98f00b204e9800998ecf8427e')
                   ).start()

LOG_FORMAT = "[%(asctime)s.%(msecs)03d] %(filename)s:%(lineno)s %(levelname)s: %(message)s"


logging.basicConfig(level=logging.INFO,
                    format=LOG_FORMAT,
                    datefmt='%m-%d %H:%M',)

log = logging.getLogger()
