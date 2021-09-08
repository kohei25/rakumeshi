import pandas as pd
import numpy as np

import sqlite3

def get_latest_data(index):
    #get features latest data from SQL
    con = sqlite3.connect('../rakumeshi.db')
    cur = con.cursor()
    query = f'SELECT age, budget, sex, genre FROM user_features'
    data = cur.execute(query).fetchall()
    con.commit()
    return data[index]


def get_binary_vector(data):
    #convert data into binary vector through pandas dataframe
    dfm = pd.DataFrame(data).T.set_axis(['age', 'budget', 'sex', 'genre'], axis=1)
    sex_categories = {0, 1, 2}
    genre_categories = {1, 2, 3, 4, 5, 6, 7}
    dfm['sex'] = pd.Categorical(dfm['sex'], categories=sex_categories)
    dfm['genre'] = pd.Categorical(dfm['genre'], categories=genre_categories)
    binary_vector = pd.get_dummies(dfm, columns=['sex', 'genre']).values
    return binary_vector


def write_binary_vector(binary_vector):
    #read numpy data and append binary vector as numpy file
    numpy_data = np.load('user_features.npy')
    update_numpy_data = np.append(numpy_data, binary_vector, axis=0)
    np.save('user_features.npy', update_numpy_data)
    return


if __name__ == '__main__':
    #np.save('user_features.npy', np.empty((0,12)))  #create empty numpy data
    latest_data = get_latest_data(-1)
    binary_vector = get_binary_vector(latest_data)
    write_binary_vector(binary_vector)
