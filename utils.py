# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    utils.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/29 17:28:22 by qpupier           #+#    #+#              #
#    Updated: 2026/09/29 17:46:55 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import pandas as pd
from math import log, exp

def g(z):
	return 1 / (1 + exp(-z))

def	h(theta, x):
	return g(sum(theta * x_i for theta, x_i in zip(theta, x)))

# def log(x):
# 	if x == 0:
# 		return -1000000
# 	return exp(x)

def	get_features_from_df(df):
	features = []
	for column in df.columns:
		if column != "Index" and column != "Hogwarts House" and pd.api.types.is_numeric_dtype(df[column]):
			features.append(column)
	return features

def	normalize(df, features, mins, maxs):
	return (df[features] - mins) / (maxs - mins)

def	normalize_from_weights(df, features, weights_df):
	mins = weights_df.loc[features, "Min"]
	maxs = weights_df.loc[features, "Max"]
	return normalize(df, features, mins, maxs)

houses = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]