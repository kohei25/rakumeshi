import pandas as pd
import sqlite3
from get_restaurant_data import get_dataframe
from preprocess_restaurant_data import preprocess

restaurant_data = get_dataframe()
# restaurant_data.to_csv('restaurants.csv')

# Save dataframe as sqlite3

# preprocess DataFrame and make features matrix
restaurant_features = preprocess(restaurant_data)

# calculate similarity among restaurants and save it as sqlite3