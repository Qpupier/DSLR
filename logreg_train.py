# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logreg_train.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/29 11:49:42 by qpupier           #+#    #+#              #
#    Updated: 2026/10/01 13:59:51 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

from utils import *

LEARNING_RATE = 0.1
NB_EPOCHS = 1000

def gradient_descent(gradients, batch_size, thetas, house):
	gradients = [gradient / batch_size for gradient in gradients]
	return [theta - LEARNING_RATE * gradient for theta, gradient in zip(thetas[house], gradients)]

def	train(dataset_path, batch_size, nb_epochs=NB_EPOCHS, display=True):
	df = parse_csv(dataset_path)
	if not COLUMN_HOUSE_NAME in df.columns:
		error(f"Missing '{COLUMN_HOUSE_NAME}' column in the dataset.")
	features = get_features_from_df(df)

	m = len(df)
	if not m:
		error("The dataset is empty.")

	mins = pd.Series([df[feature].min() for feature in features], index=features)
	maxs = pd.Series([df[feature].max() for feature in features], index=features)
	means = pd.Series([df[feature].mean() for feature in features], index=features)
	range_size = range(len(features) + 1)

	thetas = {house: [0 for _ in range_size] for house in HOUSES}
	loss_history = {house: [] for house in HOUSES}
	df = df.fillna(means)
	df[features] = normalize(df, features, mins, maxs)

	for i in range(nb_epochs):
		df = df.sample(frac=1, random_state=i).reset_index(drop=True)
		for house in thetas.keys():
			for index, student in df.iterrows():
				if not (index % batch_size):
					loss = 0
					gradients = [0 for _ in range_size]
				x = [student[feature] for feature in features] + [1]
				y = 1 if student[COLUMN_HOUSE_NAME] == house else 0
				prediction = h(thetas[house], x)
				loss += y * log(prediction) + (1 - y) * log(1 - prediction)
				error_diff = prediction - y
				gradients = [gradient_theta + error_diff * x_theta for gradient_theta, x_theta in zip(gradients, x)]
				if not ((index + 1) % batch_size):
					loss_history[house].append(-loss / batch_size)
					thetas[house] = gradient_descent(gradients, batch_size, thetas, house)
			remaining = m % batch_size
			if remaining:
				loss_history[house].append(-loss / remaining)
				thetas[house] = gradient_descent(gradients, remaining, thetas, house)

	weights_df = pd.DataFrame({
		"Feature": features + ["Bias"],
		"Min": list(mins) + [None],
		"Max": list(maxs) + [None],
		"Mean": list(means) + [None]
	})
	for house in HOUSES:
		weights_df[f"Theta_{house}"] = thetas[house]
	if display:
		print(weights_df)
	weights_df.to_csv('weights.csv', index=False)

	if display:
		for house in HOUSES:
			plt.plot(loss_history[house], label=house)
		plt.xlabel("Epochs")
		plt.ylabel("Loss")
		plt.title("Loss during gradient descent")
		plt.legend()
		plt.grid(True)
		plt.show()

if __name__ == "__main__":
	if len(sys.argv) != 2:
		error(f"Usage: python logreg_train.py <dataset.csv> [--sgd | --mini-batch <batch_size>]")
	batch_size = 1
	train(sys.argv[1], batch_size)
