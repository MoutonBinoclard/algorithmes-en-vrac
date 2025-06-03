import math
import matplotlib.pyplot as plt

def fonction(x):
    return math.exp(-x) + math.sin(2 * x)

def liste_fonction(a, b, pas, f=fonction):
    """
    Génère la liste des valeur f(x) et liste des x correspondants
    forme :
    x = [x1, x2, ..., xn]
    fx = [f(x1), f(x2), ..., f(xn)]
    """

    x = []
    fx = []
    while a <= b:
        x.append(a)
        fx.append(f(a))
        a += pas
    return x, fx

def tracer_courbe(a, b, pas, f=fonction):
    """
    Trace la courbe de la fonction f entre a et b avec un pas donné
    Avec le plus d'argument possible pour personnaliser le graphique
    """

    x, fx = liste_fonction(a, b, pas, f)

    plt.figure(figsize=(10, 5)) # Taille de la figure

    plt.plot(x, fx, label="f(x)", color='#abcabc', marker='o', markersize=3, linestyle='None')
    # color = couleur de la courbe
    # marker = marqueur pour les points
    # markersize = taille des marqueurs
    # linestyle = 'None' pour ne pas relier les points par une ligne, sinon on peut mettre '-' pour une ligne continue, '--' pour une ligne pointillée, etc.

    plt.title(f"Courbe de f entre {a} et {b}", fontweight='bold', fontstyle='italic',fontsize=18) # Titre
    # Fontweight = Poids de la police : 'normal', 'bold', 'light', etc.
    # Fontstyle = Style de la police : 'normal', 'italic', 'oblique', etc.
    # Fontsize = Taille de la police


    plt.xlabel("x", color='#4373CE') # Axe des abscisses
    plt.ylabel("y", color="#4373CE") # Axe des ordonnées
    
    plt.grid(True, color='#888888') # Affiche la grille avec une couleur

    plt.axhline(0, color='#333333', linewidth=2)
    plt.axvline(0, color='#333333', linewidth=2)
    #axhline pour la ligne horizontale, axvline pour la verticale
    # linewidth pour l'épaisseur de la ligne (1 est la valeur par défaut)
    
    plt.xlim(a, b) # Limites de l'axe des abscisses
    plt.ylim(min(fx) - 0.5, max(fx) + 0.5) # Limites de l'axe des ordonnées

    plt.gca().set_facecolor("#B1996E")  # Fond du plot = fond de la courbe
    plt.gcf().patch.set_facecolor("#D6CFB2")  # Fond de la figure = contour

    plt.legend() # Affiche la légende, il faut mettre un label dans les courbes pour que ça marche bien
    plt.show() # Montrer le graphique


tracer_courbe(-1, 10, 0.1)