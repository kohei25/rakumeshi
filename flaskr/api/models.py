from ast import keyword
from flaskr import db
from flaskr.linebot.models import User

class UserFeature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey(User.id), nullable=False)
    sex = db.Column(db.Integer)
    age = db.Column(db.Integer)
    genre = db.Column(db.Integer)
    budget = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp())

class Keyword(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey(User.id), nullable=False)
    keyword = db.Column(db.Text)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp())

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    host_user = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    group_id = db.Column(db.Text, nullable=False)
    date = db.Column(db.Text, nullable=False) # YY-MM-DD-曜日
    status = db.Column(db.Integer, nullable=False) # 0: event open, 1: event close
    attendees = db.relationship('EventAttendance', backref='event', lazy=True)
    count = db.Column(db.Integer, nullable=False) # groupのメンバー数
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp())

class EventAttendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    # 0: 出席, 1: 欠席
    attend = db.Column(db.Integer, nullable=False) 