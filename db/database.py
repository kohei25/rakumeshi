from sqlalchemy import create_engine, engine
from sqlalchemy.orm import base, scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import config

engine = create_engine(config.POSTGRESQL_DB_URI)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import db.models
    Base.metadata.create_all(bind=engine)