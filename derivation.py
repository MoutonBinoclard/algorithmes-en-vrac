def fonction(x):
    return x**2 - 4*x + 3

def derivation(f, x, epsilon): # Calcul la dérivée en un point pour une précsion donnée
    return (f(x + epsilon/2) - f(x - epsilon/2)) / epsilon

def tracer_courbe_et_derivation(f, epsilon, debut, fin):
    """
    Trace la courbe et sa dérivée sur un intervalle donnée
    """
    
    import matplotlib.pyplot as plt
    
    valeur_de_x = []
    valeur_de_fx = []
    valeur_de_f_prime_x = []
    
    while debut <= fin: # Pour replir les listes valeur_de_x, fvaleur_de_x et valeur_de_f_prime_x
        valeur_de_x.append(debut)
        valeur_de_fx.append(f(debut))
        valeur_de_f_prime_x.append(derivation(f, debut, epsilon))
        debut += epsilon

    plt.plot(valeur_de_x, valeur_de_fx, label='f(x)')
    plt.plot(valeur_de_x, valeur_de_f_prime_x, label='f\'(x)', linestyle='--')
    plt.axhline(0, color='black', linewidth=2)  # Ligne horizontale
    plt.legend()
    plt.show()

# Test de la dérivation
tracer_courbe_et_derivation(fonction, 0.0001, 0, 5)  # On trace la courbe de f(x) et sa dérivée entre 0 et 5 avec un pas de 0.01