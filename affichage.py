import networkx as nx
import matplotlib.pyplot as plt
from main import *
from tkinter import *


def w1():
    #tkinter fenetre
    w = Tk()
    w.title("Menu")
    w.geometry("900x680")
    w.minsize(480,300)
    w.config(background="#41B77F")

    #creer la frame gros bouton
    frame = Frame(w,bg="#41B77F")

    #ajouter texte
    title_ = Label(frame,text="Bienvenue sur notre pojet SAE3.02",font=("Courrier",45),bg="#41B77F")
    title_.pack() #affiche notre texte

    #ajouter 2eme texte
    title_ = Label(frame,text="cliquez sur l'option que vous choisissez",font=("Courrier",25),bg="#41B77F")
    title_.pack()

    #creer bouton affichant la second fenetre
    map_bouton = Button(frame,text="nombre de fibre nécésaire",font=("Courrier",35),command=w2,bg="#41B77F",fg="black")
    map_bouton.pack(pady=20,fill=X)

    #creer bouton  qui affiche le graph d'incompatibilité
    corr_b = Button(frame,text="Graphe d'incompatibilité",font=("Courrier",35),command=dessiner_graph,bg="#41B77F",fg="black")
    corr_b.pack(pady=20,fill=X)

    choix_b = Button(frame,text="choisir ses options ",font=("Courrier",35),command=None,bg="#41B77F",fg="black")
    choix_b.pack(pady=20,fill=X,side=BOTTOM)

    fermer = Button(w, text="tout fermer ", font=("Courrier", 25), command=exit, bg="#41B77F", fg="#41B77F")
    fermer.pack(pady=20, fill=X, side=BOTTOM)

    #activer laffichage (frame)
    frame.pack(expand=True)
    #afficher
    w.mainloop()



def w2():
    nb_filtre = algo_welsh
    w2 = Tk()
    w2.title("resultat")
    w2.geometry("900x680")
    w2.minsize(480, 300)
    w2.config(background="#41B77F")

    frame2= Frame(w2,bg="#41B77F")
    frame3= Frame(w2,bg="#34565F")

    title_ = Label(frame2, text="Bienvenue sur notre pojet SAE15", font=("Courrier", 45), bg="#41B77F")
    title_.pack(pady=20)
    title_ = Label(frame3, text= f"Ainsi, {nb_filtre()} fibres seront necessaire", font=("Courrier", 35), bg="#41B77F")
    title_.pack()
    fermer = Button(w2, text="tout fermer ", font=("Courrier", 25), command=exit, bg="#41B77F", fg="#41B77F")
    fermer.pack(pady=20, fill=X, side=BOTTOM)
    rtr = Button(w2, text="retour",font=("Courrier", 20), command=w1, bg="#41B77F", fg="#41B77F" )
    rtr.place(x=0, y=0)

    frame2.pack(side=TOP)
    frame3.pack(expand=True)
    w2.mainloop()

w1()