import pandas as pd
import sqlite3
from get_restaurant_data import get_dataframe

df = get_dataframe()
df.to_csv('restaurants.csv')

# Save dataframe as sqlite3

# preprocess dataframe

# calculate similarity among restaurants and save it as sqlite3