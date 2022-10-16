import asyncio
import time , importlib

from ubi import u , log
from ubi.modules import ALL_MODULES

loop = asyncio.get_event_loop()


async def main():
    await u.start()
    for modul in ALL_MODULES:
        log.info(f"💾 Loading : {modul}" )
        importlib.import_module("ubi.modules." + modul)
    log.info("🔥 Bot online !")
    await u.run_until_disconnected()


if __name__ == '__main__':
    BOT_RUNTIME = int(time.time())
    loop.run_until_complete(main())
    log.info("💀 Bot Dead !")


