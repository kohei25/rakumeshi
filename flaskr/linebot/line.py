from flask import request, abort
from linebot.exceptions import (
	InvalidSignatureError
)
from linebot import (
	LineBotApi, WebhookHandler
)
from .chat.scenario import chat_scenario
from flaskr.config import config

class Line(object):
    def __init__(self, app):
        self.app = app
        self.line_bot_api = LineBotApi(config.LINE_CHANNEL_ACCESS_TOKEN)
        self.handler = WebhookHandler(config.LINE_CHANNEL_SECRET)
    
    def callback(self):
        signature = request.headers['X-Line-Signature']
        body = request.get_data(as_text=True)
        # self.app.logger.info('Request body: ' + body)
        try:
            self.handler.handle(body, signature)
        except InvalidSignatureError:
            print('Invalid signature. Please check your channe access token/channel secret.')
            abort(400)
        return

    def scenario(self, event):
        chat_scenario(self.line_bot_api, event)
        return
    
    