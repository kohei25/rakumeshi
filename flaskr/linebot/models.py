from flaskr import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    line_id = db.Column(db.Text, unique=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp())

class SelectedRestaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey(User.id), nullable=False)
    # FIXME: use ForeignKey
    restaurant_id = db.Column(db.Integer, nullable=False)
    # 0: push送ってない, 評価してない 1: push送った, 評価してない 2: push送った, 評価した
    status = db.Column(db.Integer, nullable=False)
    push = db.Column(db.DateTime)
    selected_time = db.Column(db.DateTime, nullable=False)

class RatingRestaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey(User.id), nullable=False)
    # FIXME: use ForeignKey
    restaurant_id = db.Column(db.Integer, nullable=False)
    rate = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)