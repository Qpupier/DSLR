# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logreg_train.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tdutel <tdutel@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/28 11:48:06 by tdutel            #+#    #+#              #
#    Updated: 2026/09/28 14:23:53 by tdutel           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import	sys
from	pathlib import Path
import	pandas as pd


##############################################
#	Load the CSV file and check for errors	#
#############################################

if len(sys.argv) != 2:
	print("Usage: python logreg_train.py <csv_file>")
	sys.exit(1)
csv_file = Path(sys.argv[1])
if not csv_file.is_file():
	print(f"Error: file not found: {csv_file}", file=sys.stderr)
	sys.exit(1)

df = pd.read_csv(csv_file)
features = []
for column in df.columns:
	if column != "Index" and column != "Hogwarts House" and pd.api.types.is_numeric_dtype(df[column]):
		features.append(column)


#############################################################################
#	Replace NaN values in each feature column with the mean of that column	#
#############################################################################

for feature in features:

	total = 0
	count = 0

	for value in df[feature]:
		if not pd.isna(value):
			total += value
			count += 1

	mean = total / count if count > 0 else 0

	df.loc[df[feature].isna(), feature] = mean

	# print("\n\n Feature :", feature)
	# print("\n\nligne 4 du df :", df.iloc[4]) # tester avec un eleve qui a NaN a Defense Against the Dark Arts, pour voir si la valeur a été remplacée par la moyenne
	# print("ligne 4 du df :", df.iloc[43])


#############################################################################################
#	Standardize the features by subtracting the mean and dividing by the standard deviation	#
#############################################################################################

