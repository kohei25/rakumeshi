import numpy as np
import pandas as pd


def get_similarities(feature_vector):
    """
    ベクトル同士のコサイン類似度行列を計算する
    """
    similarities = np.zeros((feature_vector.shape[0], feature_vector.shape[0]))

    for i1, v1 in enumerate(feature_vector):
        for i2, v2 in enumerate(feature_vector):
            similarities[i1][i2] = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

    return similarities


def predict_rating(rating, item_index, similarities):
    """
    評価値を予測する
    """
    numerator = 0.0
    enumerator = 0.0
    epsilon = 0.0001

    for i, r in enumerate(rating):
        if r != -1:
            numerator += similarities[item_index][i] * r
            enumerator += similarities[item_index][i]

    return numerator / (enumerator+epsilon)


def rank_items(ratings, similarities):
    """
    (アイテムのインデックス, 予測した評価値)のタプルリストをランキング(評価値の降順ソート)で返す
    """
    ranking = [ ]

    for i, r in enumerate(ratings):
        if r != -1:
            continue

        ranking.append((i, predict_rating(ratings, i, similarities)))

    return sorted(ranking, key=lambda r: r[1], reverse=True)


if __name__ == '__main__':

    data = pd.read_csv('restaurants_tokyo_raiting.csv')

    onehot_data = pd.get_dummies(data, columns=['budget', 'genre'])
    onehot_data = onehot_data.fillna(-1)

    features = onehot_data.iloc[:,4:].values
    ratings = onehot_data['rating'].values

    similarities = get_similarities(features)
    sorted_ranking = rank_items(ratings, similarities)

    top_k = 10
    data_name = data['name'].values
    for i in range(top_k):
        print('{}位:{};   予測評価値:{:.2f}'.format(i+1,data_name[sorted_ranking[i][0]],sorted_ranking[i][1]))
