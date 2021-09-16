import re
from linebot.models.events import Postback
from linebot.models.messages import Message
from linebot.models.send_messages import TextSendMessage
from requests.api import post
from .message_template import (
    carousel_columns, carousel_template_message, confirm_tpl, button_tpl, loc_tpl
)
from .message_content import (
    first_rep
)
from linebot.models.actions import (
    PostbackAction
)

# from .test_data import (
#     test_data
# )

def chat_scenario(line_bot_api, event):
    e_type = event.type
    print(event)
    if e_type == 'message':
        text = event.message.text
        if text == 'ラクメシ':
            first_rep(line_bot_api, event)
    elif e_type == 'postback':
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
