from concurrent.futures import thread
import os
import threading
import time

from flask import Flask, render_template, send_from_directory
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import true

db = SQLAlchemy()

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)

    from flaskr.config import config
    db_url = config.DATABASE_URL

    if db_url is None:
        db_path = os.path.join(app.instance_path, 'flaskr.sqlite')
        db_url = f'sqlite:///{db_path}'
        os.makedirs(app.instance_path, exist_ok=True)
    
    app.config.from_mapping(
        SQLALCHEMY_DATABASE_URI=db_url,
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    db.init_app(app)
    # app.cli.add_command(init_db_command)

    from flaskr import linebot, api
    
    app.register_blueprint(linebot.bp)
    app.register_blueprint(api.bp)

    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

    @app.route('/admin/init-db')
    def init_db():
        init_db_command()
        return render_template('admin.html', text='Initialized the database')
    
    @app.route('/admin/start-monitor-db')
    def start_monitor_db():
        from flaskr.linebot.line import Line
        monitor = threading.Thread(target=Line.monitor_db)
        monitor.start()
        return render_template('admin.html', text='start monitoring db')

    return app

def init_db_command():
    """Clear existing data and create new tables."""
    if db:
        db.drop_all()
    db.create_all()
    print('Initialized the database.')
    # click.echo("Initialized the database.")