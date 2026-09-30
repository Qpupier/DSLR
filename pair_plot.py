# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    pair_plot.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/25 15:19:34 by qpupier           #+#    #+#              #
#    Updated: 2026/09/30 12:10:36 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import seaborn as sns
from utils import *

df = parse_csv('datasets/dataset_train.csv')
# df = parse_csv('datasets/muggle_test.csv')

features = get_features_from_df(df)

sns.pairplot(
	df,
	vars=features,
	diag_kind="hist",
	diag_kws={
		"bins": 20
	},
	hue=COLUMN_HOUSE_NAME,
	palette=COLORS
)
plt.show()
