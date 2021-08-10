# Regen & Mod by @shamilhabeebnelli
# Pyrogram - Telegram MTProto API Client Library for Python
# Copyright (C) 2017-2020 Dan <https://github.com/delivrance>
#
# This file is part of Pyrogram.
#
# Pyrogram is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pyrogram is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

import os
import re
from youtube_dl import YoutubeDL
ydl_opts = {
    "geo-bypass": True,
    "nocheckcertificate": True
    }
ydl = YoutubeDL(ydl_opts)
links=[]
finalurl=""
STREAM=os.environ.get("STREAM_URL", "http://node-25.zeno.fm/kezsc0y2wwzuv?listening-from-radio-garden=1622271954020&rj-ttl=5&rj-tok=AAABec5bAE4Aj31dmRAEFgcbvw")
regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
match = re.match(regex,STREAM)
if match:
    meta = ydl.extract_info(STREAM, download=False)
    formats = meta.get('formats', [meta])
    for f in formats:
        links.append(f['url'])
    finalurl=links[0]
else:
    finalurl=STREAM

class Config:
    ADMIN = os.environ.get("ADMINS", '1185346119')
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = int(os.environ.get("API_ID", '1492128'))
    CHAT = int(os.environ.get("CHAT", "-1001403236771"))
    LOG_GROUP=os.environ.get("LOG_GROUP", "-1001403236771")
    if LOG_GROUP:
        LOG_GROUP=int(LOG_GROUP)
    else:
        LOG_GROUP=None
    STREAM_URL=finalurl
    ADMIN_ONLY=os.environ.get("ADMIN_ONLY", "N")
    ARQ_API=os.environ.get("ARQ_API", "ZCGMTA-WTNMXA-AXBKXK-SWVFVH-ARQ")
    REPLY_MESSAGE=os.environ.get("REPLY_MESSAGE", None)
    DURATION_LIMIT=int(os.environ.get("DUR", 15))
    API_HASH = os.environ.get("API_HASH", "496a1aab7943406f28e3de49fff16ea2")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1757219716:AAFUuhq93FR4ggr_xwwgueGIZa0wljD2Qhc") 
    SESSION = os.environ.get("SESSION_STRING", "BQApa8zk11VMBfzwIO1AinC0lCnYWeZrVZaqWgbGvi2bxMFjHpsmIdIKh6AirAqHsF6hl0TnyQDXsWr_TU_N_IseVvQcfjnWLdfYHy_5wol9nRdRD6BEPwhGGWhoAAJAGWKQw-fgR-REtOUN52FsTjKL6y2XmpxxF4NIT-Way43NFKlmL6sDCKellKPOIClhCgByZKQ2q5ZXTzpz_BiHXFtIwTv6nRdAzSVP7x0Zl_c9LXyoqAEq3N4RYKPQJ_Y6gpKrQeJ53CrRyrvV0nMlQ7lTKD50awxqrEMmbby3Nb-2RcELldk431jkMxkxzYn97oYvt2JTAtwnsaOWNAzDKiR4RqbyRwA")
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")
    playlist=[]
    msg = {}
