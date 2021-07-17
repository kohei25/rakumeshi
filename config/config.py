import os
from dotenv import load_dotenv
load_dotenv()

LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
LINE_CHANNEL_SECRET = os.getenv('LINE_CHANNEL_SECRET')
HOTPEPPER_API_KEY = os.getenv('HOTPEPPER_API_KEY')
POSTGRESQL_DB_URI = os.getenv('POSTGRESQL_DB_URI')
