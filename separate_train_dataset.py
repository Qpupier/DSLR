# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    separate_train_dataset.py                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/30 17:15:36 by qpupier           #+#    #+#              #
#    Updated: 2026/10/01 13:58:44 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

from utils import *

def separate_dataset(dataset_path, display=True):
	df = parse_csv(dataset_path)
	train_df = {}
	for house in HOUSES:
		train_df[house] = df[df[COLUMN_HOUSE_NAME] == house].sample(frac=0.8)
	train_df = pd.concat(train_df.values())
	test_df = df.drop(train_df.index)
	dataset_path = dataset_path.rsplit('.', 1)[0]
	train_df.to_csv(f"{dataset_path}_80.csv", index=False)
	test_df.to_csv(f"{dataset_path}_20.csv", index=False)
	if display:
		print("House distribution in the training dataset:\n")
		print(train_df["Hogwarts House"].value_counts(normalize=True))
		print("\nHouse distribution in the test dataset:\n")
		print(test_df["Hogwarts House"].value_counts(normalize=True))

if __name__ == "__main__":
	if len(sys.argv) != 2:
		error(f"Usage: python separate_train_dataset.py <dataset.csv>")
	separate_dataset(sys.argv[1])
