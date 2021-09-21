from flask import Blueprint, jsonify, make_response, request, flash
from flask_cors import CORS
from .models import UserFeature
from flaskr import db

bp = Blueprint('api', __name__, url_prefix='/api')
CORS(bp)

@bp.route('/register_preference', methods=['POST'])
def register_preference():
    json_data = request.get_json()
    preference = json_data['preference']
    line_id = json_data['userId']
    print(line_id)
    print(preference['sex'])
    # user = get_user(line_id)
    error = None

    if error is not None:
        flash(error)
    # else:
        # db.session.add(UserFeature(sex=int(preference['sex']), age=int(preference['age']), genre=int(preference['genre']), budget=int(preference['budget']), user=user))
        # db.session.commit()
    return make_response(jsonify())

@bp.route('/input_keyword', methods=['POST'])
def input_keyword():
    json_data = request.get_json()
    keywords = json_data['keywords']
    checkboxes = json_data['checkboxes']
    print(keywords)
    print(checkboxes)
    # user = get_user(line_id)
    error = None

    if error is not None:
        flash(error)
    # else:
        # db.session.add(UserFeature(sex=int(preference['sex']), age=int(preference['age']), genre=int(preference['genre']), budget=int(preference['budget']), user=user))
        # db.session.commit()
    return make_response(jsonify())