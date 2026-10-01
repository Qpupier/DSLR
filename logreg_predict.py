# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logreg_predict.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/29 15:31:56 by qpupier           #+#    #+#              #
#    Updated: 2026/10/01 13:55:28 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

from utils import *
from sklearn.metrics import accuracy_score

def predict(test_path, weights_path, display=True):
	test_df = parse_csv(test_path)
	weights_df = parse_csv(weights_path, index_col=0)

	features = get_features_from_df(test_df)
	for feature in features:
		if not feature in weights_df.index:
			error(f"Feature '{feature}' not found in weights.csv")
	for house in HOUSES:
		if not f"Theta_{house}" in weights_df.columns:
			error(f"Theta for house '{house}' not found in weights.csv")
	test_df.fillna(weights_df.loc[features, "Mean"], inplace=True)
	test_df[features] = normalize_from_weights(test_df, features, weights_df)

	list_predictions = []
	verities = []
	predicted_houses = []
	for _, row in test_df.iterrows():
		x = [row[feature] for feature in features] + [1]
		predictions = {house: h(weights_df[f'Theta_{house}'].values, x) for house in HOUSES}
		predicted_house = max(predictions, key=predictions.get)
		if row[COLUMN_HOUSE_NAME] in HOUSES:
			list_predictions.append(predicted_house)
			verities.append(row[COLUMN_HOUSE_NAME])
		predicted_houses.append(predicted_house)

	houses_df = pd.DataFrame({
		COLUMN_INDEX_NAME: test_df[COLUMN_INDEX_NAME],
		COLUMN_HOUSE_NAME: predicted_houses
	})
	if display:
		print(houses_df)
	houses_df.to_csv('houses.csv', index=False)

	if list_predictions:
		return accuracy_score(verities, list_predictions)
	return None

if __name__ == "__main__":
	if len(sys.argv) != 3:
		error(f"Usage: python logreg_predict.py <dataset.csv> <weights.csv>")
	accuracy = predict(sys.argv[1], sys.argv[2])
	if accuracy is not None:
		print(f"\nAccuracy: {accuracy:.2%}")
