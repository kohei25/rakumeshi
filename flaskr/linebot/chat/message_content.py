import re
from linebot.models.actions import (
    MessageAction, URIAction, PostbackAction
)
from linebot.models.send_messages import StickerSendMessage

from .message_template import (
    button_tpl
)
from flaskr.config import config
# from flaskr.linebot.views import get_group_users

def first_rep(line_bot_api, event):
    url_starter = config.LIFFURL_STARTER
    url_keyword = config.LIFFURL_KEYWORD
    url_favorite = config.LIFFURL_FAVORITE
    title = 'こんにちは，ラクメシです🤡'
    text = 'なにをしますか？'
    buttons = [
        URIAction(
            label='キーワードからお店を探す',
            uri=url_keyword
        ),
        PostbackAction(
            label='現在地からお店を探す',
            data='location_search'
        ),
        URIAction(
            label='好みを登録する',
            uri=url_favorite
        ),
        URIAction(
            label='テスト',
            uri=url_starter
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