import os
from flask import Flask, request, abort

from chat_template.scenario import (
	chat_scenario
)

from linebot import (
	LineBotApi, WebhookHandler
)
from linebot.exceptions import (
	InvalidSignatureError
)

from linebot.models import (
	MessageEvent, TextMessage, TextSendMessage
)

import config

app = Flask(__name__)

line_bot_api = LineBotApi(config.LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(config.LINE_CHANNEL_SECRET)

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

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
	text = event.message.text
	chat_scenario(line_bot_api, event, text)

if __name__ == '__main__':
	app.run()

