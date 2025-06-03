def recherche_nombre_premier_jusque_n(n):
    """
    Recherche les nombres premiers jusqu'à n.
    """
    
    if n < 2: # Pas de nombre premier avant 2
        return []

    premiers = []
    for nombre in range(2, n + 1):
        est_premier = True
        for i in range(2, int(nombre**0.5) + 1): # On teste jusqu'à la racine carrée du nombre
            if nombre % i == 0:
                est_premier = False
                break
        if est_premier:
            premiers.append(nombre)
    
    return premiers

print(recherche_nombre_premier_jusque_n(100))  # Exemple d'utilisation