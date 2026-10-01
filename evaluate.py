# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_accuracy.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/01 13:48:24 by qpupier           #+#    #+#              #
#    Updated: 2026/10/01 14:00:19 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

from utils import *
from separate_train_dataset import separate_dataset
from logreg_train import train
from logreg_predict import predict

if __name__ == "__main__":
	if len(sys.argv) != 2:
		error(f"Usage: python test_accuracy.py <nb>")

	try:
		nb = int(sys.argv[1])
	except ValueError:
		error(f"Invalid number of tests: {sys.argv[1]}")

	accuracy = 0
	for i in range(nb):
		separate_dataset("datasets/dataset_train.csv", display=False)
		train("datasets/dataset_train_80.csv", 1280, nb_epochs=500, display=False)
		accuracy += predict("datasets/dataset_train_20.csv", "weights.csv", display=False)
	print(f"\nAverage accuracy over {nb} tests: {accuracy / nb:.2%}")
