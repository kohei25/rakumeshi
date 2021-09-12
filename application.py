from flask import Flask, g
from line.line import Line
from db.sqlite import Sqlite
import sqlite3


app = Flask(__name__)
sqlite = Sqlite(g, app)
sqlite.init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# sever active check
@app.route('/')
def hello():
    return 'home'

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