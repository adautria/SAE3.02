import os
from random import randint

try:
   # Envoie le fichier donnees.txt dans la corbeille
   os.remove('donnees2.txt')
except FileNotFoundError:
   # Le fichier n'existe pas, rien à faire
   pass
   
fichier = open('donnees.txt', 'w')

for i in range (10):
    freq_min = randint (0,1000)
    bp = randint (20,500)
    freq_max = freq_min + bp 
    ligne = str(i+1) + ' ' + str(freq_min) + ' ' + str(freq_max) + '\n'
    fichier.write(ligne)


fichier.close()