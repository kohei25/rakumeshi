from linebot.models import (
	TextMessage
)
from chat_template.message_tpl import (
	carousel_columns, carousel_template_message, confirm_tpl
)
from chat_template.test_data import (
	test_data
)

def chat_scenario(line_bot_api, event, text):
	if text == 'ラクメシ' or text == '最初から選択しなおす':
		c_tpl = confirm_tpl()
		line_bot_api.reply_message(
			event.reply_token,
			c_tpl
		)
	elif text == '"ラク飯"のおすすめを表示する':
		t_data = test_data()
		tmp = carousel_columns(t_data)
		tmp_carousel = carousel_template_message(tmp)
		line_bot_api.reply_message(
			event.reply_token,
			tmp_carousel
		)

	return
