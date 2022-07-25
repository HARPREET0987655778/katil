## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("", "AQA2BUmo07qs2V6z8UhuhS5UYAFk-OD-RnKxqtR2Ksu2fo7JH_306clwUQaOie-horakOAvMtlB_tiDQMP7bd-sgGeDuem5CiPcVxPOWp0W4c6SI1MPpM1u2swzrRtV08lvq-kHHZwkQFIVNEqT1knyMCnaf_sMXgRsmMvKDRxQ_mbRwSRu_RstPtle0P-qHnah84dkDNDC_OHsYG5u747FlOzd1mHWMnCTaAKSdc39OJ2nSNQnEisRgdXAKpP4pyi7N0j7ax2SnIAh-rG_75O3wPNUxAdE2cgj0HbWQbwts1Fvz9bR_dsGnWTf35TV7ijcPl1HOcsGExAtI1MtUfWpQAAAAATHYCs8A")
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
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1834450801").split()))
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
