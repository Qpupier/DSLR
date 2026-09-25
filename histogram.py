# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    histogram.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tdutel <tdutel@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/25 11:38:23 by tdutel            #+#    #+#              #
#    Updated: 2026/09/25 16:37:02 by tdutel           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd		# sert à manipuler des données sous forme de tableaux, notamment les fichiers CSV
import matplotlib.pyplot as plt		#sert à tracer des graphiques

df = pd.read_csv('datasets/dataset_train.csv')

feature = "Care of Magical Creatures"
colors = {
	"Gryffindor": "red",
	"Hufflepuff": "yellow",
	"Ravenclaw": "blue",
	"Slytherin": "green"
}


for house in colors:
	data = df[df["Hogwarts House"] == house][feature]
	plt.hist(data, bins=15, color=colors[house], alpha=0.5, label=house)

plt.title(feature)
plt.xlabel("Notes")
plt.ylabel("Nombre d'élèves")
plt.legend()
plt.show()







































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
