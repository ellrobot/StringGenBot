from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")
MONGO_DB_URI = getenv("MONGO_DB_URL", None)

OWNER_ID = int(getenv("OWNER_ID", 6855539355))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/zyriccbase")
