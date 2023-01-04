import networkx as nx
import matplotlib.pyplot as plt


#recuperation des donnees sous forme d'une liste de liste
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
    return(lst_donnees)

# Dessinez le graphique
def dessiner (G):
    pos = nx.circular_layout(G)
    nx.draw_networkx_nodes(G,pos)
    nx.draw_networkx_edges(G,pos)
    nx.draw_networkx_labels(G,pos) 
    plt.show()

def cree_graph_incompatibilite():
    lst_donnees = recup_donnees()
    lst_signaux = []
    # Créez un graphique vide
    G = nx.Graph()
    # Ajoutez des noeuds et des arêtes
    for signal in lst_donnees :
        G.add_node(signal[0])
        lst_signaux.append(signal[0])
    # Ajoute les arretes representant les incompatibilite c'est a dire les superpositions de freq
    while lst_donnees :
        signal_selec = lst_donnees[0]
        lst_donnees.pop(0)
        for signal_comparé in lst_donnees :
            if signal_selec[1][0]-10 > signal_comparé[1][1] or signal_selec[1][1]+10 > signal_comparé[1][0]:
                G.add_edge(signal_selec[0],signal_comparé[0])
    return G

graph_incompatible = cree_graph_incompatibilite()
dessiner(graph_incompatible)





