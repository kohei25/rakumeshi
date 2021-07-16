from flask import Flask, request, abort

# LINE module
from linebot import (
	LineBotApi, WebhookHandler
)
from linebot.exceptions import (
	InvalidSignatureError
)
from line.chat_template.scenario import (
	chat_scenario
)

# database
# from db.database import db_session, init_db

# environment variables
from config import config

app = Flask(__name__)
# init_db()

# production environment
line_bot_api = LineBotApi(config.LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(config.LINE_CHANNEL_SECRET)

# dev environment
# line_bot_api = LineBotApi(config.LINE_CHANNEL_ACCESS_TOKEN_DEV)
# handler = WebhookHandler(config.LINE_CHANNEL_SECRET_DEV)

# @app.teardown_appcontext
# def shutdown_session(exception=None):
# 	db_session.remove()

@app.route('/')
def hello():
	return 'home'

@app.route('/callback', methods=['POST'])
def callback():
	signature = request.headers['X-Line-Signature']

	body = request.get_data(as_text=True)
	app.logger.info('Request body: ' + body)
	try:
		handler.handle(body, signature)
	except InvalidSignatureError:
		print('Invalid signature. Please check your channe access token/channel secret.')
		abort(400)
	return 'OK'

@handler.default()
def default(event):
	chat_scenario(line_bot_api, event)

if __name__ == '__application__':
	app.run()