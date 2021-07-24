import pandas as pd
import numpy as np

from database import db_session
from models import User, UserFeatures, ShopEvaluation

def get_data():
    #get features data from SQL
    Base = declarative_base()
    Base.query = db_session.query_property()
    UF = UserFeatures
    data_user = db_session.query(UF.user_id, UF.sex, UF.genre, UF.budget).all()

    return data_user

def get_binary_vector(data):
    #convert data into binary vector through pandas dataframe
    dfm = pd.DataFrame(data)
    vector = pd.get_dummies(dfm).values
    
    return vector
