import networkx as nx
import matplotlib.pyplot as plt

#variable globale
lst_couleurs_choisies = {}

#recuperation des donnees sous forme d'une liste de liste
def recup_donnees(fichier):
    lst_donnees = []  #On initialise la liste lst_donnees
    with open(fichier, 'r') as d:   #On ouvre le fichier 
        for line in d:
            col1, col2, col3 = line.strip().split(' ')
            col1 = int(col1)
            col2 = int(col2)     #On convertit les valeurs du fichier.txt en nombres (integer)
            col3 = int(col3)
            # maintenant, on peut traiter les données de chaque colonne comme des variables
            lst_donnees.append([col1, [col2, col3]])  #On insère les valeurs dans la liste
    return(lst_donnees)


def cree_graph_incompatibilite(fichier_choisie):
    lst_donnees = recup_donnees(fichier_choisie)
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




def algo_welsh (fichier_choisie):
    G = cree_graph_incompatibilite(fichier_choisie)
    lst_noeuds = G.nodes()
    dico_couleurs_choisies = {}
    for noeud in lst_noeuds:
        nx.set_node_attributes(G, {noeud: 'white'}, 'couleur')
    for noeud in lst_noeuds:
        lst_voisins = list(G.neighbors(noeud))
        couleurs_possibles = {
            "white": 1,
            "red": 0,
            "orange": 0,
            "yellow": 0,
            "green": 0,
            "blue": 0,
            "purple": 0,
            "pink": 0,
            "brown": 0,
            "gray": 0,
            "beige": 0,
            "olive": 0,
            "navy": 0,
            "teal": 0,
            "lavender": 0,
            "turquoise": 0,
            "coral": 0,
            "magenta": 0,
            "crimson": 0,
            "violet": 0}
        for voisin in lst_voisins :
            couleur_du_voisin = G.nodes[voisin]['couleur']
            couleurs_possibles[couleur_du_voisin] = 1
        for key,value in couleurs_possibles.items():
            if value == 0 :
                nx.set_node_attributes(G, {noeud: key}, 'couleur')
                dico_couleurs_choisies[noeud]=key
                break
    return dico_couleurs_choisies

# Dessinez le graphique
def dessiner_graph(fichier_choisie):
    G = cree_graph_incompatibilite(fichier_choisie)
    pos = nx.circular_layout(G)
    dico_couleurs_choisies = algo_welsh(fichier_choisie)
    for signal,couleur in dico_couleurs_choisies.items():
        nx.draw_networkx_nodes(G,pos,node_color=couleur,node_size=700,nodelist=[signal])
    nx.draw_networkx_edges(G,pos)
    nx.draw_networkx_labels(G,pos) 
    plt.show()


def find_largest_clique(fichier_choisie):
    graph = cree_graph_incompatibilite(fichier_choisie)
    max_clique = []
    for v in graph:
        clique = []
        clique.append(v)
        for u in graph:
            if all(x in graph[u] for x in clique):
                clique.append(u)
        if len(clique) > len(max_clique):
            max_clique = clique
    return len(max_clique)

def nb_fibre (fichier_choisie):
    lst = algo_welsh(fichier_choisie)
    result_welsh = int(len(set(lst.values())))
    result_clique = int(find_largest_clique(fichier_choisie))
    if result_clique == result_welsh:
        return f"Un total de {result_welsh} fibres sont nécessaire au minimum "
    else:
        return f"{result_welsh} fibres sont nécessaire (attention le resultat n'est pas optimum)"

def visuel_multi():
    pass


def coordonnées_x(fichier_choisie,signal):
    lst_donnees = recup_donnees(fichier_choisie)
    x1 = lst_donnees[signal-1][1][0]
    x2 = lst_donnees[signal-1][1][1]
    return x1,x2

def coordonnées_y(fichier_choisie,signal):
    dico_couleurs_choisies = algo_welsh(fichier_choisie)
    dico_placement = {
            "white": 0,
            "red": 1,
            "orange": 2,
            "yellow":3,
            "green": 4,
            "blue": 5,
            "purple": 6,
            "pink": 7,
            "brown": 8,
            "gray": 9,
            "beige": 10,
            "olive": 11,
            "navy": 12,
            "teal": 13,
            "lavender": 14,
            "turquoise": 15,
            "coral": 16,
            "magenta": 17,
            "crimson": 18,
            "violet": 19}
    couleur_choisie = dico_couleurs_choisies[signal]
    y1 = dico_placement[couleur_choisie]
    y2 = dico_placement[couleur_choisie]
    return y1,y2,couleur_choisie
        


def visuel_multi(fichier_choisie):
    dico_couleurs_choisies = algo_welsh(fichier_choisie)
    # initialisation de la figure
    fig, ax = plt.subplots()
    # boucle sur chaque segment à dessiner
    for signal,couleur in dico_couleurs_choisies.items():
        # récupération des coordonnées du segment
        x1,x2 = coordonnées_x(fichier_choisie,signal)
        y1,y2,couleur_choisie = coordonnées_y(fichier_choisie,signal)
        # dessin du segment
        ax.plot([x1, x2], [y1, y2], lw=10, color=couleur_choisie)
    # affichage de la figure
    plt.show()


