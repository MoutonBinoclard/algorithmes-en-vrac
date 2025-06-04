def lecture_fichier(fichier):
    """
    Lit le fichier (ici codeur.txt) et retourne les trois listes
    Chaque liste correspond à une colonne du fichier
    """
    temps, canal_a, canal_b = [], [], []
    with open(fichier, encoding="utf-8") as f:
        lines = f.readlines()

        # On saute les deux premières lignes d'en-tête
        for line in lines[2:]:
            if line.strip() == "": # Ligne vide, on la saute
                continue
            valeurs_ligne = line.strip().split('\t')
            if len(valeurs_ligne) != 3:
                continue
            temps.append(float(valeurs_ligne[0]))
            canal_a.append(float(valeurs_ligne[1]))
            canal_b.append(float(valeurs_ligne[2]))
    return temps, canal_a, canal_b

temps, canal_a, canal_b = lecture_fichier("codeur.txt")

# En regardant le fichier, on va se dire que l'état haut c'est plus que 2.5
# Et l'état bas c'est moins que 2.5
# (Le signal est pas mal, pas de valeur entre deux états)

