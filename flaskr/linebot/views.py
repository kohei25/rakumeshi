from crypt import methods
import functools
from traceback import print_tb

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flaskr import db
from flaskr.linebot.models import User

from .line import Line

bp = Blueprint('linebot', __name__)

# LINE responce
line = Line(bp)
handler = line.handler

@bp.route('/add_user', methods=['POST'])
def add_user():
    lineid = request.form['lineid']
    user = User.query.filter_by(lineid=lineid).first()
    message = '' # 非同期通信のエラー対策
    if user is None:
        db.session.add(User(lineid=lineid))
        db.session.commit()
    return message

@bp.route('/callback', methods=['POST'])
def callback():
    line.callback()
    return 'OK'

@handler.default()
def default(event):
	line.scenario(event)
	return