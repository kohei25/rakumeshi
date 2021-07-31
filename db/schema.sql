CREATE TABLE restraunts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    restraunts_name TEXT NOT NULL
);
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    line_id TEXT NOT NULL UNIQUE,
    created_at INTEGER
);
CREATE TABLE uer_features (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    sex INTEGER,
    genre INTEGER,
    budget INTEGER,
    created_at INTEGER NOT NULL,
    update_at INTEGER NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id)
);
CREATE TABLE shop_evaluation(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    evaluation INTEGER,
    created_at INTEGER NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id)
);