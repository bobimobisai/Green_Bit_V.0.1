from dotenv import load_dotenv
from os import getenv

load_dotenv(".env")
token = getenv("BOT_TOKEN")
db_user = getenv("DATA_BASE_USER")
db_pass = getenv("DATA_BASE_PASSWORD")
