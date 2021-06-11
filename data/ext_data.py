import json
import requests
import pandas as pd
import urllib.parse
# config.py
import config

api_key = config.HOTPEPPER_API_KEY

i_start = 1
restaurant_datas=[]

while True:
	query = {
		'key': api_key,
		'large_area': 'Z011', # 東京
		'order': 1,
		'start': i_start,
		'count': 100,
		'format': 'json'
	}
	url_base = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'
	responce = requests.get(url_base, query)
	result = json.loads(responce.text)['results']['shop']
	if len(result) == 0:
		break
	for restaurant in result:
		restaurant_datas.append([restaurant['name'], restaurant['address'], restaurant['budget']['code'], restaurant['genre']['code']])
	i_start += 100
	print(i_start)

columns = ['name', 'address', 'budget', 'genre']
df_restaurants = pd.DataFrame(restaurant_datas, columns=columns)
df_restaurants.to_csv('restaurants_tokyo.csv')