import re
from linebot.models.actions import (
    MessageAction, URIAction, PostbackAction
)
from linebot.models.send_messages import StickerSendMessage
from requests.models import ReadTimeoutError

from .message_tpl import (
    button_tpl
)

def first_rep(line_bot_api, event):
    title = 'こんにちは，ラクメシです🤡'
    text = 'なにをしますか？'
    buttons = [
        URIAction(
            label='キーワードからお店を探す',
            uri='https://liff.line.me/1656378583-Ke1mWeD9'
        ),
        PostbackAction(
            label='現在地からお店を探す',
            data='location_search'
        ),
        URIAction(
            label='好みを登録する',
            uri='https://liff.line.me/1656378583-rLZqp0ma'
        )
    ]
    line_bot_api.reply_message(
        event.reply_token,
        button_tpl(title, text, buttons)
    )
    return

def rate_rep(line_bot_api, event):
    '''
    function: 30分後にお店の評価を促すラインを送る
    input => line_bot_api, event
    output => ボタンテンプレート
    '''
    return

# ***************
# 現在地からお店を探す
# ***************
class LocationSearch(object):
    def __init__(self, line_bot_api, event):
        self.line_bot_api = line_bot_api
        self.event = event
    
    # def first_rep(self):