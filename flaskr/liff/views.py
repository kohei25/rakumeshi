from ast import keyword
from copy import error
from crypt import methods
import functools
from traceback import print_tb

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flaskr import db
from flaskr.linebot.models import User
from .models import UserFeature, Keyword

bp = Blueprint('liff', __name__)

def get_user(lineid):
    user = User.query.filter_by(lineid=lineid).first()
    return user

@bp.route('/')
def home():
    return render_template('index.html')
    # return render_template('thankyou.html')

@bp.route('/liff_index')
def liff_index():
    return render_template('liff.html')

@bp.route('/register_favorite', methods=('GET', 'POST'))
def register_features():
    if request.method == 'POST':
        sex = request.form['sex']
        age = request.form['age']
        genre = request.form['genre']
        budget= request.form['budget']
        line_id = request.form['userid']
        user = get_user(line_id)
        error = None

        if error is not None:
            flash(error)
        else:
            db.session.add(UserFeature(sex=int(sex), age=int(age), genre=int(genre), budget=int(budget), user=user))
            db.session.commit()
            return render_template('thankyou.html')
    
    return render_template('register_favorite.html')

@bp.route('/input_keyword', methods=('GET', 'POST'))
def register_keyword():
    if request.method == 'POST':
        keywords = request.form['keyword']
        line_id = request.form['userid']
        styles = request.form.getlist('style')
        seats = request.form.getlist('seat')
        alchools = request.form.getlist('alchool')
        facilities = request.form.getlist('facility')
        '''
        recommendation function
        input -> styles(list), seats(list), alchools(list), facilities(list), keyword(free keyword)
        output -> three restaurants data(dict)
        '''
        user = get_user(line_id)
        error = None
        if error is not None:
            flash(error)
        else:
            db.session.add(Keyword(keyword=keywords, user=user))
            db.session.commit()
            return render_template('thankyou.html')
    
    return render_template('input_keyword.html')