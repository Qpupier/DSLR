# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    pair_plot.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/25 15:19:34 by qpupier           #+#    #+#              #
#    Updated: 2026/09/25 16:00:49 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('datasets/dataset_train.csv')
# df = pd.read_csv('datasets/muggle_test.csv')
subjects = []
for column in df.columns:
	if column != "Hogwarts House" and column != "Index" and pd.api.types.is_numeric_dtype(df[column]):
		subjects.append(column)
sns.pairplot(
	df,
	vars=subjects,
	diag_kind="hist",
	diag_kws={
		"bins": 20
	},
	hue="Hogwarts House",
	palette={
		"Gryffindor": "red",
		"Hufflepuff": "yellow",
		"Ravenclaw": "blue",
		"Slytherin": "green",
		"Muggle": "black"
	}
)
plt.show()
