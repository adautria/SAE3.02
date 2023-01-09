import os
from random import randint
def cree_donnees_f(nb_signaux):
   try:
      # Envoie le fichier donnees.txt dans la corbeille
      os.remove('donnees2.txt')
   except FileNotFoundError:
      # Le fichier n'existe pas, rien à faire
      pass
      
   fichier = open('donnees.txt', 'w')

   for i in range (nb_signaux):
      freq_min = randint (0,1000)
      bp = randint (20,500)
      freq_max = freq_min + bp 
      ligne = str(i+1) + ' ' + str(freq_min) + ' ' + str(freq_max) + '\n'
      fichier.write(ligne)


   fichier.close()
