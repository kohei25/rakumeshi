from .database import db_session
from .models import User, UserFeatures, ShopEvaluation

def add_user(line_id):
    n_user = User(line_id)
    db_session.add(n_user)
    db_session.commit()
    return

# def add_user_features(answer):
#     user_feature = UserFeatures(sex=answer['sex'], genre=answer['genre'], budget=answer['budget'])
#     db_session.add(user_feature)
#     db_session.commit()
#     return

# def add_shop_evaluation(shop_id, evaluation):
#     shop_evaluation = ShopEvaluation(shop_id=shop_id, evaluation=evaluation)
#     db_session.add(shop_evaluation)
#     db_session.commit()
#     return
