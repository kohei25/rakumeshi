import requests
import json

from config import config

api_key = config.HOTPEPPER_API_KEY

def test_data(keyword):
	query = {
		'key': api_key,
		'large_area': 'Z011',  # 東京
		'order': 4,  # 名前の順
		'keyword': keyword,
		'start': 1,  # 検索結果の何番目から出力するか
		'count': 3,  # 最大取得件数
		'format': 'json'
	}
	url_base = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'
	responce = requests.get(url_base, query)
	result = json.loads(responce.text)['results']['shop']
	# print(result)
	return result