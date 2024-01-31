import platform
import config
import psutil
import time
import random
from daxxop import daxxop
from pyrogram import Client, filters
from pyrogram.types import Message

start_time = time.time()


# █ ✪ █▓▓▓▓▓ [BADBABY] ▓▓▓▓█ ✪ █#

PING_PIC = [
    "https://telegra.ph/file/625d235cc0a22fb8525b5.jpg",
    ]
# ------------------------------------------------------------------------------- #




def time_formatter(milliseconds):
    minutes, seconds = divmod(int(milliseconds / 1000), 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    weeks, days = divmod(days, 7)
    tmp = (((str(weeks) + "ᴡ:") if weeks else "") +
           ((str(days) + "ᴅ:") if days else "") +
           ((str(hours) + "ʜ:") if hours else "") +
           ((str(minutes) + "ᴍ:") if minutes else "") +
           ((str(seconds) + "s") if seconds else ""))
    if not tmp:
        return "0s"
    if tmp.endswith(":"):
        return tmp[:-1]
    return tmp

@daxxop.on_message(filters.command("ping"))
async def activevc(_, message: Message):
    uptime = time_formatter((time.time() - start_time) * 1000)
    cpu = psutil.cpu_percent()
    storage = psutil.disk_usage('/')
    
    python_version = platform.python_version()

    TEXT = (
        f"➪ᴜᴘᴛɪᴍᴇ: {uptime}\n"
        f"➪ᴄᴘᴜ: {cpu}%\n"
        f"➪ꜱᴛᴏʀᴀɢᴇ: {size_formatter(storage.total)} (Total)\n"
        f"➪{size_formatter(storage.used)} (Used)\n"
        f"➪{size_formatter(storage.free)} (Free)\n"
        f"➪ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ: {python_version}\n"
    )

    await message.reply_photo(
        photo=random.choice(PING_PIC),
        caption=TEXT,
    )

def size_formatter(bytes, suffix='B'):
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(bytes) < 1024.0:
            return "%3.1f %s%s" % (bytes, unit, suffix)
        bytes /= 1024.0
    return "%.1f %s%s" % (bytes, 'Y', suffix)
