import networkx as nx
import matplotlib.pyplot as plt
from tkinter import *
from main import *
from cree_donnees import *
from tkinter import filedialog

fichier_choisie = 'donnees.txt'

# Première fenêtre qui est le menu de notre interface
def w1():
    global fichier_choisie
    # On crée une fenêtre Tkinter
    w1 = Tk()
    # On définit le titre de la fenêtre et ses dimensions
    w1.title("Menu")
    w1.geometry("900x680")
    w1.minsize(480,300)
    # On définit la couleur d'arrière-plan de la fenêtre
    w1.config(background="#2F3CAD")
    
    # Fonction pour passer à la fenêtre 2
    def aller_w2():
        w1.destroy()
        w2()
    # Fonction pour passer à la fenêtre 3
    def aller_w3():
        w1.destroy()
        w3()
    # Fonction pour importer un fichier
    def import_file():
        global fichier_choisie
        # On utilise une boîte de dialogue pour sélectionner un fichier
        fichier_choisie = filedialog.askopenfilename()
    
    # On crée un frame pour les gros boutons
    frame1= Frame(w1,bg="#2F3CAD")
    # On crée un frame pour les autres boutons
    frame = Frame(w1,bg="#2F3CAD")
    
    # On ajoute du texte à la fenêtre
    title_ = Label(frame1,text="Bienvenue sur notre projet SAE3.02",font=("Courrier",45),bg="#2F3CAD")
    title_.pack(side=TOP,) # On affiche le texte
    
    # On ajoute du texte à la fenêtre
    title_ = Label(frame,text="Choisissez une option parmi celles ci-dessous",font=("Courrier",25),bg="#2F3CAD")
    title_.pack()
    
    # On crée un bouton pour importer un fichier
    bouton_importerF = Button(frame,text="Choisissez un fichier à importer",font=("Courrier",30),command=import_file,bg="#2F3CAD",fg="black")
    bouton_importerF.pack(pady=10,fill=X)
    
    # On crée un bouton pour créer un fichier (renvoie vers la fenêtre 3)
    bouton_creefichier = Button(frame,text="Créez un fichier de données",font=("Courrier",30),command=aller_w3,bg="#2F3CAD",fg="black")
    bouton_creefichier.pack(pady=10,fill=X)

    # On crée un bouton pour afficher le graphe d'incompatibilité
    bout_graph = Button(frame,text="Graphe d'incompatibilités",font=("Courrier",30),command=lambda: dessiner_graph(fichier_choisie),bg="#2F3CAD",fg="black")
    bout_graph.pack(pady=10,fill=X)
    
    # On crée un bouton pour afficher la fenêtre 2
    bout_result = Button(frame,text="Nombre de fibres nécessaires",font=("Courrier",30),command=aller_w2,bg="#2F3CAD",fg="black")
    bout_result.pack(pady=10,fill=X)
    
    # On crée un bouton pour afficher le visuel du multiplexage
    bout_result = Button(frame,text="Visuel du multiplexage",font=("Courrier",30),command=lambda:visuel_multi(fichier_choisie),bg="#2F3CAD",fg="black")
    bout_result.pack(pady=10,fill=X)
    
    # On crée un bouton pour fermer toutes les fenêtres et arrêter le programme
    fermer = Button(w1, text="Tout fermer ", font=("Courrier", 25), command=exit, bg="#2F3CAD", fg="#2F3CAD")
    fermer.pack(pady=20, fill=X, side=BOTTOM)
    
    # On affiche les frames
    frame1.pack(expand=True)
    frame.pack(expand=True)
    # On affiche la fenêtre
    w1.mainloop()


# Fenetre de l'onglet 'nombre de fibres nécessaires'
def w2():
    # On crée la fenêtre 2
    w2 = Tk()
    w2.title("resultat du multiplexage")
    w2.geometry("900x680")
    w2.minsize(480, 300)
    w2.config(background="#2F3CAD")
    
    # On définit la fonction de retour à la fenêtre 1
    def retour_w2():
        w2.destroy()
        w1()
    
    # On crée les frames
    frame2= Frame(w2,bg="#2F3CAD")
    frame3= Frame(w2,bg="#2F3CAD")
    
    # On ajoute le titre de la fenêtre
    title_ = Label(frame2, text="Projet SAE3.02", font=("Courrier", 50), bg="#2F3CAD")
    title_.pack(pady=40)
    
    # On ajoute le titre du résultat du multiplexage
    titlet_ = Label(frame3, text= "Multiplexage", font=("Courrier", 35), bg="#2F3CAD")
    # On ajoute un séparateur
    titlea_ = Label(frame3, text= "-----------------------------------------------", font=("Courrier", 35), bg="#2F3CAD")
    # On ajoute le résultat du multiplexage
    titlebis_ = Label(frame3, text= nb_fibre(fichier_choisie), font=("Courrier", 35), bg="#2F3CAD")
    # On ajoute un séparateur
    titleb_ = Label(frame3, text= "-----------------------------------------------", font=("Courrier", 35), bg="#2F3CAD")
    # On affiche tous les éléments de la fenêtre
    titlet_.pack()
    titlea_.pack()
    title_.pack()
    titlebis_.pack()
    titleb_.pack()
    
    # On crée un bouton pour fermer toutes les fenêtres et le programme
    fermer = Button(w2, text="Tout fermer ", font=("Courrier", 25), command=exit, bg="#2F3CAD", fg="#2F3CAD")
    fermer.pack(pady=20, fill=X, side=BOTTOM)
    # On crée un bouton pour retourner à la fenêtre précédente
    rtr = Button(w2, text="Retour",font=("Courrier", 20), command=retour_w2, bg="#2F3CAD", fg="#2F3CAD" )
    rtr.place(x=0, y=0)
    # On affiche les frames
    frame2.pack(side=TOP)
    frame3.pack(expand=True)
    
    # On lance la boucle Tkinter pour afficher la fenêtre
    w2.mainloop()


def w3():
    # On crée une fenêtre Tk et définir son titre et ses dimensions
    w3 = Tk()
    w3.title("cree donnes")
    w3.geometry("900x680")
    w3.minsize(480, 300)
    w3.config(background="#2F3CAD")

    # On définie une fonction pour détruire w3 et ouvrir w1
    def retour_w3():
        w3.destroy()
        w1()
    # Fonction pour passer à la fenêtre 3
    def aller_w4():
        w3.destroy()
        w4()
    
    # On définie une fonction pour créer un fichier appelé "donnees.txt"
    # avec le nombre de signaux spécifié par l'utilisateur
    def donnes_f():
        nb_signaux = int(champ_saisie.get())
        cree_donnees_f(nb_signaux)
        afficher_donnees.pack()

    # On crée deux frames dans la fenêtre w3
    frame2 = Frame(w3, bg="#2F3CAD")
    frame3 = Frame(w3, bg="#2F3CAD")

    # On crée également un bouton pour créer le fichier "donnees.txt"
    title_ = Label(frame2, text="Créer un fichier 'donnees.txt'", font=("Courrier", 45), bg="#2F3CAD")
    title_bb = Label(frame2, text="---------------------------------------", font=("Courrier", 45), bg="#2F3CAD")
    # On affiche les titres que l'on a créé
    title_.pack(pady=15)
    title_bb.pack()

    # On crée un sous titres donnant les instructions
    title_ = Label(frame3, text= "Choisir le nombre de signaux voulus dans le fichier", font=("Courrier", 35), bg="#2F3CAD")
    titlebis_ = Label(frame3, text= "(entre 1 et 25)", font=("Courrier", 35), bg="#2F3CAD")
    # On crée un un champ de saisie permettant de saisir le nombre de signaux voulue dans le fichier
    champ_saisie = Entry(frame3, font=("Courrier", 25))
    # On crée un bouton permettant d'executer le script qui crée le fichier 'donnees.txt'
    cree_D = Button(frame3, text="Créer le fichier", font=("Courrier", 25), command=donnes_f, bg="#2F3CAD", fg="black")
    # On crée un bouton permettant d'executer le script qui crée le fichier 'donnees.txt'
    afficher_donnees = Button(frame3, text="afficher les données", font=("Courrier", 25), command=aller_w4, bg="#2F3CAD", fg="black")
    # On affiche tous les éléments de la fenêtre
    title_.pack()
    titlebis_.pack()
    champ_saisie.pack()
    cree_D.pack(pady=20)
    
    # On crée un bouton pour fermer toutes les fenêtres et le programme 
    fermer = Button(w3, text="Tout fermer ", font=("Courrier", 25), command=exit, bg="#2F3CAD", fg="#2F3CAD")
    fermer.pack(pady=20, fill=X, side=BOTTOM)
    # On crée un bouton pour retourner à la fenêtre précédente
    rtr = Button(w3, text="Retour", font=("Courrier", 20), command=retour_w3, bg="#2F3CAD", fg="#2F3CAD" )
    rtr.place(x=0, y=0)

    # On affiche les frames 
    frame2.pack(side=TOP)
    frame3.pack(expand=True)

    # On démarre la boucle principale
    w3.mainloop()


def w4():
    # On crée une fenêtre Tk et définir son titre et ses dimensions
    w4 = Tk()
    w4.title("affichage donnees")
    w4.geometry("900x680")
    w4.minsize(480, 300)
    w4.config(background="#2F3CAD")

    # On récupère les données du fichier choisi
    donnees = recup_donnees(fichier_choisie)

    # On définie une fonction pour détruire w4 et ouvrir w1
    def retour_w4():
        w4.destroy()
        w1()
    
    # On crée deux frames dans la fenêtre w4
    frame2 = Frame(w4, bg="#2F3CAD")

    # On crée un titre et l'affiche sur notre fenêtre
    # On crée également un bouton pour créer le fichier "donnees.txt"
    title_ = Label(frame2, text="Voici le contenu du fichier 'donnees.txt'", font=("Courrier", 45), bg="#2F3CAD")
    title_bb = Label(frame2, text="---------------------------------------", font=("Courrier", 45), bg="#2F3CAD")
    # On affiche les titres que l'on a créé
    title_.pack(pady=15)
    title_bb.pack()
    
    # On crée les labels pour les titres de colonne
    label1 = Label(w4,text='signal',font=("Courrier", 15), bg="#2F3CAD")
    label1.place(x=350, y=160)
    label2 = Label(w4, text='fréq min',font=("Courrier", 15), bg="#2F3CAD")
    label2.place(x=430, y=160)
    label3 = Label(w4, text='fréq max',font=("Courrier", 15), bg="#2F3CAD")
    label3.place(x=520, y=160)
    # On initialise la coordonnée y de notre premier widget de données à 190
    y1 = 190
    # On parcourt les données récupérées et on affiche chaque élément dans un label
    for k in donnees:
        label1 = Label(w4,text=k[0],font=("Courrier", 12), bg="#2F3CAD")
        label1.place(x=350, y=y1)
        label2 = Label(w4, text=k[1][0],font=("Courrier", 12), bg="#2F3CAD")
        label2.place(x=430, y=y1)
        label3 = Label(w4, text=k[1][1],font=("Courrier", 12), bg="#2F3CAD")
        label3.place(x=520, y=y1)
        # On incrémente la coordonnées y pour que la prochaine ligne soit écrite en dessous
        # de la ligne précédente 
        y1 += 16
    
    # On crée un bouton pour fermer toutes les fenêtres et le programme 
    fermer = Button(w4, text="Tout fermer", font=("Courrier", 25), command=exit, bg="#2F3CAD", fg="#2F3CAD")
    fermer.pack(pady=20, fill=X, side=BOTTOM)
    # On crée un bouton pour retourner à la fenêtre précédente
    rtr = Button(w4, text="Retour", font=("Courrier", 20), command=retour_w4, bg="#2F3CAD", fg="#2F3CAD" )
    rtr.place(x=0, y=0)

    # On affiche les frames 
    frame2.pack(side=TOP)

    # On démarre la boucle principale
    w4.mainloop()

# Lance l'affichage de la fenetre menu
w1()
