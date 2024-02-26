import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
ADMINS = str(os.getenv("ADMIN"))
POSTGRES_URI = str(os.getenv("POSTGRES_URI"))

ip = os.getenv("ip")
db_host = ip
aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}



