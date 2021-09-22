from asyncio.proactor_events import constants
from flask import Blueprint, jsonify, make_response, request, flash
from flask_cors import CORS
from .models import Keyword, UserFeature
from flaskr import db
from flaskr.linebot.models import User

bp = Blueprint('api', __name__, url_prefix='/api')
CORS(bp)


def get_user(lineid):
    user = User.query.filter_by(lineid=lineid).first()
    return user

@bp.route('/check_user', methods=['POST'])
def check_user():
    json_data = request.get_json()
    line_id = json_data['userId']
    user = User.query.filter_by(lineid=line_id).first()
    responce = {'status': 'Registered'}
    if user is None:
        db.session.add(User(lineid=line_id))
        db.session.commit()
        responce['status'] = 'newRegistered'
    print(responce)
    return make_response(jsonify(responce))

@bp.route('/register_preference', methods=['POST'])
def register_preference():
    '''
    json_data:
        preference: {
            sex: number,
            age: number,
            genre: number,
            budget: number
        }
        line_id: string
    '''
    json_data = request.get_json()
    preference = json_data['preference']
    line_id = json_data['userId']
    user = get_user(line_id)
    error = None

    if error is not None:
        flash(error)
    else:
        db.session.add(UserFeature(sex=int(preference['sex']), age=int(preference['age']), genre=int(preference['genre']), budget=int(preference['budget']), user=user))
        db.session.commit()
    return make_response(jsonify())

@bp.route('/input_keyword', methods=['POST'])
def input_keyword():
    '''
    json_data: (details ref. app/components/liff/type.ts)
        keywords: {
            'min_budget': number,
            'max_budget': number,
            'keyword': string(ex. '焼肉, 渋谷')
        }
        checkboxes: {
            style: boolean['free_drink', 'free_food', 'cource', 'lunch']
            seat: boolean['private_room', 'tatami', 'terrace']
            alchool: boolean['shochu', 'sake', 'wine', 'cocktail', 'sommelier']
            facility: boolean['wifi', 'parking']

            (ex. style: [false, false, false, true])
        }
    '''
    json_data = request.get_json()
    print('json_data', json_data)
    keywords = json_data['keywords']
    checkboxes = json_data['checkboxes']
    line_id = json_data['userId']
    user = get_user(line_id)
    error = None

    if error is not None:
        flash(error)
    else:
        db.session.add(Keyword(sex=int(keyword=keywords['keyword'], user=user)))
        db.session.commit()
    return make_response(jsonify())