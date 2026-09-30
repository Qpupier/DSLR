# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    histogram.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/25 11:38:23 by tdutel            #+#    #+#              #
#    Updated: 2026/09/30 12:07:59 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

from utils import *

df = parse_csv('datasets/dataset_train.csv')

feature = "Care of Magical Creatures"

for house in COLORS:
	data = df[df[COLUMN_HOUSE_NAME] == house]
	plt.hist(data[feature], bins=15, color=COLORS[house], alpha=0.5, label=house)

plt.title(feature)
plt.xlabel("Grades")
plt.ylabel("Number of Students")
plt.legend()
plt.show()
