
# postgreSQL
## user
| id          | line_id | created_at |
|-------------|---------|------------|
| [PK]integer | text    | timestamp  |

## user_feature
| id          | user_id  | sex     | genre   | budget  | created_at | update_at |
|-------------|----------|---------|---------|---------|------------|-----------|
| [PK]integer | [FK]text | integer | integer | integer | timestamp  | timestamp |

sex...0: 男，1:女, 2:その他
genre...hotpepper apiに準拠
butget...hotpepper apiに準拠


## shop_evaluation
| id          | user_id     | shop_id     | evaluation | created_at |
|-------------|-------------|-------------|------------|------------|
| [PK]integer | [FK]integer | [FK]integer | integer    | timestamp  |