from telethon import events
from ubi import u

@u.on(events.NewMessage( pattern=r'\.ping'))
async def pingH(event):
    await event.reply("Pong.")
