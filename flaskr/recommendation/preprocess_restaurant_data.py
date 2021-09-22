import xml.etree.ElementTree as ET
import re
import pandas as pd

def get_reference(query):
	with open('ref_hotpepper/{}.xml'.format(query), mode='r') as f:
		content = f.read()
	xml_string = re.sub(r' xmlns=".*?"', '', content, count=1)
	root = ET.fromstring(xml_string)
	return [tag.find('code').text for tag in root.findall(query)]

def preprocess(df):
    # almost same as `pandas.get_dummies` but this follows the API reference
    features = pd.DataFrame()
    for genre in get_reference('genre'):
        features['genre_'+genre] = ((df['genre>code'] == genre) | (df['sub_genre>code'] == genre)).astype(int)
    mapping = {}
    for i, budget in enumerate(get_reference('budget')):
        mapping[budget] = i
    features['budget'] = df['budget>code'].map(mapping)
    return features.values