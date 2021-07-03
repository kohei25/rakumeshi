import requests
import json
import sys

sys.path.append('../')

from .. import config

api_key = config.HOTPEPPER_API_KEY

def test_data():
	query = {
		'key': api_key,
		'large_area': 'Z011',  # 東京
		'order': 1,  # 名前の順
		'start': 1,  # 検索結果の何番目から出力するか
		'count': 3,  # 最大取得件数
		'format': 'json'
	}
	url_base = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'
	responce = requests.get(url_base, query)
	result = json.loads(responce.text)['results']['shop']
	# print(result)
	return result