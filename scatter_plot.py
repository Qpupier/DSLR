# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scatter_plot.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tdutel <tdutel@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/25 16:38:17 by tdutel            #+#    #+#              #
#    Updated: 2026/09/25 16:44:24 by tdutel           ###   ########.fr        #
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
	data = df[df["Hogwarts House"] == house]
	plt.scatter(data['Astronomy'], data['Defense Against the Dark Arts'], color=colors[house], label=house)

plt.title(feature)
plt.xlabel("Notes")
plt.ylabel("Nombre d'élèves")
plt.legend()
plt.show()
