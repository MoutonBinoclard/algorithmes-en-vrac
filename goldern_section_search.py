# Golden-section search
# Algorithme permettant de trouver le minimum d'une fonction continue sur un intervalle donné

import math 

phi = (1 + math.sqrt(5)) / 2  # Nombre d'or

def f(x): # On met une fonction dont on cherche le minimum
    return 0.2*x**3 - 6*x + 8

def methode_du_nombre_dor(a, b, epsilon): # a et b borne de l'intervalle dans le sens croissant, epsilon la précision de l'intervalle

    if a >= b: # Verification de l'intervalle
        return "L'intervalle doit être dans le sens croissant."
    
    # Initialisation des points intérieurs
    c = b + (a - b) / phi
    d = a + (b - a) / phi
    
    while abs(b - a) > epsilon: # Tant que la precision n'est pas atteinte :
        
        if f(c) < f(d): # Si f(x) est plus petit que f(d), d devient le nouveau b
            b = d
        else: # Sinon c devient le nouveau a
            a = c
        
        # On met ensuite à jour les points c et d
        c = b - (b - a) / phi
        d = a + (b - a) / phi
    
    return (a + b) / 2  # On retourne le millieu de l'intervalle final

# Test de la fonction
# Ps : Après étude, on sait que cette fonction n'admet qu'un minimum sur l'intervalle [0, 5]
print(methode_du_nombre_dor(0, 5, 0.001))  # On cherche le minimum de f(x) sur l'intervalle [0, 5] avec une précision de 0.001
# On obtient environ 3.16, ce qui effictivement le mininum de la fonction f sur cet intervalle