from .application.db
from datetime import datetime

class User(db.Model):
	__tablename__='users'
	id = db.Column(db.Integer, primary_key=True)
	line_id = db.Column(db.String, unique=True, nullable=False)
	created_data = db.Column(db.DateTime, nullabele=False, default=datetime.now(tz=datetime.timedelta(hours=9)))

	def __init__(self, line_id=None):
		self.line_id = line_id

class UserFeatures(db.Model):
	__tablename__='userfeatures'
	sex = db.Column(db.Integer)
	genre = db.Column(db.Integer)
	budget = db.Column(db.Integer)

	def __init__(self, sex, genre, budget):
		self.sex = sex
		self.genre = genre
		self.budget = budget

class ShopEvaluation(db.Model):
	__tablename__='shopevaluation'
	shop_id = db.Column(db.String)
	evaluation = db.Column(db.Integer) # 0 ~ 5

	def __init__(self, shop_id=None, evaluation=None):
		self.shop_id = shop_id
		self.evaluation = evaluation