## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("AQAmUXSBRvyYgolf_hcTXVLAmAOWRcoAS4Tc6IFHqKQ5hmUpOuD4xpiUQMG3xzYwtlWVmlU2Rl7Bt_1dsk8OInkKp54Qbi4mrFgwlsw5380K-okE09LxCrctP7PbpK1yv2-sfiYevdhZvuuLDd-RjotRCbn0GVph5YF1ILwSyfYdtIZ7E0AwJWKYCe6HHZm8G7s0XQF8jT9KJv2_b9HLbyccOBHifmRE9KcIz_a0v_-DDvrxRCDqIrbOhXtI9ukoH7QcjJvCo_meJ5UAoAuTiM3Wrepv09Z_y5NmHEz3aD07aw3yutqCE5vM2Mc9zEc32gFPBvz803qJKX1ODn6n-NdoAAAAATNUmxoA", "AQAmUXSBRvyYgolf_hcTXVLAmAOWRcoAS4Tc6IFHqKQ5hmUpOuD4xpiUQMG3xzYwtlWVmlU2Rl7Bt_1dsk8OInkKp54Qbi4mrFgwlsw5380K-okE09LxCrctP7PbpK1yv2-sfiYevdhZvuuLDd-RjotRCbn0GVph5YF1ILwSyfYdtIZ7E0AwJWKYCe6HHZm8G7s0XQF8jT9KJv2_b9HLbyccOBHifmRE9KcIz_a0v_-DDvrxRCDqIrbOhXtI9ukoH7QcjJvCo_meJ5UAoAuTiM3Wrepv09Z_y5NmHEz3aD07aw3yutqCE5vM2Mc9zEc32gFPBvz803qJKX1ODn6n-NdoAAAAATNUmxoA")
BOT_TOKEN = getenv("5585173601:AAHfBp0qy5N_TS-eNu-82bYpqlrw54Vr7PM", "5585173601:AAHfBp0qy5N_TS-eNu-82bYpqlrw54Vr7PM")
BOT_NAME = getenv("SHIZUKA", "SHIZUKA")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "ITZ_HARPREET_OP")
OWNER_USERNAME = getenv("OWNER_USERNAME", "ITZ_HARPREET_OP")
ALIVE_NAME = getenv("ALIVE_NAME", "SHIZUKA")
BOT_USERNAME = getenv("BOT_USERNAME", "Shizuka_Music_Bot")
OWNER_ID = getenv("OWNER_ID", "1834450801")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "SHIZUKAXASSISTANT")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "ITZ_HARPREET_OP")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ITZ_HARPREET_OP")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1669178360").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "180"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/c540aac0249486854787b.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6f1cfec700087f6fcb391.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/c3547532105a0cb67229d.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c3401a572375b569138c3.png")
