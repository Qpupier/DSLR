# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logreg_train.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tdutel <tdutel@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/28 11:48:06 by tdutel            #+#    #+#              #
#    Updated: 2026/09/28 23:29:00 by tdutel           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import	sys
from	pathlib import Path
import	pandas as pd


# On passe par une standardisation des données pour que les notes des features aient toutes la même échelle

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

means = {}
for feature in features:

	total = 0
	count = 0

	for value in df[feature]:
		if not pd.isna(value):
			total += value
			count += 1

	mean = total / count if count > 0 else 0
	df.loc[df[feature].isna(), feature] = mean
	means[feature] = mean

	# print("\n\n Feature :", feature)
	# print("\n\nligne 4 du df :", df.iloc[4]) # tester avec un eleve qui a NaN a Defense Against the Dark Arts, pour voir si la valeur a été remplacée par la moyenne
	# print("ligne 4 du df :", df.iloc[43])


#############################################################################################
#	Standardize the features by subtracting the mean and dividing by the standard deviation	#
#############################################################################################
standard_deviations = {}

for feature in features:
	squared_diff_sum = 0

	for value in df[feature]:
		squared_diff_sum += (value - means[feature]) ** 2

	standard_deviations[feature] = (squared_diff_sum / len(df[feature])) ** 0.5 if len(df[feature]) > 0 else 0 # Avoid division by zero

	df[feature] = (df[feature] - means[feature]) / standard_deviations[feature]

print((df[features]))


#######################################################################
# creation d'une classification binaire pour chaque maison, pour pouvoir faire du one-vs-all
#######################################################################
house = "Gryffindor"		# pour tester un premier modele avec gryffindor, puis on pourra faire un modele pour chaque maison

y = []

for student_house in df["Hogwarts House"]:
	if student_house == house:
		y.append(1)
	else:
		y.append(0)

# ###########################################################################
# #	Calculer le score z
# ###########################################################################
theta = [0] * (len(features) + 1)
scoreZ = []
for student in range(len(df)):
	z = theta[0]

	for i in range(len(features)):
		print(features[i], "\t\t\t\tValue:",  df.loc[student, features[i]], "Theta:", theta[i + 1])
		z += theta[i + 1] * df.loc[student, features[i]] 
		print("z:", z)
	scoreZ.append(z)
	exit() # pour tester l'affichage des features et des valeurs de theta
