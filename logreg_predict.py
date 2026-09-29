# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logreg_predict.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/29 15:31:56 by qpupier           #+#    #+#              #
#    Updated: 2026/09/29 17:52:50 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

from utils import pd, h, get_features_from_df, normalize_from_weights, houses

weights_df = pd.read_csv('weights.csv', index_col=0)
test_df = pd.read_csv('datasets/dataset_test.csv')
# test_df = pd.read_csv('datasets/dataset_train.csv')

features = get_features_from_df(test_df)
test_df.fillna(weights_df.loc[features, "Mean"], inplace=True)
test_df[features] = normalize_from_weights(test_df, features, weights_df)

predicted_houses = []
for _, row in test_df.iterrows():
	x = [row[feature] for feature in features] + [1]
	predictions = {house: h(weights_df[f'Theta_{house}'].values, x) for house in houses}
	predicted_house = max(predictions, key=predictions.get)
	predicted_houses.append(predicted_house)

houses_df = pd.DataFrame({
	'Index': test_df['Index'],
	'Hogwarts House': predicted_houses
})
print(houses_df)
houses_df.to_csv('houses.csv', index=False)
