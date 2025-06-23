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


# On imagine cette forme pour le codeur

# codeur b  codeur a
#     \     /
#       *****
#    **       **     ^
#   *           *    |   Sens de rotation direct
#  *      x      *   |
#   *           *    |
#    **       **
#       *****


# PRECISION SIMPLE

def codeur_incremental_precision_simple(temps, canal_a, canal_b, nombre_fentes, position_angulaire_initiale=0):
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

# Code avec moins de lignes, et plus sexy
def codeur_incremental_precision_simple_avec_moins_de_lignes_de_codes_bla_bla_bla(temps, canal_a, canal_b, nombre_fentes, position_angulaire_initiale=0):
    etats = [(a > 2.5, b > 2.5) for a, b in zip(canal_a, canal_b)]
    position_angulaire, temps_passage = [position_angulaire_initiale], [temps[0]]
    for i in range(1, len(etats)):
        if etats[i-1] == (False, False):
            if etats[i] == (True, False):
                position_angulaire.append(position_angulaire[-1] + 1)
                temps_passage.append(temps[i])
            elif etats[i] == (False, True):
                position_angulaire.append(position_angulaire[-1] - 1)
                temps_passage.append(temps[i])
    position_angulaire = [p * (360 / nombre_fentes) for p in position_angulaire]
    return position_angulaire, temps_passage





# PRECISION DOUBLE

def codeur_incremental_precision_double(temps, canal_a, canal_b, nombre_fentes, position_angulaire_initiale=0):
    """
    Fonction qui retourne la position du codeur en fonction du temps
    et des deux canaux A et B
    """
    position_angulaire = [position_angulaire_initiale]
    temps_passage = [temps[0]]  # On initialise avec le premier temps
    etat_a_precedent = canal_a[0] > 2.5
    etat_b_precedent = canal_b[0] > 2.5

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

        # On regarde aussi les fronts descendants

        elif etat_a_precedent and etat_b_precedent and not etat_a_en_cours and etat_b_en_cours:
            # A descend en premier, sens direct
            position_angulaire.append(position_angulaire[-1] + 1)
            temps_passage.append(temps[index])

        elif etat_a_precedent and etat_b_precedent and not etat_b_en_cours and etat_a_en_cours:
            # B descend en premier, sens inverse
            position_angulaire.append(position_angulaire[-1] - 1)
            temps_passage.append(temps[index])

        etat_a_precedent = etat_a_en_cours
        etat_b_precedent = etat_b_en_cours
    
    # Convertir la le nombre de passage de fente en position angulaire
    position_angulaire = [p * (180 / nombre_fentes) for p in position_angulaire] # 180 degrés car on regarde aussi les fronts descendants
    return position_angulaire, temps_passage





# PRECISION QUATRE

def codeur_incremental_precision_4(temps, canal_a, canal_b, nombre_fentes, position_angulaire_initiale=0):
    etats = [(a > 2.5, b > 2.5) for a, b in zip(canal_a, canal_b)]
    position_angulaire, temps_passage = [position_angulaire_initiale], [temps[0]]
    for i in range(1, len(etats)):
        # Augmentation
        if etats[i-1] == (False, False) and etats[i] == (True, False):
            position_angulaire.append(position_angulaire[-1] + 1)
            temps_passage.append(temps[i])
        if etats[i-1] == (True, False) and etats[i] == (True, True):
            position_angulaire.append(position_angulaire[-1] + 1)
            temps_passage.append(temps[i])
        if etats[i-1] == (True, True) and etats[i] == (False, True):
            position_angulaire.append(position_angulaire[-1] + 1)
            temps_passage.append(temps[i])
        if etats[i-1] == (False, True) and etats[i] == (False, False):
            position_angulaire.append(position_angulaire[-1] + 1)
            temps_passage.append(temps[i])
        # Diminution
        if etats[i-1] == (False, False) and etats[i] == (False, True):
            position_angulaire.append(position_angulaire[-1] - 1)
            temps_passage.append(temps[i])
        if etats[i-1] == (False, True) and etats[i] == (True, True):
            position_angulaire.append(position_angulaire[-1] - 1)
            temps_passage.append(temps[i])
        if etats[i-1] == (True, True) and etats[i] == (True, False):
            position_angulaire.append(position_angulaire[-1] - 1)
            temps_passage.append(temps[i])
        if etats[i-1] == (True, False) and etats[i] == (False, False):
            position_angulaire.append(position_angulaire[-1] - 1)
            temps_passage.append(temps[i])
    position_angulaire = [p * (90 / nombre_fentes) for p in position_angulaire]
    return position_angulaire, temps_passage


def codeur_incremental_precision_4_moins_de_lignes(temps, canal_a, canal_b, nombre_fentes, position_angulaire_initiale=0):
    etats = [(a > 2.5, b > 2.5) for a, b in zip(canal_a, canal_b)]
    position_angulaire, temps_passage = [position_angulaire_initiale], [temps[0]]
    for i in range(1, len(etats)):
        if etats[i-1] != etats[i]: # Changement d'état
            if (etats[i-1][0] != etats[i][0] and etats[i-1][0] == etats[i][1]) or \
               (etats[i-1][1] != etats[i][1] and etats[i-1][1] != etats[i][0]):
                position_angulaire.append(position_angulaire[-1] + 1)
                temps_passage.append(temps[i])
            else: # Diminution
                position_angulaire.append(position_angulaire[-1] - 1)
                temps_passage.append(temps[i])
    position_angulaire = [p * (90 / nombre_fentes) for p in position_angulaire]
    return position_angulaire, temps_passage




position_angulaire_simple, temps_passage_simple = codeur_incremental_precision_simple(temps, canal_a, canal_b, 20)
position_angulaire_double, temps_passage_double = codeur_incremental_precision_double(temps, canal_a, canal_b, 20)
position_angulaire_simple_bla_bla, temps_passage_simple_bla_bla = codeur_incremental_precision_simple_avec_moins_de_lignes_de_codes_bla_bla_bla(temps, canal_a, canal_b, 20)
position_angulaire_4, temps_passage_4 = codeur_incremental_precision_4(temps, canal_a, canal_b, 20)
position_angulaire_4_moins_de_lignes, temps_passage_4_moins_de_lignes = codeur_incremental_precision_4_moins_de_lignes(temps, canal_a, canal_b, 20)


import matplotlib.pyplot as plt
plt.plot(temps_passage_simple, position_angulaire_simple, label="Position du codeur (simple)")
plt.plot(temps_passage_double, position_angulaire_double, label="Position du codeur (double)")
plt.plot(temps_passage_simple_bla_bla, position_angulaire_simple_bla_bla, label="Position du codeur (simple avec moins de lignes de code)", linestyle='--')
plt.plot(temps_passage_4, position_angulaire_4, label="Position du codeur (quatre)", linestyle=':')
plt.plot(temps_passage_4_moins_de_lignes, position_angulaire_4_moins_de_lignes, label="Position du codeur (quatre avec moins de lignes de code)", linestyle='-.')
plt.xlabel("Temps (s)")
plt.ylabel("Position angulaire (degrés)")
plt.title("Position angulaire du codeur incrémental")
plt.legend()
plt.grid()
plt.show()






































# Ajout d'un truc sexy, pour rendre le code plus stylé
"""
#####==########+=++++++++++*####***********************#*++++++++-=*****#%%%%%%%%%##*******###%%%%%%
####-+########+=+++++++++++*#####**********************#*+++++++++--###%%%%%%%%#+==++++++++++++*#%%%
###-*########=+++++++++*+++*%####**********++++==*****##****+*+****--%%%%%%%%*++++++***++++++*++++#%
#*-*#######*=+++++++++*#+++#%#####****#*****++======*###*++**++*****%%%%%%%+++*++++***++++++*+++*++*
*=########*=+++++++++###+++#%#####**####*****+==-----=##*++*%#****#%%%%%%**+++++*****++++++*+++*****
=########*=+++++++++#%##*++#%#####*###******+====------**++*%%*==#%%%%%#*+++++++*****=++++++++******
########*++++++++++#%###*++#%#####+###****+++=====--=---+++**=---#%%%%#*++++++******+++++++++*******
#######+++++++++++######+++*%####*+###****+++++=+==========---==-%%%%**+++++++*****+++++++++********
######++*++++++++#######*++*%####*+**#*****+++++++++++=====--=***%%%*++++++++****#+++++++++*********
*####++*+++++++*########+++*%####*-+*#******#####%%*=======*#*+#%%%*++++++++****#+++++**++**********
*##*++++++++++**########*++*%#####+=*****##%%%%%%#+=====+##*+#%%%%#*+++++++****#*++++***+***********
*#*++++++++++***########*++*%######-*#*#%%%%%%%#*++++=---#%*%%%%%#*++++++++***#*++*****+************
**++++++++++****########*++*%#####****#%%%%%%#*+++++==---+%##%%%%*++++*********+++****++************
++**+++++++******#######*++*%####*+##%%%%%%%#+=*####*+=+##%%#%%%**++++++*****#*++*******************
++++++++++*******######%*++*%###*+%%%%#%%%%#=+**#*+**+=**%%%*%%#*+++++***+========+*****************
+++++++++*+++++**#####%%*++*##*#%%#%%%##%%*=#**+==++*+-+*#%%*%%*+++****===-----------+*************+
++++++++**+++****###%%%%*++*%###%%#%%%##%#+%#**++++***-+*#%%*%#*++****==--------------=*************
+++++++**********###%%%%*+++####%%##%%###*%%#**++++**+=*#%%%##*++****+------------======+====--=****
+++++***********##%%%%%%*+++###%%%%###+*%%%%##**+***+++*%%%%%*+++****=--------==++*******++++===+***
++++*#*********####%%%%%*+=+%#%%%####**%%%%%%%#********%%%%%%++++****--------+#%%%%%%%%%%%*+====****
++*******#*****##*+*%%%#*+++%%%%%#%#*#%%%%%%%%%%#**++*%%%%%%%+*******----+#%%%%%%#%%%%%%%%%#+==*****
++********###*#%#*==*#%%#+++#%%%%%#####%%%%%%%%****++====*%%%+***###*--+#%%##%%%#%%#%%%%%%%#+=***#**
+**********#**#%#*=+%%*##+++*%%%%%%%##*##%%%%#%****++===--=%#******+=-+#####%%%%%%%#%%%%##%++****#**
+**********#++*%##++%%#*%+++#%%%%%%%%####%%%#*#****++++=---=#******--=#####%%%%%%%%%#%%##%#+********
+**********#%#%%%#*+%%#*%+++#%%%%%%%%###%%%%*##*****+++==---*#*****+-*#####%%%%%%%#%#%###%#*********
+**********###%%%%%+#%#+#+++#%%%%%%%%##%%%%###***+***+++==--=##%%%==*%%#%#%%%*%%%%%%#%#####*********
***********###%%*+##%%#+#+++%%%%%%%%%%#%%%%#****+++++++++==--*#####%%%%%#%%%#+%%%%#%%%#####*********
**##**#****#####****%%%=*+++%%%%%%#%%%%%%#*******++++++++==---##***#%%##%%##*+%%%##%%#####**********
*############%###*=+*#%*%+++#%%##%%%%%%##***********+++++===--****#%%%%%#*+*+#%%%%#%%###%#**********
*#%%%%%%%%%%#%%%****+**#%+++*#%%%%%%%%##*******+++*#**+++===---=*****++===+++%%%%%#%%###%#*++++++***
##%%%%%%%%%%%%##**+=:=*%%+++#*##%%#*#*#*******+++++****+++===----=====-=+++++#%%%%#%###%##++++++****
#####%%%%%%%%%%####*+*###+++#*+*==+#++********+++++*#***++++==-=---=**+****++*#%%%%%#%%%#+-=+++*****
====+++++++++++++++++++++++++++==-=++=##******++++++*#***+++=====--=******#**++%%%%#%####=--++******
==+++++++++++++++++++++++++++++++=:-=-=*#*****++++++**#***++++=====*******##***#%%#*+#%*=====*#****+
+++++********************#########=::::=+*****+++++++*#***+++++===+***+**************++==+====#***+*
++++++++++++************##********==:::-=+*****+++++++*#****++++===*****************++===++===******
++++++++++******##*#***++++*****+*++=:::-=+*****+++++++*#****++++==+*******#****+++**+====++==+#***+
+++++++++*********+++++++++*+=-:--:+*-:-::=+*****++++++**#****++++=+*##***###*****++++++===++==**+++
=+++++++****#**++++++===::........:+**=:-::=********++++**#***+++++=+******#********+++*+++++==+*+++
-++++++***#*+++=---::.............:+***+:--:=********+++***#****+++++***#***#*********++****++++++++
=++++++**+++++-:..................:+*+***---:-*************#****++++++****#***#*******++=+**++++++++
=++++**+++==-:............:::::::..=*+***#+:-:-*************#*****++++*****#**##********+++**+++++++
+++***+==-.............::::........-*++***%*-::-************#*******+++**#*****#**********+*#**+++++
++**+++-............::.............:**++***##-::-+***********#*******++*******####*********+*#*+++++
**++++-............:...:............+**+*****#-:---+*********#********++#*#*#*####*#**##****##***+++
*+++=:.........::......:............-*******##*::---**********#********+****######*##**#****#%#**+++
+++=................................:+******#*#:--:-+******+**##*******+**#*#####**#*####***###**+++
++=.........:.........................-+******#--::=*******++++#********+*########***####***###***++
==:.......:...........................:=*******::--+******++++++#*******+**####################***+*
=:.......:......:......:............:..=++****-:-=*****++++++++++#*********#####%#############****+*
-::....-::::::::::...::::..............-+++*#=-=+****++++++++++++*#**+*++++######################***
::::.:-:::::...........:...............:+++=--+*****++++++++++++++****+*+++####################*****
:::.:-:::::::...............::::.......-+==-=***++++++++++++++++++*#***+++*###############%##****#**
..::-=-::::.::...::.:.:....::::........-++-=***+++++++++++++++++***%#*****#%#%############%%####****
...:-:.:::::::..:::--:::..:::=-:.....:=**-+*****++++++++++++++*****%%%##*###%%%###########%%%%#%%#**
.::--::.......:::::--::-:.:--::::...:=*#:=******+++++++++++++*****###*##**##%%%##%%#######%%####%%#*
--====----=------=-----=-----:::--::-*#=-*******+++++++++++*******##***#*###%%%%%%%#%##%##%######***
-.--::.........::......:...........:=##:=***********+++++*********###****#%%%%%%%%%#%#####%##%%#****
=.--:-+#+.........................:-*##:=*************************####***###%%%%%%%%%%#%%%%%%%%%#***
=:=*####*-.::..........:..........-+###==************************##%#****###%%%%%%%%%%%%%%%%%%%%##**
==#***#***======--::---=----::::::=*####-+#*********************###%#####*#%%%%%%%%%%%%%%%%%%%%%##**
+=*****##*+#*++=+=---%%%%%%%%%%%%*=######=*###*****************####%#####***###%%%%%%%%%%%%%%%%###**
+=***#**##**#****++=-#%%%%%%%%%%%%+*######+*###***************###########*#####%%%%%%%%%%%%%%%%%##**
+=****#**##*#********%%%%%%%%%%%%%%-######%**###**************##############%#%%%%%%%%%%%%%%%%%%####
+=******#*#**#*****+*##############:+#######+*####***********##################%%%%%%%%%%%%%%%%%####
+=****##*#***##**+++*%#*##########*-+#######%=*####**********########%######***#%%%%%%%%%%%%%%%%####
+=+*#*#*#*###**+===-==--=+########+-+###**####+#####*******##########%#######*###%%%%%####%%%%%%####
+=+=+######%%***+++++***********##+-*###****##**#####*****#########%##############%%%#####%%%%%%####
+=+-+#*##%#%%#*###*+==************+-+###****##%**#############################**##%%######%%%%%%%###
"""