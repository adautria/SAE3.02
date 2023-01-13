import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

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
    # On récupère les données à partir du fichier sélectionné
    lst_donnees = recup_donnees(fichier_choisie)
    # On initialise une liste de signaux et un graph
    lst_signaux = []
    G = nx.Graph()
    # Pour chaque signal dans les données, on ajoute un noeud au graph
    for signal in lst_donnees :
        G.add_node(signal[0])
        lst_signaux.append(signal[0])
    # Tant qu'il reste des signaux dans la liste des données
    while lst_donnees :
        # On sélectionne le premier signal de la liste
        signal_selec = lst_donnees[0]
        # On retire le signal de la liste
        lst_donnees.pop(0)  
        # Pour chaque signal restant à comparer
        for signal_compare in lst_donnees :
            # Si le signal sélectionné et le signal à comparer sont incompatibles, on passe au suivant
            if signal_selec[1][0]-10 > signal_compare[1][1] or signal_selec[1][1]+10 < signal_compare[1][0]:
                pass
            # Sinon, on ajoute une arête entre ces deux signaux dans le graph
            else:
                G.add_edge(signal_selec[0],signal_compare[0])
    # On retourne le graph final
    return G


#fonct
def algo_welsh (fichier_choisie):
    # Créer un graphique à partir du fichier de données d'incompatibilité
    G = cree_graph_incompatibilite(fichier_choisie)
    # Obtenir la liste des noeuds du graphique
    lst_noeuds = G.nodes()
    # Initialiser un dictionnaire pour enregistrer les couleurs choisies pour chaque noeud
    dico_couleurs_choisies = {}
    # Initialiser tous les noeuds à la couleur blanche
    for noeud in lst_noeuds:
        nx.set_node_attributes(G, {noeud: 'white'}, 'couleur')
    # Pour chaque noeud, obtenir la liste de ses voisins et les couleurs possibles
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
        # Marquer les couleurs utilisées par les voisins du noeud comme indisponibles
        for voisin in lst_voisins :
            couleur_du_voisin = G.nodes[voisin]['couleur']
            couleurs_possibles[couleur_du_voisin] = 1
        # Trouver la première couleur disponible dans la liste des couleurs possibles et l'attribuer au noeud
        for key,value in couleurs_possibles.items():
            if value == 0 :
                nx.set_node_attributes(G, {noeud: key}, 'couleur')
                dico_couleurs_choisies[noeud]=key
                break
    # Retourner le dictionnaire des couleurs choisies pour chaque noeud
    return dico_couleurs_choisies


# Fonction que dessine le graphe d'incompatibilité
def dessiner_graph(fichier_choisie):
    # On crée un graph à partir du fichier sélectionné
    G = cree_graph_incompatibilite(fichier_choisie)
    # On définit une disposition circulaire pour les noeuds du graph
    pos = nx.circular_layout(G)
    # On récupère les couleurs choisies pour chaque signal dans un dictionnaire
    dico_couleurs_choisies = algo_welsh(fichier_choisie)
    # Pour chaque signal et sa couleur dans le dictionnaire
    for signal,couleur in dico_couleurs_choisies.items():
        # On dessine chaque noeud du graph en utilisant la couleur choisie
        nx.draw_networkx_nodes(G,pos,node_color=couleur,node_size=700,nodelist=[signal])
    # On dessine les arêtes du graph
    nx.draw_networkx_edges(G,pos)
    # On ajoute les labels des noeuds du graph
    nx.draw_networkx_labels(G,pos) 
    # On affiche le graph
    plt.show()


def trouve_clique_min(fichier_choisie):
    # On crée un graph à partir du fichier sélectionné
    graph = cree_graph_incompatibilite(fichier_choisie)
    # On initialise une liste vide pour la clique maximale
    max_clique = []
    # Pour chaque noeud du graph
    for v in graph:
        # On initialise une liste vide pour la clique actuelle
        clique = []
        # On ajoute le noeud au début de la clique
        clique.append(v)
        # Pour chaque autre noeud du graph
        for u in graph:
            # Si tous les noeuds de la clique actuelle sont voisins du noeud u, on ajoute u à la clique
            if all(x in graph[u] for x in clique):
                clique.append(u)
        # Si la clique actuelle est plus grande que la clique maximale précédente, on met à jour la clique maximale
        if len(clique) > len(max_clique):
            max_clique = clique
    # On retourne la taille de la clique maximale
    return len(max_clique)


def nb_fibre (fichier_choisie):
    # On récupère le dictionnaire des couleurs choisies pour chaque signal
    lst = algo_welsh(fichier_choisie)
    # On calcule le nombre de couleurs différentes utilisées par l'algorithme de Welsh et Powell
    result_welsh = int(len(set(lst.values())))
    # On calcule la taille de la clique maximale dans le graph
    result_clique = int(trouve_clique_min(fichier_choisie))
    # Si le nombre de fibres nécessaires selon l'algorithme de Welsh et Powell est égal à la taille de la clique maximale
    if result_clique == result_welsh:
        # On retourne le nombre de fibres nécessaires au minimum
        return f"Un total de {result_welsh} fibres sont nécessaire au minimum "
    # Sinon, on retourne le nombre de fibres théoriquement nécessaire, compris entre la taille de la clique maximale 
    # et le nombre de couleurs utilisées par l'algorithme de Welsh et Powell
    else:
        return f"En théorie, entre {result_clique} et {result_welsh} fibres seront nécessaires"


def coordonnees_x(fichier_choisie,signal):
    # On récupère les données du fichier sélectionné
    lst_donnees = recup_donnees(fichier_choisie)
    # On récupère les coordonnées x1 et x2 du signal sélectionné dans la liste des données
    x1 = lst_donnees[signal-1][1][0]
    x2 = lst_donnees[signal-1][1][1]
    # On retourne les coordonnées x1 et x2
    return x1,x2
def coordonnees_y(fichier_choisie,signal):
    # On récupère le dictionnaire des couleurs choisies pour chaque signal
    dico_couleurs_choisies = algo_welsh(fichier_choisie)
    # On crée un dictionnaire associant à chaque couleur sa position sur l'axe y
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
    # On récupère la couleur choisie pour le signal sélectionné
    couleur_choisie = dico_couleurs_choisies[signal]
    # On définit y1 et y2 comme étant égaux à la position de la couleur choisie sur l'axe y
    y1 = dico_placement[couleur_choisie]
    y2 = dico_placement[couleur_choisie]
    # On retourne les coordonnées y1 et y2 ainsi que la couleur choisie pour le signal sélectionné
    return y1,y2,couleur_choisie
        

def visuel_multi(fichier_choisie):
    # On récupère le dictionnaire des couleurs choisies pour chaque signal
    dico_couleurs_choisies = algo_welsh(fichier_choisie)
    # On initialise la figure avec les dimensions 8,6 et l'axe
    fig, ax = plt.subplots(figsize=(12, 7))
    # Pour chaque signal et sa couleur dans le dictionnaire
    for signal,couleur in dico_couleurs_choisies.items():
        # On récupère les coordonnées x1, x2, y1, y2 et la couleur choisie pour le signal
        x1,x2 = coordonnees_x(fichier_choisie,signal)
        y1,y2,couleur_choisie = coordonnees_y(fichier_choisie,signal)
        # On dessine le segment sur l'axe
        ax.plot([x1, x2], [y1, y2], lw=10, color=couleur_choisie)
        # Ajout du numéro du signal sur le segment
        ax.text(((x1+x2)/2)-20, ((y1+y2)/2)-0.07, signal, fontsize=12)
    # On définit les labels des axes du graphique
    ax.set_xlabel('fréquence (Hz)')
    ax.set_ylabel('numéro de fibre')
    # On définit le format de l'axe y pour qu'il n'utilise que des nombres entiers
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    # On affiche la figure
    plt.show()


