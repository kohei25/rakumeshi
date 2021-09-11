import os

import click
from flask import Flask, send_from_directory
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)

    db_url = os.environ.get('DATABASE_URL')

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
    app.cli.add_command(init_db_command)

    from flaskr import linebot, liff
    
    app.register_blueprint(linebot.bp)
    app.register_blueprint(liff.bp)

    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

    return app

def init_db():
    db.drop_all()
    db.create_all()


@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")