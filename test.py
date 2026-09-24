import pandas as pd
# importer le dataset dans /datasets/dataset_train.csv
data = pd.read_csv('datasets/dataset_train.csv')

# print (data)
# print(data.dtypes)
# print(data["Hogwarts House"].value_counts())

# print (data.describe())

# print(data.columns)
# selectionner uniquement les colonnes numériques
columns_numeric = data.select_dtypes(include=['float64', 'int64']).columns
# print(columns_numeric)


# nombre de collonnes numeriques
print(f"Nombre de colonnes numériques: {len(columns_numeric)}\n\n")

# afficher sur une ligne chaque nom de colonne numerique dans le but de faire un tableau visuel dessous
print("features :\t", end="")
for col in columns_numeric:
    print(col, end="\t")

somme = 0
compteur = 0
print("\nCount :\t", end="")
for i in range(len(columns_numeric)):
	for valeur in data[columns_numeric[i]]:
		if pd.notna(valeur):
			somme += valeur
			compteur += 1
	print(compteur, end="\t")


moyenne = somme / compteur

print(moyenne)







			# for i in columns_numeric:
			# 	count = 0
			# 	for j in columns_numeric[i]:
			# 		if columns_numeric[i] :
			# 			count += 1
			# 	print(f"{i}: {count}")
# afficher le nombre de count pour chaque colonne numérique
# for col in columns_numeric:
    # print(f"{col}: {data[col].count()}")

# count = sum
# mean =
# std = 
# min =
# twenty_five =
# fifty =
# seventy_five =
# max =
