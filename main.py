import networkx as nx
import matplotlib.pyplot as plt


# format recuperer
# [[1,[200,400]],[2,[500,600]],[3,[600,900]]]
# cette liste sera nommé lst_donnees
# ecrire un programme nommée recup_donnees

def recup_donnees():
    lst_donnees = []  #On initialise la liste lst_donnees
    with open('donnees.txt', 'r') as d:   #On ouvre le fichier 
        for line in d:
            col1, col2, col3 = line.strip().split(' ')
            col1 = int(col1)
            col2 = int(col2)     #On convertit les valeurs du fichier.txt en nombres (integer)
            col3 = int(col3)
            # maintenant, on peut traiter les données de chaque colonne comme des variables
            lst_donnees.append([col1, [col2, col3]])  #On insère les valeurs dans la liste
    print(lst_donnees)

recup_donnees()
