import sqlite3

DATABASE = './rakumeshi.db'

class Sqlite(object):
    def __init__(self, g, app):
        self.g = g
        self.database = DATABASE
        self.app = app
    
    @property
    def db(self):
        db = getattr(self.g, '_database', None)
        if db is None:
            db = self.g._database = sqlite3.connect(self.database)
        return db

    def init_db(self):
        with self.app.app_context():
            with self.app.open_resource('./db/schema.sql', mode='r') as f:
                self.db.cursor().executescript(f.read())
            self.db.commit()
        return 'init db'

    def query_db(self, query, args=(), one=False):
        cur = self.db.execute(query, args)
        rv = cur.fetchall()
        cur.close()
        return (rv[0] if rv else None) if one else rv

    def add_test_data(self):
        return
