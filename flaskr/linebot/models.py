from flaskr import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lineid = db.Column(db.String, unique=True, nullable=False)
    # created_at = db.Column(db.Integer)