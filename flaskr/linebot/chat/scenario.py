import re
from linebot.models.events import Postback
from linebot.models.messages import Message
from linebot.models.send_messages import TextSendMessage
from linebot.models.template import TemplateSendMessage, ButtonsTemplate
from requests.api import post
from .message_template import (
    carousel_columns, carousel_template_message, button_tpl, loc_tpl
)
from .message_content import (
    first_rep
)
from linebot.models.actions import (
    MessageAction, URIAction, PostbackAction
)
from flaskr.config import config

def chat_for_user_unregistrated(line_bot_api, event):
    url_preference = config.LIFFURL + '/register_preference'
    # url_for_biginner = config.LIFFURL_BIGINNER
    title = 'こんにちは，ラクメシです🤡'
    text = 'まずはあなたの好みを登録してください'
    buttons = [
        URIAction(
            label='好みを登録する',
            uri=url_preference
        ),
        # URIAction(
        #     label='使い方を見る',
        #     uri=url_for_biginner
        # )
    ]
    line_bot_api.reply_message(
        event.reply_token,
        button_tpl(title, text, buttons)
    )
    return

def chat_for_user_registrated(line_bot_api, event):
    url_keyword = config.LIFFURL + '/input_keyword'
    # url_for_biginner = config.LIFFURL_BIGINNER
    title = 'こんにちは，ラクメシです🤡'
    text = 'お店の検索の方法を選択してください'
    buttons = [
        URIAction(
            label='キーワードから検索する',
            uri=url_keyword
        ),
        # URIAction(
        #     label='現在地から検索する',
        #     uri=url_keyword
        # ),
        # URIAction(
        #     label='使い方を見る',
        #     uri=url_for_biginner
        # )
    ]
    print('keyword_url:', url_keyword)
    line_bot_api.reply_message(
        event.reply_token,
        button_tpl(title, text, buttons)
    )
    return

def chat_for_group(line_bot_api, event, count, group_id):
    url_event = config.LIFFURL + '/event/add/?group_id' + str(group_id) + '&count=' + count
    print(url_event)
    # url_for_biginner = config.LIFFURL_BIGINNER
    title = 'こんにちは，ラクメシです🤡'
    text = 'イベントを作成してください'
    buttons = [
        URIAction(
            label='イベントを作成する',
            uri=url_event
        ),
        # URIAction(
        #     label='使い方を見る',
        #     uri=url_for_biginner
        # )
    ]
    line_bot_api.reply_message(
        event.reply_token,
        button_tpl(title, text, buttons)
    )
    return

def send_invitation(line_bot_api, to, data):
    # FIXME: dataの抽出
    url_invitation = config.LIFFURL + f'invitation/?event_id={data}&date={data}&locatino={data}&style={data}'
    line_bot_api.push_message(
        to,
        URIAction(
            # FIXME: data -> style
            label=f'{data}の招待状',
            uri=url_invitation
        )
    )
    return

def send_reccomendated_restaurants(line_bot_api, to):
    line_bot_api.push_message(
        to,
        'text'
    )
    return

def request_rating_restaurant(line_bot_api, to, data):
    title = 'お店の評価をお願いします'
    text = '以降のレストランのレコメンドの際に用いられます'
    buttons= [
        PostbackAction(
            label='1 ｜ 悪くない　　',
            data='action=rating&rate=1'
        ),
        PostbackAction(
            label='2 ｜ よき　　　　',
            data='action=rating&rate=2'
        ),
        PostbackAction(
            label='3 ｜ おいしい　　',
            data='action=rating&rate=3'
        ),
        PostbackAction(
            label='4 ｜ 絶対またくる',
            data='action=rating&rate=4'
        ),
    ]
    line_bot_api.push_message(
        to,
        button_tpl(title, text, buttons)
    )
    return

def call_me(line_bot_api, event):
    first_rep(line_bot_api, event)
    return

def chat_scenario(line_bot_api, event):
    postback = event.postback.data
    if postback == 'location_search':
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text=''
            )
        )
        return
    elif 'lat' in postback:
        name = re.findall('name=(.*)&a',postback)[0]
        address = re.findall('address=(.*)&lat', postback)[0]
        lat = re.findall('lat=(.*)&', postback)[0]
        lng = re.findall('lng=(.*)', postback)[0]
        line_bot_api.reply_message(
            event.reply_token,
            loc_tpl(name, address, float(lat), float(lng))
        )
    return
