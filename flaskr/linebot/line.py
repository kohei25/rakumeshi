from flask import request, abort
from linebot.exceptions import (
	InvalidSignatureError
)
from linebot import (
	LineBotApi, WebhookHandler
)
from .chat.scenario import (
    chat_scenario, call_me
)
from .models import User
from flaskr.config import config
from flaskr import db

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
        if event.message.text =="ラクメシ":
            e_source = event.source
            e_source_type = e_source.type
            # todo : e_source_typeがgroupとuserでレスポンスをかえる
            call_me(self.line_bot_api, event)
        elif event.type == 'postback':
            chat_scenario(self.line_bot_api, event)
        return

    def get_group_users(self, group_id):
        '''
        only use for official account and premium account
        so you use unofficial account, you don't use this function
        '''
        member_ids = self.line_bot_api.get_group_member_ids(group_id)
        return member_ids
    
    def add_user(self, lineid):
        user = User.query.filter_by(lineid=lineid).first()
        print('add user')
        if user is None:
            db.session.add(User(lineid=lineid))
            db.session.commit()
        return