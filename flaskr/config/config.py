import os
from dotenv import load_dotenv
load_dotenv()

current_env = os.environ.get('FLASK_ENV')
if current_env == 'development':
    LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN_DEV')
    LINE_CHANNEL_SECRET = os.getenv('LINE_CHANNEL_SECRET_DEV')
    HOTPEPPER_API_KEY = os.getenv('HOTPEPPER_API_KEY')
    LIFFURL_STARTER = os.getenv('LIFFURL_STARTER_DEV')
    LIFFURL_KEYWORD = os.getenv('LIFFURL_KEYWORD_DEV')
    LIFFURL_FAVORITE = os.getenv('LIFFURL_FAVORITE_DEV')
else:
    LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
    LINE_CHANNEL_SECRET = os.getenv('LINE_CHANNEL_SECRET')
    HOTPEPPER_API_KEY = os.getenv('HOTPEPPER_API_KEY')
    POSTGRESQL_DB_URI = os.getenv('POSTGRESQL_DB_URI')
    LIFFURL_STARTER = os.getenv('LIFFURL_STARTER')
    LIFFURL_KEYWORD = os.getenv('LIFFURL_KEYWORD')
    LIFFURL_FAVORITE = os.getenv('LIFFURL_FAVORITE')


