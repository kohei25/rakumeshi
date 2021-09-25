from flask import Blueprint, jsonify, make_response, request, flash
from flask_cors import CORS
from .models import EventAttendance, Keyword, UserFeature, Event
from flaskr import db
from flaskr.linebot.models import User
from flaskr.linebot import line

bp = Blueprint('api', __name__, url_prefix='/api')
CORS(bp)

@bp.route('/check_user', methods=['POST'])
def check_user():
    json_data = request.get_json()
    line_id = json_data['userId']
    line.Line.check_user(line_id)
    return make_response(jsonify())

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
    user = line.Line.check_user(line_id)
    error = None

    if error is not None:
        flash(error)
    else:
        db.session.add(UserFeature(user_id=user.id, sex=int(preference['sex']), age=int(preference['age']), genre=int(preference['genre']), budget=int(preference['budget'])))
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
    keyword = json_data['keywords']['keyword']
    print(keyword)
    checkboxes = json_data['checkboxes']
    line_id = json_data['userId']
    user = line.Line.check_user(line_id)
    # restrants = reccomendated_restaurants()
    # push_message(line_id, 1, restrants)
    error = None

    if error is not None:
        flash(error)
    else:
        if keyword is not None:
            db.session.add(Keyword(user_id=user.id, keyword=keyword))
            db.session.commit()
    return make_response(jsonify())

def register_attend(event_id, user, attend):
    db.session.add(EventAttendance(event_id=event_id, user_id=user.id, attend=attend))
    db.session.commit() 
    return

def check_event_status(event_id):
    attendees = EventAttendance.query.filter_by(event_id=event_id).all()
    event = Event.query.filter_by(status=0).first()
    if event.count == len(attendees):
        event.staus = 1
        db.session.commit()
    return event

@bp.route('/event', methods=['POST'])
def event():
    json_data = request.get_json()
    status = 0
    count = json_data['count']
    group_id = json_data['groupId']
    date = json_data['date']
    location = json_data['location']
    line_id = json_data['userId']
    style = json_data['style']
    user = line.Line.check_user(line_id)
    error = None


    if error is not  None:
        flash(error)
    else:
        db.session.add(Event(host_user=user.id, group_id=group_id, date=date, status=status, count=count))
        db.session.commit()
        event = Event.query.filter_by(status=0).first()
        data = {
            'status': status,
            'invitation': {
                'event_id': event.id,
                'date': date,
                'location': location,
                'style': style
            }
        }
        line.push_message(group_id, data)
        register_attend(event.id, user, 0)
    return make_response(jsonify())

@bp.route('/attend', methods=['POST'])
def attend_event():
    json_data = request.get_json()
    event_id = json_data['eventId']
    attend = json_data['attend']
    line_id = json_data['userId']
    user = get_user(line_id)
    error = None

    if error is not None:
        flash(error)
    else:
        register_attend(event_id, user, attend)
        event = check_event_status(event_id)
        if event.status == 1:
            line.push_message(event.group_id, 1)
    return make_response(jsonify())

