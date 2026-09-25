# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    histogram.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tdutel <tdutel@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/25 11:38:23 by tdutel            #+#    #+#              #
#    Updated: 2026/09/25 16:38:47 by tdutel           ###   ########.fr        #
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
