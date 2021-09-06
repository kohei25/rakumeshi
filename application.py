from crypt import methods
from os import abort
from flask import Flask, g, render_template, request
from line.line import Line
from db.sqlite import Sqlite
import sqlite3


app = Flask(__name__)
# sqlite = Sqlite(g, app)
# sqlite.init_db()

# @app.teardown_appcontext
# def close_connection(exception):
#     db = getattr(g, '_database', None)
#     if db is not None:
#         db.close()

# sever active check
@app.route('/')
def hello():
    return render_template('hello.html') 

@app.route('/input_keyword', methods=['GET', 'POST'])
def input_keyword():
    '''
    GET:
        user input keyword
    POST:
        user's keyword
    '''
    try:
        if request.method == 'GET':
            return render_template('input_keyword.html')
        elif request.method == 'POST': 
            return render_template('thankyou.html')
        else:
            return abort(400)
    except Exception as e:
        return str(e)

@app.route('/register_favorite', methods=['GET', 'POST'])
def register_favorite():
    '''
    GET:
        user register favorite in page
    POST:
        user's favorite to DB
    '''
    try:
        if request.method == 'GET':
            return render_template('register_favorite.html')
        elif request.method == 'POST': 
            return render_template('thankyou.html')
        else:
            return abort(400)
    except Exception as e:
        return str(e)

# LINE responce
line = Line(app)
handler = line.handler

@app.route('/callback', methods=['POST'])
def callback():
    line.callback()
    return 'OK'

@handler.default()
def default(event):
	line.scenario(event)
	return

if __name__ == '__application__':
    app.run()