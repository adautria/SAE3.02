import os
from random import randint


def cree_donnees_f(nb_signaux):
   try:
     # Envoie le fichier donnees.txt dans la corbeille
      os.remove('donnees2.txt') #Supprimer le fichier donnees2.txt s'il existe
   except FileNotFoundError:
      # Le fichier n'existe pas, rien à faire
      pass

   # Ouvrir le fichier donnees.txt en mode écriture
   fichier = open('donnees.txt', 'w') 

   for i in range (nb_signaux):
      # Génère un nombre aléatoire entre 0 et 1000 pour freq_min
      freq_min = randint (0,1000) 
      # Génère un nombre aléatoire entre 20 et 500 pour bp
      bp = randint (20,500) 
      # Calcule la valeur de freq_max
      freq_max = freq_min + bp 
      ligne = str(i+1) + ' ' + str(freq_min) + ' ' + str(freq_max) + '\n'
      # Ecrit les valeurs de i+1, freq_min, freq_max dans le fichier donnees.txt
      fichier.write(ligne) 
   # Ferme le fichier donnees.txt
   fichier.close() 
