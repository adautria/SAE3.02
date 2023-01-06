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


def dessiner_couleur (G,C):
    node_colors = [v['couleur'] for v in G.nodes.values()]
    pos = nx.circular_layout(G)
    nx.draw_networkx_nodes(G,pos,node_color=node_colors)
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
        for signal_compare in lst_donnees :
            if signal_selec[1][0]-10 > signal_compare[1][1] or signal_selec[1][1]+10 < signal_compare[1][0]:
                pass
            else:
                G.add_edge(signal_selec[0],signal_compare[0])
    return G


# Dessinez le graphique
def dessiner_graph ():
    G = cree_graph_incompatibilite()
    pos = nx.circular_layout(G)
    nx.draw_networkx_nodes(G,pos)
    nx.draw_networkx_edges(G,pos)
    nx.draw_networkx_labels(G,pos) 
    plt.show()

def algo_welsh ():
    G = cree_graph_incompatibilite()
    lst_noeuds = G.nodes()
    dico_couleurs_choisies = {}
    for noeud in lst_noeuds:
        nx.set_node_attributes(G, {noeud: 'blanc'}, 'couleur')
    for noeud in lst_noeuds:
        lst_voisins = list(G.neighbors(noeud))
        couleurs_possibles = {"blanc": 1,"rouge":0, "orange":0, 'jaune':0, 'vert':0, 'bleu':0, 'violet':0, 'marron':0, 'gris':0, 'noir':0, 'rose':0, 'turquoise':0, 'indigo':0, 'magenta':0, 'cyan':0}
        for voisin in lst_voisins :
            couleur_du_voisin = G.nodes[voisin]['couleur']
            couleurs_possibles[couleur_du_voisin] = 1
        for key,value in couleurs_possibles.items():
            if value == 0 :
                nx.set_node_attributes(G, {noeud: key}, 'couleur')
                dico_couleurs_choisies[noeud]=key
                break
    return dico_couleurs_choisies

def nb_fibre ():
    lst = algo_welsh()
    return int(len(set(lst.values())))






def dessiner_graph ():
    G = cree_graph_incompatibilite()
    pos = nx.circular_layout(G)
    for signal,couleur in lst_couleurs_choisies.items():
        nx.draw_networkx_nodes(G,pos,node_color=couleur,nodelist=[signal])
    nx.draw_networkx_edges(G,pos)
    nx.draw_networkx_labels(G,pos) 
    plt.show()


