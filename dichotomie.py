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

def dichotomie(a, b, epsilon, f=fonction):
    """
    Methode de la dichotomie pour trouver une racine d'une fonction f
    """
    
    if a >= b:  # Vérification du sens de l'intervalle (a doit être inférieur à b)
        return "L'intervalle doit être dans le sens croissant."
    
    while abs(b - a) > epsilon:  # Tant que la précision n'est pas atteinte
        c = (a + b) / 2  # Point milieu
        
        if f(c) == 0:  # Si c est une racine
            return c
        
        elif f(a) * f(c) < 0:  # Si a et c sont de signes opposés, la racine est dans [a, c]
            b = c # On réduit l'intervalle à [a, c]

        else:  # Sinon la racine est dans [c, b]
            a = c # On reduit l'intervalle à [c, b]
            
    return (a + b) / 2  # Retourne le milieu de l'intervalle final

# Affichage de la courbe
tracer_courbe(0.5, 2, 0.01)  # On trace la courbe de f(x) entre 0 et 5 avec un pas de 0.1

# Test de la fonction
print(dichotomie(0.5, 2, 0.001))  # On cherche une racine de f(x) sur l'intervalle [0, 5] avec une précision de 0.001