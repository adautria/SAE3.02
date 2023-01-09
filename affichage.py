import networkx as nx
import matplotlib.pyplot as plt
from tkinter import *
from main import *
from cree_donnees import *
from tkinter import filedialog

fichier_choisie = 'donnees.txt'

def w1():
    #tkinter fenetre
    w1 = Tk()
    w1.title("Menu")
    w1.geometry("900x680")
    w1.minsize(480,300)
    w1.config(background="#2F3CAD")
    def aller_w2():
        w1.destroy()
        w2()
    def aller_w3():
        w1.destroy()
        w3()
    def import_file():
        global fichier_choisie
        # Ouvrir une boîte de dialogue pour sélectionner le fichier
        fichier_choisie = filedialog.askopenfilename()
    #creer la frame gros bouton
    frame = Frame(w1,bg="#2F3CAD")

    #ajouter texte
    title_ = Label(frame,text="Bienvenue sur notre projet SAE3.02",font=("Courrier",45),bg="#2F3CAD")
    title_.pack() #affiche notre texte

    #ajouter 2eme texte
    title_ = Label(frame,text="cliquez sur l'option que vous choisissez",font=("Courrier",25),bg="#2F3CAD")
    title_.pack()

    #bouton d'importation de fichier
    bouton_importerF = Button(frame,text="Choisissez un fichier a importer",font=("Courrier",30),command=import_file,bg="#2F3CAD",fg="black")
    bouton_importerF.pack(pady=10,fill=X)

    #boutoun de creation du fichier ( renvoi vers seconde fenetre)
    bouton_creefichier = Button(frame,text="Cree un fichier de donnes",font=("Courrier",30),command=aller_w3,bg="#2F3CAD",fg="black")
    bouton_creefichier.pack(pady=10,fill=X)

    #creer bouton  qui affiche le graph d'incompatibilité
    bout_graph = Button(frame,text="Graphe d'incompatibilité",font=("Courrier",30),command=lambda: dessiner_graph(fichier_choisie),bg="#2F3CAD",fg="black")
    bout_graph.pack(pady=10,fill=X)

    #creer bouton affichant la second fenetre
    bout_result = Button(frame,text="Nombre de fibre nécéssaire",font=("Courrier",30),command=aller_w2,bg="#2F3CAD",fg="black")
    bout_result.pack(pady=10,fill=X)

    #creer bouton pour le visuel des fibres
    bout_result = Button(frame,text="visuel du multiplexage",font=("Courrier",30),command=visuel_multi,bg="#2F3CAD",fg="black")
    bout_result.pack(pady=10,fill=X)

    #bouton de fermeture des fenetre et du programme
    fermer = Button(w1, text="tout fermer ", font=("Courrier", 25), command=exit, bg="#2F3CAD", fg="#2F3CAD")
    fermer.pack(pady=20, fill=X, side=BOTTOM)

    #activer laffichage (frame)
    frame.pack(expand=True)
    #afficher
    w1.mainloop()



def w2():
    nb_filtre = algo_welsh
    w2 = Tk()
    w2.title("resultat")
    w2.geometry("900x680")
    w2.minsize(480, 300)
    w2.config(background="#2F3CAD")
    def retour_w2():
        w2.destroy()
        w1()

    frame2= Frame(w2,bg="#2F3CAD")
    frame3= Frame(w2,bg="#2F3CAD")

    title_ = Label(frame2, text="Projet SAE15", font=("Courrier", 50), bg="#2F3CAD")
    title_.pack(pady=40)
    titlet_ = Label(frame3, text= "Multiplexage", font=("Courrier", 35), bg="#2F3CAD")
    titlea_ = Label(frame3, text= "-----------------------------------------------", font=("Courrier", 35), bg="#2F3CAD")
    titlebis_ = Label(frame3, text= nb_fibre(fichier_choisie), font=("Courrier", 35), bg="#2F3CAD")
    titleb_ = Label(frame3, text= "-----------------------------------------------", font=("Courrier", 35), bg="#2F3CAD")
    titlet_.pack()
    titlea_.pack()
    title_.pack()
    titlebis_.pack()
    titleb_.pack()
    fermer = Button(w2, text="tout fermer ", font=("Courrier", 25), command=exit, bg="#2F3CAD", fg="#2F3CAD")
    fermer.pack(pady=20, fill=X, side=BOTTOM)
    rtr = Button(w2, text="retour",font=("Courrier", 20), command=retour_w2, bg="#2F3CAD", fg="#2F3CAD" )
    rtr.place(x=0, y=0)

    frame2.pack(side=TOP)
    frame3.pack(expand=True)
    w2.mainloop()

def w3():
    nb_filtre = algo_welsh
    w3 = Tk()
    w3.title("cree donnes")
    w3.geometry("900x680")
    w3.minsize(480, 300)
    w3.config(background="#2F3CAD")
    def retour_w3():
        w3.destroy()
        w1()
    def donnes_f():
        nb_signaux = int(champ_saisie.get())
        cree_donnees_f(nb_signaux)
        retour_w3()
    
    frame2= Frame(w3,bg="#2F3CAD")
    frame3= Frame(w3,bg="#2F3CAD")

    title_ = Label(frame2, text="Crée de fichier de données de la taille que vous souhaitez", font=("Courrier", 45), bg="#2F3CAD")
    title_.pack(pady=20)
    title_ = Label(frame3, text= "Choisir le nombres de signaux voulu dans le fichier", font=("Courrier", 35), bg="#2F3CAD")
    titlebis_ = Label(frame3, text= "(entre 1 et 25)", font=("Courrier", 35), bg="#2F3CAD")
    champ_saisie = Entry(frame3, font=("Courrier", 25))
    cree_D = Button(frame3,text="Creer le fichier",font=("Courrier",25),command=donnes_f,bg="#2F3CAD",fg="black")
    title_.pack()
    titlebis_.pack()
    champ_saisie.pack()
    cree_D.pack(pady=20,fill=X)
    
    fermer = Button(w3, text="tout fermer ", font=("Courrier", 25), command=exit, bg="#2F3CAD", fg="#2F3CAD")
    fermer.pack(pady=20, fill=X, side=BOTTOM)
    rtr = Button(w3, text="retour",font=("Courrier", 20), command=retour_w3, bg="#2F3CAD", fg="#2F3CAD" )
    rtr.place(x=0, y=0)

    frame2.pack(side=TOP)
    frame3.pack(expand=True)
    w3.mainloop()


w1()
