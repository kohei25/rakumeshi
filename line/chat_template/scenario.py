from linebot.models import (
	TextMessage
)
from .message_tpl import (
	carousel_columns, carousel_template_message, confirm_tpl
)
from .test_data import (
	test_data
)

from line.models import User
from line.application import db

def add_user(line_id):
	user = User.query.filter_by(line_id=line_id)
	if user is None:
		n_user = User(line_id)
		db.session.add(n_user)
		db.session.commit()
	return

def chat_scenario(line_bot_api, event, text):
	if text == 'ラクメシ' or text == '最初から選択しなおす':
		c_tpl = confirm_tpl()
		line_id = event.source.user_id
		add_user(line_id)
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
