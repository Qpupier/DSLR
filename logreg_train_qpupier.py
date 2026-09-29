# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logreg_train_qpupier.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/29 11:49:42 by qpupier           #+#    #+#              #
#    Updated: 2026/09/29 17:47:02 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

from utils import pd, h, get_features_from_df, normalize, houses

LEARNING_RATE = 0.1
NB_ITERATIONS = 100

if __name__ == "__main__":
	df = pd.read_csv('datasets/dataset_train.csv')
	features = get_features_from_df(df)

	mins = pd.Series([df[feature].min() for feature in features], index=features)
	maxs = pd.Series([df[feature].max() for feature in features], index=features)
	means = pd.Series([df[feature].mean() for feature in features], index=features)
	range_size = range(len(features) + 1)
	m = len(df)

	thetas = {house: [0 for _ in range_size] for house in houses}

	df = df.fillna(means)
	df[features] = normalize(df, features, mins, maxs)

	for house in thetas.keys():
		for i in range(NB_ITERATIONS):
			gradients = [0 for _ in range_size]
			# loss = [0 for _ in range(m)]
			for _, row in df.iterrows():
				x = [row[feature] for feature in features] + [1]
				y = 1 if row["Hogwarts House"] == house else 0
				# loss = [loss_theta + y * log(h(thetas[house], x)) + (1 - y) * log(1 - h(thetas[house], x)) for loss_theta in loss]
				error = h(thetas[house], x) - y
				gradients = [gradient_theta + error * x_theta for gradient_theta, x_theta in zip(gradients, x)]
			# loss = [-j_theta / m for j_theta in loss]
			gradients = [gradient / m for gradient in gradients]
			thetas[house] = [theta - LEARNING_RATE * gradient for theta, gradient in zip(thetas[house], gradients)]

	weights_df = pd.DataFrame({
		"Feature": features + ["Bias"],
		"Min": list(mins) + [0],
		"Max": list(maxs) + [0],
		"Mean": list(means) + [0]
	})
	for house in houses:
		weights_df[f"Theta_{house}"] = thetas[house]
	print(weights_df)
	weights_df.to_csv('weights.csv', index=False)
