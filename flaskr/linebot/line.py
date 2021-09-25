from datetime import datetime
import numbers
import re
import time
from flaskr.api.models import UserFeature
from flask import request, abort
from linebot.exceptions import (
	InvalidSignatureError
)
from linebot import (
	LineBotApi, WebhookHandler
)
from .chat.scenario import (
    chat_for_group, chat_for_user_registrated, chat_for_user_unregistrated, chat_scenario, call_me, request_rating_restaurant, send_invitation, send_reccomendated_restaurants
)
from .models import RatingRestaurant, SelectedRestaurant, User
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
        '''
        - userの状況（好み登録済みかどうか）
        - 呼び出し場所（user or group）
        によってシナリオを変える
        '''
        print(event)
        e_source = event.source
        e_type = event.type
        if e_type == 'message':
            if event.message.text == "ラクメシ":
                e_source_type = e_source.type
                line_id = e_source.user_id
                print('e_source_type:', e_source_type, 'user_id:', line_id)
                # todo : e_source_typeがgroupとuserでレスポンスをかえる
                if e_source_type == 'group':
                    group_id = e_source.group_id
                    count = self.get_group_count(group_id)
                    chat_for_group(self.line_bot_api, event,  count, group_id)
                elif e_source_type == 'user':
                    checked = self.check_registrated_preference(line_id)
                    print(checked)
                    if checked:
                        # 好みを登録済み
                        chat_for_user_registrated(self.line_bot_api, event)
                    else:
                        # 好みを未登録
                        chat_for_user_unregistrated(self.line_bot_api, event)
            # FIXME: トリガーを変更する
            elif event.message.text == "評価":
                data = {
                    
                }
                request_rating_restaurant(self.line_bot_api, event.source.user_id, data)
        elif e_type == 'postback':
            e_postback = event.postback
            data = e_postback.data
            m = re.match(r'action=([a-z]+)&([a-zA-Z0-9=]+)', data).groups()
            action = m[0]
            if action == 'rating':
                user = self.check_user(e_source.user_id)
                rate = re.match(r'rate=([0-9])', m[1]).groups()[0]
                print(f'rate: {rate}')
                created_at = datetime.now()
                # FIXME: restaurant idのデータを取得する
                db.session.add(RatingRestaurant(user_id= user.id, restaurant_id=1 , rate=rate, created_at=created_at))
                db.session.commit()
                # TODO: update selectedRestaurant status
                # TODO: rating thank you message
        return

    def push_message(self, to, data):
        '''
        to: userId, groupId
        status | 0: event create -> send invitaton, 1: close event -> recommend restaurant
        '''
        if data['status'] == 0:
            send_invitation(self.line_bot_api, to, data['invitation'])
        elif data['status'] == 1:
            send_reccomendated_restaurants(self.line_bot_api, to)
        return

    def get_group_users(self, group_id):
        '''
        only use for official account and premium account
        so you use unofficial account, you don't use this function
        '''
        member_ids = self.line_bot_api.get_group_member_ids(group_id)
        return member_ids

    def get_group_count(self, group_id):
        count = self.line_bot_api.get_group_members_count(group_id)
        return count
    
    def check_user(self, line_id):
        user = User.query.filter_by(line_id=line_id).first()
        if user is None:
            db.session.add(User(line_id=line_id))
            db.session.commit()
            user = User.query.filter_by(line_id=line_id).first()
        return user
    
    def check_registrated_preference(self, line_id):
        status = False
        user = User.query.filter_by(line_id=line_id).first()
        if user is None:
            return status
        checked = UserFeature.query.filter_by(user_id=user.id)
        if checked is not None:
            status = True
        return status
    
    def monitor_db(self):
        while(True):
            # FIXME: arrange interval time production 60*60 (s)
            interval = 10
            time.sleep(interval)
            request_rating_users = SelectedRestaurant.query.filter_by(status=0).all()
            for user in request_rating_users:
                request_rating_restaurant(self.line_bot_api, user.line_id, )

            # TODO: push request rating message
            print('hi')
        return