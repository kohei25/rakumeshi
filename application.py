from flask import Flask
from line.line import Line
from db.database import db_session, init_db # database
from config import config # environment variable

app = Flask(__name__)
init_db()

@app.teardown_appcontext
def shutdown_session(exception=None):
	db_session.remove()

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