import xml.etree.ElementTree as ET
import requests
import re
import pandas as pd
# config.py
import config

def get_responce(large_service_area, start, count):
	url_base = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'
	api_key = config.HOTPEPPER_API_KEY
	query = {
		'key': api_key,
		'large_service_area': large_service_area,
		'order': 1, # 名前の順
		'start': start, # 検索結果の何番目から出力するか
		'count': count, # 最大取得件数
	}
	responce = requests.get(url_base, query)
	return responce

def parse_xml(root, dic, name=''):
    for child in root:
        if name == '':
            name_child = name + child.tag
        else:
            name_child = name + '>' + child.tag
        if len(child) == 0:
            dic[name_child] = child.text
        else:
            parse_xml(child, dic, name_child)

def xml_to_dataframe(content):
	xml_string = re.sub(rb' xmlns=".*?"', b'', content, count=1)
	root = ET.fromstring(xml_string)
	list_dic = []
	for shop in root.findall('shop'):
		dic = {}
		parse_xml(shop, dic)
		list_dic.append(dic)
	return pd.DataFrame(list_dic)

def get_large_service_areas():
	with open('ref_hotpepper/large_service_area.xml', mode='r') as f:
		content = f.read()
	xml_string = re.sub(r' xmlns=".*?"', '', content, count=1)
	root = ET.fromstring(xml_string)
	return [large_service_area.find('code').text for large_service_area in root.findall('large_service_area')]

# get the number of shops in the large_service_area
def get_shop_length(large_service_area):
	content = get_responce(large_service_area, 1, 1).content
	xml_string = re.sub(rb' xmlns=".*?"', b'', content, count=1)
	root = ET.fromstring(xml_string)
	return int(root.find('results_available').text)

def get_dataframe(count=100):
	list_dataframe = []
	large_service_areas = get_large_service_areas()
	for large_service_area in large_service_areas:
		shop_length = get_shop_length(large_service_area)
		n = (shop_length - 1) // count + 1
		for i in range(n):
			start = i * count + 1
			content = get_responce(large_service_area, start, count).content
			list_dataframe.append(xml_to_dataframe(content))
	return pd.concat(list_dataframe).set_index('id')
