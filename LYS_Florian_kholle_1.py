# Projet Kholle
# Maitriser des simples opérations en Python
# 25/11/18
# Lys Florian

import csv

# Lecture du fichier 

def read_file():
	with open('file.csv', "r") as r:
		spamreader = csv.reader(r)
		for row in spamreader:
			print(', '.join(row))

# Ecriture dans le fichier

def write_file(message):
	with open('file.csv', "w") as r:
		spamwrite = csv.write(r):
		spamwrite.writerow(message)

# Avoir la valeur maximum

def valeur_max(number):
	max = number[0]
	for value in number:
		if value > max
			max = value
	return max

# Avoir la valeur minimum

def valeur_min(number):
	min = number[0]
	for value in number:
		if value < min
			min = value
	return min

# Calcul de la moyenne

def calcul_moy(number):
	total = 0
	for value in number :
		total += int(value)
	moyenne = total / nbArgs
	return moyenne

# Calcul de la somme

def calcul_som(number):
	total = 0
	for value in number:
		total += int(value)
	return total