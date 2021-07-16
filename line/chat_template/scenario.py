import re
from linebot.models.events import Postback
from linebot.models.messages import Message
from linebot.models.send_messages import TextSendMessage
from requests.api import post
from .message_tpl import (
    carousel_columns, carousel_template_message, confirm_tpl, button_tpl, loc_tpl
)
from linebot.models.actions import (
    PostbackAction
)

from .test_data import (
    test_data
)
# from db.user_func import add_user
# from db.models import User

def chat_scenario(line_bot_api, event):
    # userのidを取得
    # line_id = event.source.user_id
    # user = User.query.filter_by(line_id=line_id).first()
    # if user == None:
    #     add_user(line_id)
    # user_id = User.query.filter_by(line_id=line_id).first().id
    e_type = event.type
    if e_type == 'message':
        text = event.message.text
        if text == 'ラクメシ':
            buttons = [
            PostbackAction(
                label='お店を探す',
                display_text='お店を探す',
                data='search'
            ),
            PostbackAction(
                label='好みを登録する',
                display_text='好みを登録する',
                data='kregiste_feature'
            )]
            line_bot_api.reply_message(
                event.reply_token,
                button_tpl(buttons)
            )
        elif text == '渋谷' or text == '新宿':
            t_data = test_data(text)
            line_bot_api.reply_message(
                event.reply_token,
                carousel_template_message(carousel_columns(t_data))
            )
    elif e_type == 'postback':
        postback = event.postback.data
        if postback == 'search':
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='キーワードを入力してね！ 例：渋谷、ランチ')
            )
        elif postback == 'registe_feature':
            line_bot_api.reply_message(
                event.reply_token,
            )
        elif 'lat' in postback:
            # print(postback)
            # name={}&address{}&lat={}&lng={}
            name = re.findall('name=(.*)&a',postback)[0]
            address = re.findall('address=(.*)&lat', postback)[0]
            lat = re.findall('lat=(.*)&', postback)[0]
            lng = re.findall('lng=(.*)', postback)[0]
            line_bot_api.reply_message(
                event.reply_token,
                loc_tpl(name, address, float(lat), float(lng))
            )
    return
