
from flask import Flask
from line import config
# DB module
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
# DB setting
app.config['SQLALCHEMY_DATABASE_URI'] = config.POSTGRESQL_DB_URI
db = SQLAlchemy(app)
migrate = Migrate(app)

import line.application