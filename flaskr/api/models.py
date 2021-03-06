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

    user = db.relationship(User, lazy='joined', backref='userfeatures')

class Keyword(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey(User.id), nullable=False)
    keyword = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp())

    user = db.relationship(User, lazy='joined', backref='keywords')