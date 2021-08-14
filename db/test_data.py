from faker import Faker
from faker.providers import bank
import sqlite3
import os

restaurant_num = 20 # レストランの数
user_num = 1000 # ユーザーの数
evaluation_num = 100 # 評価の数

path = '../rakumeshi.db'
if os.path.exists(path):
    os.remove(path)
    print('200')
else:
    print('200')

con = sqlite3.connect('../rakumeshi.db')
cur = con.cursor()

with open('./schema.sql', 'r') as f:
    cur.executescript(f.read())

fake = Faker()
fake.add_provider(bank)


import pandas as pd
from datetime import datetime

columns = ['line_id', 'created_at']
df = pd.DataFrame(columns=columns)

for _ in range(1, user_num):
    dt = int(datetime.now().timestamp())
    l_id = fake.swift11()
    d = [ l_id, dt ]
    df_c = pd.DataFrame([d], columns=columns)
    df = df.append(df_c, ignore_index=True)


df.to_sql(name='users', con=con, if_exists='append', index=False)


from random import randrange, uniform
import datetime


for i in range(1, user_num):
    id = i
    sex = randrange(3)
    age = int(uniform(1, 6))
    genre = int(uniform(1, 7))
    budget = int(uniform(1, 3))
    created_at = int(datetime.datetime.now().timestamp())
    updated_at = int(datetime.datetime.now().timestamp())
    query = 'INSERT INTO user_features(user_id, sex, age, genre, budget, created_at, updated_at) VALUES ((SELECT id FROM users WHERE id = ?), ?, ?, ?, ?, ?, ?)'
    args = [id, sex, age, genre, budget, created_at, updated_at]
    cur.execute(query, args)
    con.commit()


df_r = pd.read_csv('./restaurants.csv')
df_r = df_r[:restaurant_num]
df_r = df_r.drop(['id'], axis=1)
df_r.insert(0, 'id', range(0, len(df_r)))
df_r.to_sql(name='restaurants', con=con, if_exists='append', index=False)


for i in range(0, evaluation_num):
    user_id = randrange(user_num - 1)
    restraunt_id = randrange(restaurant_num)
    evaluation = randrange(6)
    created_at = int(datetime.datetime.now().timestamp())
    query = 'INSERT INTO shop_evaluation(user_id, restraunt_id, rating, created_at) VALUES ((SELECT id FROM users WHERE id = ?), (SELECT id FROM restaurants WHERE id = ?), ?, ?)'
    args = [user_id, restraunt_id, evaluation, created_at]
    cur.execute(query, args)
    con.commit()
con.close()

print('create test_data')
