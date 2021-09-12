CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    line_id TEXT NOT NULL UNIQUE,
    created_at INTEGER
);
CREATE TABLE user_features (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    sex INTEGER,
    age INTEGER,
    genre INTEGER,
    budget INTEGER,
    created_at INTEGER NOT NULL,
    updated_at INTEGER NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id)
);
CREATE TABLE shop_evaluation(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    restraunt_id INTEGER,
    rating INTEGER,
    created_at INTEGER NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(restraunt_id) REFERENCES restraunts(id)
);