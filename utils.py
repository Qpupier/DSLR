# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    utils.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/29 17:28:22 by qpupier           #+#    #+#              #
#    Updated: 2026/09/30 11:55:20 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import sys
import pandas as pd
from math import log, exp

COLUMN_HOUSE_NAME = "Hogwarts House"
COLUMN_INDEX_NAME = "Index"
HOUSES = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]

def g(z):
	return 1 / (1 + exp(-z))

def	h(theta, x):
	return g(sum(theta * x_i for theta, x_i in zip(theta, x)))

def	get_features_from_df(df):
	features = []
	for column in df.columns:
		if column != COLUMN_INDEX_NAME and column != COLUMN_HOUSE_NAME and pd.api.types.is_numeric_dtype(df[column]):
			features.append(column)
	return features

def	normalize(df, features, mins, maxs):
	try:
		return (df[features] - mins) / (maxs - mins)
	except Exception as e:
		error(f"Normalization error: {e}")

def	normalize_from_weights(df, features, weights_df):
	if not "Min" in weights_df.columns or not "Max" in weights_df.columns:
		error("weights.csv must contain 'Min' and 'Max' columns for normalization.")
	mins = weights_df.loc[features, "Min"]
	maxs = weights_df.loc[features, "Max"]
	return normalize(df, features, mins, maxs)

def error(msg):
	print(f"Error: {msg}", file=sys.stderr)
	sys.exit(1)

def parse_csv(file_path, index_col=None):
	try:
		return pd.read_csv(file_path, index_col=index_col)
	except FileNotFoundError:
		error(f"File not found: {file_path}")
	except pd.errors.EmptyDataError:
		error(f"File is empty: {file_path}")
	except pd.errors.ParserError:
		error(f"File is not a valid CSV: {file_path}")
	except Exception as e:
		error(e)
