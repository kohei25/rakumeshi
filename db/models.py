from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import user
from .database import Base

class User(Base):
	__tablename__='user'
	id = Column(Integer, primary_key=True)
	line_id = Column(String, unique=True, nullable=False)
	created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
	user_features = relationship('UserFeatures')
	shop_evaluations = relationship('ShopEvaluation')

	def __init__(self, line_id=None):
		self.line_id = line_id

class UserFeatures(Base):
	__tablename__='userfeatures'
	id = Column(Integer, primary_key=True)
	user_id = Column(Integer, ForeignKey('user.id'))
	sex = Column(Integer) # 0: man, 1: woman, 2: other
	genre = Column(Integer)
	budget = Column(Integer)
	created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
	update_at = Column(DateTime, nullable=False, default=datetime.utcnow)

	def __init__(self, sex, genre, budget):
		self.sex = sex
		self.genre = genre
		self.budget = budget

class ShopEvaluation(Base):
	__tablename__='shopevaluation'
	id = Column(Integer, primary_key=True)
	user_id = Column(Integer, ForeignKey('user.id'))
	shop_id = Column(String, nullable=False)
	evaluation = Column(Integer) # 0 ~ 5

	def __init__(self, shop_id=None, evaluation=None):
		self.shop_id = shop_id
		self.evaluation = evaluation