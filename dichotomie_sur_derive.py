def fonction(x):
    return x**2 - 4*x + 3

def tracer_courbe(a, b, pas, f=fonction):
    """
    Trace la courbe de la fonction f entre a et b avec un pas donné
    """
    
    import matplotlib.pyplot as plt
    
    x = []
    fx = []
    
    while a <= b:
        x.append(a)
        fx.append(f(a))
        a += pas
    
    plt.plot(x, fx)
    plt.axhline(0, color='black', linewidth=2)  # Ligne horizontale
    plt.show()


# Affichage de la courbe
tracer_courbe(0.5, 3, 0.01)  # On trace la courbe de f(x) entre 0 et 5 avec un pas de 0.1
# On observe un minimum vers 2


def dichotomie_sur_derive(a, b, epsilon, f=fonction):
    """
    Methode de la dichotomie pour trouver l'extremum d'une fonction f
    sur un intervalle [a, b] avec une précision epsilon.
    On utilise la dérivée de la fonction pour trouver le minimum.
    """

    if a >= b:  # Vérification du sens de l'intervalle (a doit être inférieur à b)
        return "L'intervalle doit être dans le sens croissant."
    
    
    derivée_a = (f(a + epsilon) - f(a)) / epsilon
    derivée_b = (f(b) - f(b - epsilon)) / epsilon
    
    if derivée_a * derivée_b > 0 : # Derivée de même signe -> pas ou minium 2 extremums
        return "L'intervalle ne contient pas d'extremum."
    
    while abs(b - a) > epsilon:  # Tant que la précision n'est pas atteinte
        
        derivée_a = (f(a + epsilon) - f(a)) / epsilon
        
        c = (a + b) / 2  # Point milieu
        derivée_c = (f(c + epsilon/2) - f(c - epsilon/2)) / epsilon

        if derivée_c == 0:  # Si c est un extremum
            return c
        
        elif derivée_a * derivée_c < 0:  # Si a et c sont de signes opposés, l'extremum est dans [a, c]
            b = c

        else:  # Sinon l'extremum est dans [c, b]
            a = c

    return (a + b) / 2  # Retourne le milieu de l'intervalle final

# Test de la fonction
print(dichotomie_sur_derive(0.5, 3, 0.001))  # On cherche un extremum de f(x) sur l'intervalle [0, 5] avec une précision de 0.001
