# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scatter_plot.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/25 16:38:17 by tdutel            #+#    #+#              #
#    Updated: 2026/10/02 11:22:53 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

from utils import *

df = parse_csv('datasets/dataset_train.csv')

feature_x = "Astronomy"
feature_y = "Defense Against the Dark Arts"

for house in COLORS:
	data = df[df[COLUMN_HOUSE_NAME] == house]
	plt.scatter(data[feature_x], data[feature_y], color=COLORS[house], label=house)

plt.title(f"{feature_x} vs {feature_y}")
plt.xlabel(f"Grades in {feature_x}")
plt.ylabel(f"Grades in {feature_y}")
plt.legend()
plt.show()
