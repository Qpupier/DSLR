# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scatter_plot.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/25 16:38:17 by tdutel            #+#    #+#              #
#    Updated: 2026/09/30 12:08:14 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

from utils import *

df = parse_csv('datasets/dataset_train.csv')

feature = "Care of Magical Creatures"

for house in COLORS:
	data = df[df[COLUMN_HOUSE_NAME] == house]
	plt.scatter(data['Astronomy'], data['Defense Against the Dark Arts'], color=COLORS[house], label=house)

plt.title(feature)
plt.xlabel("Grades")
plt.ylabel("Number of Students")
plt.legend()
plt.show()
