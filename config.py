from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("17250424"))
API_HASH = getenv("753bc98074d420ef57ddf7eb1513162b")

BOT_TOKEN = getenv("6830518422:AAEPRM-cfMZjZk6yCHqg61aY3Q-qqONgot0")
MONGO_DB_URI = getenv("mongodb+srv://1234:1234@cluster0.gb6uhwg.mongodb.net/?retryWrites=true&w=majority", None)

OWNER_ID = int(getenv("OWNER_ID", 6855539355))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/zyriccbase")
