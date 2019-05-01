#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 17:29:20 2019

@author: daddy
"""

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

"""Extraire et créer un fichier EXCEL contenant les liste des élèves ayant la moyenne"""

# Lecture de notre jeu de données
df = pd.read_csv('project_data_science.csv')
print(df)

# Filtrer la colonne Moyenne afin de sortir les éléves ayant une moyenne supérieur ou égal à 10
means = df[(df['Moyenne'] >= 10)]
print(means)

# Création d'un fichier csv contenant l'ensemble des éléves ayant la moyennne
file_mean_students = means.to_csv('file_mean_students.csv', index=False)

# Lecture du fichier csv des éléves ayant la moyenne
students_has_means = pd.read_csv('file_mean_students.csv')
print(students_has_means)

"""Extraire et créer un fichier EXCEL contenant les élèves ayant plus de 20 ans"""

# Filtrer les éléves ayant plus de 20 ans dans la colonne Age
high_students = df[(df['Age'] > 20)]
print(high_students)

# Création d'un fichier csv contenant les éléves qui ont plus de 20 ans
file_high_students = high_students.to_csv('file_high_students.csv', index=False)

# Lecture du fichier csv des éléves ayant plus de 20 ans
students_high = pd.read_csv('file_high_students.csv')
print(students_high)

"""Extraire et créer un fichier EXCEL contenant les statistiques globales de l’école"""

# Calcul de la moyenne de l'école
mean_school = df.loc[:,"Moyenne"].mean()
print(mean_school)

# Calcul du nombre total de filles ainsi que de garçons
total_per_sex = df.groupby(['Sexe']).size()
print(total_per_sex)

# Afficher le nombre total de filles
nb_woman = total_per_sex['F']
print(nb_woman)

# Afficher le nombre total de garçons
nb_man = total_per_sex['M']
print(nb_man)

# Afficher le nombre total d'éléves
total_students = len(df)
print(total_students)

# Calcul du pourcentage de filles 
percentage_woman = (nb_woman*100/total_students)
print(percentage_woman)

# Calcul du pourcentage de garçons 
percentage_man = (nb_man*100/total_students)
print(percentage_man)

# Afficher la région ayant enregistré la plus forte moyenne
region = df.loc[df['Moyenne'].idxmax(), ['Région']]
location = region['Région']
print(location)

# Création de notre dictionnaire contenant la moyenne de l'école, le pourcentage de filles et de garçons, la région ayant la plus forte moyenne
statistiques = {'Moyenne de l’école':mean_school, '%fille':percentage_woman, '%garçon':percentage_man, 'Région':location}

# Créer notre dataframe avec les données statistiques
stat = DataFrame(statistiques, index=[0])

# Création d'un fichier csv contenant les donné statistiques
file_statistique = stat.to_csv('file_statistique.csv', index=False)

# Lecture du fichier csv contenant les données statistiques
stat_school = pd.read_csv('file_statistique.csv')
print(stat_school)