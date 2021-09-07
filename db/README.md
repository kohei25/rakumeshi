## test dataの作成方法
- restaurants.csvをダウンロードし，rakumeshi/dbに配置する
- rakumeshi/db　に移動
- test_data.pyの各パラメータ(restaurant_num, user_num, evaluation_num)を適当な値に設定する
- ```python test_data.py```を実行
- [DBeaver](https://dbeaver.io)にてデータを確認するには，Dbeaverにて　Database > New Database connection > SQLite > Main > Browseにてrakumeshi.dbを選択
- DBeaverのDatabase Navigatorにてrakumeshi.db > TablesにてTable(restaurants,, shop_evaluation, user_features, users)を選択しDataにてデータを確認
- dbからのデータを取ってくる．table_nameにてtable名をにゅうりょくする
```
import sqlite3

con = sqlite3.connect('../rakumeshi.db')
cur = con.cursor()
table_name = 'users'
query = f'SELECT * FROM {table_name}'
data = cur.execute(query).fetchall()
```

- test dataを作り直したい場合は再び```python test_data.py```を実行
- DBeaverにては,Database > DisconnectしてからDatabase > Invalidate/Reconnect する


# sqlite3
## user
| id          	| line_id 	| created_at         	|
|-------------	|---------	|--------------------	|
| [PK]integer 	| text    	| integer(unix time) 	|

## user_feature
| id          	| user_id     	| sex     	| age     	| genre   	| budget  	| created_at    	| updated_at    	|
|-------------	|-------------	|---------	|---------	|---------	|---------	|---------------	|---------------	|
| [PK]integer 	| [FK]integer 	| integer 	| integer 	| integer 	| integer 	| integer(unix) 	| integer(unix) 	|

sex...0: 男，1:女, 2:その他  
age...[下記](#age)を参考, 1-6  
genre...[下記](#genre)を参考, 1-7  
butget...[下記](#budget)を参考, 1-3
下記に追記

## shop_evaluation
| id          	| user_id     	| shop_id     	| rating      	| created_at         	|
|-------------	|-------------	|-------------	|------------	|--------------------	|
| [PK]integer 	| [FK]integer 	| [FK]integer 	| integer    	| integer(unix time) 	|

### age
| integer | age      |
| ------- | -------- |
| 1       | 10代     |
| 2       | 20代     |
| 3       | 30代     |
| 4       | 40代     |
| 5       | 50代     |
| 6       | 60代以上 |

### genre
| integer | genre                |
| ------- | -------------------- |
| 1       | 和食                 |
| 2       | 中華                 |
| 3       | フレンチ・イタリアン |
| 4       | アジア・エスニック   |
| 5       | ロシア               |
| 6       | 洋食                 |
| 7       | その他               |

### budget
| integer | budget                    |
| ------- | ------------------------- |
| 1       | 安さ重視　（~ 2000）      |
| 2       | コスパ重視（2000 ~ 5000） |
| 3       | 味重視　　（5000 ~ ）     |