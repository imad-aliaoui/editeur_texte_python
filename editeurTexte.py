import tkinter as tk
from tkinter import filedialog

# Configuration par défaut de la police et la taille du texte
police_actuelle = "Arial" 
taille_actuelle = 12     

# Fonction pour ouvrir une boîte de dialogue et sauvegarder le contenu dans un fichier
def sauvegarder():
    contenu = zone_texte.get("1.0", "end-1c")  # Récupère tout le texte dans la zone de texte
    chemin_fichier = filedialog.asksaveasfilename(defaultextension=".txt")  # Ouvre une boîte de dialogue pour choisir l'emplacement
    if chemin_fichier:  # Si un fichier a été sélectionné
        with open(chemin_fichier, "w+") as fichier:  # Ouvre le fichier en mode écriture
            fichier.write(contenu)  # Écrit le contenu

# Fonction pour changer la police du texte
def changer_police(nouvelle_police):
    global police_actuelle
    police_actuelle = nouvelle_police
    mettre_a_jour_style()

# Fonction pour changer la taille du texte
def changer_taille(nouvelle_taille):
    global taille_actuelle 
    taille_actuelle = nouvelle_taille 
    mettre_a_jour_style() 

# Fonction pour appliquer les modifications
def mettre_a_jour_style():
    zone_texte.config(font=(police_actuelle, taille_actuelle))

# Fenêtre de l'application
fenetre = tk.Tk()  # Crée une fenêtre 
fenetre.title("Éditeur de texte")  # Définit le titre de la fenêtre

# Zone de texte où l'utilisateur peut écrire
zone_texte = tk.Text(fenetre, wrap="word", font=(police_actuelle, taille_actuelle))
zone_texte.grid(row=0, column=0, columnspan=3, sticky="nsew")  # `sticky="nsew"` permet à la zone de texte de s'étirer dans toutes les directions

# Bouton pour sauvegarder
bouton_sauvegarder = tk.Button(fenetre, text="Enregistrer", command=sauvegarder)
bouton_sauvegarder.grid(row=1, column=0, sticky="ew")  # `sticky="ew"` étire le bouton horizontalement

# Menu pour choisir la police
menu_police = tk.Menubutton(fenetre, text="Police")  # Bouton de menu déroulant pour les polices
menu_police.grid(row=1, column=1, sticky="ew")  # Place le menu dans la grille
menu_police.menu = tk.Menu(menu_police, tearoff=0)  # Crée un menu déroulant
menu_police["menu"] = menu_police.menu
for police in ["Arial", "Times New Roman", "Courier New", "Verdana", "Helvetica"]:
    menu_police.menu.add_command(label=police, command=lambda p=police: changer_police(p))

# Menu pour choisir la taille
menu_taille = tk.Menubutton(fenetre, text="Taille") 
menu_taille.grid(row=1, column=2, sticky="ew")  
menu_taille.menu = tk.Menu(menu_taille, tearoff=0)  
menu_taille["menu"] = menu_taille.menu
for taille in list(range(12, 100, 4)): 
    menu_taille.menu.add_command(label=str(taille), command=lambda t=taille: changer_taille(t))

# Paramétrage de la grille pour lorsqu'on la redimensionne
fenetre.grid_rowconfigure(0, weight=1)  # La première ligne peyt s'étirer en hauteur
fenetre.grid_columnconfigure(0, weight=1)  # La première colonne peut s'étirer en largeur
fenetre.grid_columnconfigure(1, weight=0)  # La deuxième et la troisième colonne ne s'étire pas
fenetre.grid_columnconfigure(2, weight=0) 

fenetre.mainloop()
