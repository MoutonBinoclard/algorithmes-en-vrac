import math

def fonction_position_angulaire(t): # En degrés
    """
    Definit la position angulaire en fonction du temps
    pour ensuite generer les voies 1 et 2 d'un codeur
    """

    return math.sin(t)*360  # On alterne entre vitesse positive et négative pour le fun

def generer_voies_codeur(t_ini, t_fin, pas_temps, nombre_fentes, position_capteur1=0, position_capteur2=):
    """
    Genere les voies 1 et 2 d'un codeur incrémental
    entre t_ini et t_fin avec un nombre de fentes donné
    On obtient deux liste de la forme suivante :
    v1 = [0, 0, 1, 0, 1, 0, ...]
    v2 = [0, 1, 0, 1, 0, 1, ...]
    Chaque liste contient les valeurs lues
    L'index i correspond à la valeur lue pour le temps t_ini + i * pas_temps
    """

    dephasage_angulaire_capteur = 2 * math.pi / nombre_fentes  # Dephasage angulaire entre les voies

    t = t_ini # Initialisation du temps
    while t <= t_fin:  # Tant que le temps est dans l'intervalle
        position_angulaire = fonction_position_angulaire(t)



def trouver_si_capteur_devant_fente(position_capteur, position_fente):
