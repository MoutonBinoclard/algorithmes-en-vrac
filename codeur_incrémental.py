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

"""
On imagine cette forme pour le codeur

codeur b  codeur a
     \     /
      *****
   **       **     ^
  *           *    |   Sens de rotation direct
 *      x      *   |
  *           *    |
   **       **
      *****

"""

def codeur_incremental(temps, canal_a, canal_b, nombre_fentes, position_angulaire_initiale=0):
    """
    Fonction qui retourne la position du codeur en fonction du temps
    et des deux canaux A et B
    """
    position_angulaire = [position_angulaire_initiale]
    temps_passage =[temps[0]]  # On initialise avec le premier temps
    etat_a_precedent = canal_a[0] > 2.5
    etat_b_precedent = canal_b[0] > 2.5

    # Etat haut = True, état bas = False

    for index in range(1, len(temps)):
        etat_a_en_cours = canal_a[index] > 2.5
        etat_b_en_cours = canal_b[index] > 2.5

        if not etat_a_precedent and not etat_b_precedent and etat_a_en_cours and not etat_b_en_cours:
            # A monte en premier, sens direct
            position_angulaire.append(position_angulaire[-1] + 1)
            temps_passage.append(temps[index])

        elif not etat_a_precedent and not etat_b_precedent and etat_b_en_cours and not etat_a_en_cours:
            # B monte en premier, sens inverse
            position_angulaire.append(position_angulaire[-1] - 1)
            temps_passage.append(temps[index])

        etat_a_precedent = etat_a_en_cours
        etat_b_precedent = etat_b_en_cours
    
    # Convertir la le nombre de passage de fente en position angulaire
    position_angulaire = [p * (360 / nombre_fentes) for p in position_angulaire]
    return position_angulaire, temps_passage



position_angulaire, temps_passage=codeur_incremental(temps, canal_a, canal_b, nombre_fentes=20, position_angulaire_initiale=0)



import matplotlib.pyplot as plt
plt.plot(temps_passage, position_angulaire, label="Position du codeur")
plt.xlabel("Temps (s)")
plt.ylabel("Position angulaire (degrés)")
plt.title("Position angulaire du codeur incrémental")
plt.grid()
plt.show()

    