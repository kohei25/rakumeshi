from linebot.models.messages import Message
from linebot.models.send_messages import LocationSendMessage
from linebot.models.template import (
    TemplateSendMessage, CarouselTemplate, CarouselColumn, ConfirmTemplate, ButtonsTemplate
)
from linebot.models.actions import (
    MessageAction, URIAction, PostbackAction
)

def carousel_columns(test_data):
    car_columns = []
    for v in test_data:
        p_data = 'name={}&address={}&lat={}&lng={}'.format(v['name'], v['address'], v['lat'], v['lng'])
        car_columns.append(
            CarouselColumn(
                thumbnail_image_url=v['photo']['pc']['l'],
                title=v['name'],
                text=v['genre']['catch'],
                actions=[
                    URIAction(
                        label='お店の詳細',
                        uri=v['urls']['pc']
                    ),
                    PostbackAction(
                        label='ここにする',
                        display_text='ここにする',
                        data=p_data
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
            ]
        )
    )

def button_tpl(buttons):
    return TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            # thumbnail_image_url='https://example.com/image.jpg',
            title='ラクメシです！',
            text='なにをしますか？',
            actions=buttons
        )
    )

def loc_tpl(title, address, lat, lng):
    return LocationSendMessage(
        title=title,
        address=address,
        latitude=lat,
        longitude=lng
    )

