from linebot.models.template import (
	TemplateSendMessage, CarouselTemplate, CarouselColumn, ConfirmTemplate
)
from linebot.models.actions import (
	MessageAction, URIAction, PostbackAction
)

def carousel_columns(test_data):
	car_columns = []
	for v in test_data:
		car_columns.append(
			CarouselColumn(
				thumbnail_image_url=v['photo']['pc']['l'],
				title=v['name'],
				text=v['genre']['catch'],
				actions=[
					# lat, lngからgoogle mapsで表示する
					# URIAction(
					# 	label='地図を表示する',
					# 	# uri=v[]
					# ),
					URIAction(
						label='お店の詳細',
						uri=v['urls']['pc']
					)
				]
			)
		)
	return car_columns

def carousel_template_message(carousel_columns):
	return TemplateSendMessage(
		alt_text='Carousel template',
		template=CarouselTemplate(columns=carousel_columns)
	)

def confirm_tpl():
	return TemplateSendMessage(
		alt_text='Confirm template',
		template=ConfirmTemplate(
			text='"ラク飯"のおすすめを表示する？',
			actions=[
				MessageAction(
					label='✅はい',
					text='"ラク飯"のおすすめを表示する'
				),
				MessageAction(
					label='❌いいえ',
					text='最初から選択しなおす',
				)
				# PostbackAction(
				# 	label='❌いいえ',
				# 	display_text='最初から選択しなおす',
				# 	data='action=reccomend'
				# )
			]
		)
	)



