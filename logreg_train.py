# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logreg_train.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/29 11:49:42 by qpupier           #+#    #+#              #
#    Updated: 2026/09/30 18:39:14 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

from utils import *

LEARNING_RATE = 0.01
NB_EPOCHS = 10000

if __name__ == "__main__":

	if len(sys.argv) != 2:
		error(f"Usage: python logreg_train.py <dataset.csv>")

	df = parse_csv(sys.argv[1])
	features = get_features_from_df(df)

	if not COLUMN_HOUSE_NAME in df.columns:
		error(f"Missing '{COLUMN_HOUSE_NAME}' column in the dataset.")

	mins = pd.Series([df[feature].min() for feature in features], index=features)
	maxs = pd.Series([df[feature].max() for feature in features], index=features)
	means = pd.Series([df[feature].mean() for feature in features], index=features)
	range_size = range(len(features) + 1)
	m = len(df)
	if not m:
		error("The dataset is empty.")

	thetas = {house: [0 for _ in range_size] for house in HOUSES}
	theta_history = {house: [] for house in HOUSES}
	loss_history = {house: [] for house in HOUSES}
	df = df.fillna(means)
	df[features] = normalize(df, features, mins, maxs)

	for house in thetas.keys():
		for i in range(NB_EPOCHS):
			gradients = [0 for _ in range_size]
			loss = 0
			abs_errors = 0
			for _, row in df.iterrows():
				x = [row[feature] for feature in features] + [1]
				y = 1 if row[COLUMN_HOUSE_NAME] == house else 0
				prediction = h(thetas[house], x)
				loss += y * log(prediction) + (1 - y) * log(1 - prediction)
				error_diff = prediction - y
				abs_errors += abs(error_diff)
				gradients = [gradient_theta + error_diff * x_theta for gradient_theta, x_theta in zip(gradients, x)]
			gradients = [gradient / m for gradient in gradients]
			thetas[house] = [theta - LEARNING_RATE * gradient for theta, gradient in zip(thetas[house], gradients)]
			theta_history[house].append(abs_errors / m)
			loss_history[house].append(-loss / m)

	weights_df = pd.DataFrame({
		"Feature": features + ["Bias"],
		"Min": list(mins) + [0],
		"Max": list(maxs) + [0],
		"Mean": list(means) + [0]
	})
	for house in HOUSES:
		weights_df[f"Theta_{house}"] = thetas[house]
	print(weights_df)
	weights_df.to_csv('weights.csv', index=False)

	for house in HOUSES:
		plt.plot(loss_history[house], label=house)
	plt.xlabel("Epochs")
	plt.ylabel("Loss")
	plt.title("Loss during gradient descent")
	plt.legend()
	plt.grid(True)
	plt.show()

	plt.figure(figsize=(10, 6))
	for house in HOUSES:
		plt.plot(theta_history[house], label=house)
	plt.title("Evolution of the error by house")
	plt.xlabel("Epochs")
	plt.ylabel("Error")
	plt.legend()
	plt.grid(True)
	plt.tight_layout()
	plt.show()
