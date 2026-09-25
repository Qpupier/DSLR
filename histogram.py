# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    histogram.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tdutel <tdutel@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/25 11:38:23 by tdutel            #+#    #+#              #
#    Updated: 2026/09/25 14:59:05 by tdutel           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd		# sert à manipuler des données sous forme de tableaux, notamment les fichiers CSV
import matplotlib.pyplot as plt		#sert à tracer des graphiques
import numpy as np		#sert

df = pd.read_csv('datasets/dataset_train.csv')
print(df.columns)

# stocker les maisons dans une liste
houses = []
for house in df["Hogwarts House"].unique():
	houses.append(house)
# stocker les matières dans une liste 
subjects = []

for column in df.columns:
	if column != "Hogwarts House" and column != "Index" and pd.api.types.is_numeric_dtype(df[column]):
		subjects.append(column)
print(len(subjects))

# for house in houses:










































"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('datasets/dataset_train.csv')

houses = ['Gryffindor', 'Slytherin', 'Ravenclaw', 'Hufflepuff']
colors = ['red', 'green', 'blue', 'yellow']
subjects = []
for subject in df.columns:
	if subject != "Hogwarts House" and subject != "Index" and pd.api.types.is_numeric_dtype(df[subject]):
		subjects.append(subject)

columns = 3
rows = (len(subjects) + columns - 1) // columns
fig, axes = plt.subplots(rows, columns, figsize=(18, rows * 5))
axes = axes.flatten()

for axis, subject in zip(axes, subjects):
	scores = df[subject].dropna()
	bins = 20
	for house, color in zip(houses, colors):
		axis.hist(
			df[df['Hogwarts House'] == house][subject].dropna(),
			bins=bins,
			color=color,
			alpha=0.5,
			label=house
		)
	axis.set_xlabel('Scores')
	axis.set_ylabel('Fréquence')
	axis.set_title(f'Distribution des scores en {subject}')
	axis.legend()

for axis in axes[len(subjects):]:
	axis.set_visible(False)

fig.tight_layout()
plt.show()


# Quelle matière possède une distribution de scores homogène entre les quatre maisons ?

"""
