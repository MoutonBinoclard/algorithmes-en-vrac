# Coordonnées cartessiennes

a = (0, 0)
b = (1, 2)
c = (2, 1)

def cercle_passant_par_3_points_co_cart(pt1, pt2, pt3):
    # Étape 1 : trouver 2 milleux, entre 1 et 2, puis 1 et 3 par exemple
    m1 = ((pt1[0] + pt2[0]) / 2, (pt1[1] + pt2[1]) / 2)
    m2 = ((pt1[0] + pt3[0]) / 2, (pt1[1] + pt3[1]) / 2)
    
    # Étape 2 : trouver les vecteurs directeurs des cotés
    v1 = (pt2[0] - pt1[0], pt2[1] - pt1[1])
    v2 = (pt3[0] - pt1[0], pt3[1] - pt1[1])

    # Étape 3 : trouver les vecteurs normaux
    n1 = (-v1[1], v1[0])  # Normal à v1
    n2 = (-v2[1], v2[0])  # Normal à v2
    
    # Déterminant du système, juste pour vérifier si les points sont alignés
    det = n1[0] * n2[1] - n1[1] * n2[0]
    
    if abs(det) < 1e-10:  # Points alignés
        return None, None
    
    # Résolution du système
    dx = m2[0] - m1[0]
    dy = m2[1] - m1[1]
    t = (dx * n2[1] - dy * n2[0]) / det
    
    # Centre du cercle
    centre_x = m1[0] + t * n1[0]
    centre_y = m1[1] + t * n1[1]
    centre = (centre_x, centre_y)

    return centre


# Placer les points et le centre sur un graphique, sans tracer le cercle
import matplotlib.pyplot as plt
plt.plot(a[0], a[1], 'r+', label='Point A')
plt.plot(b[0], b[1], 'g+', label='Point B')
plt.plot(c[0], c[1], 'b+', label='Point C')
centre = cercle_passant_par_3_points_co_cart(a, b, c)
if centre:
    plt.plot(centre[0], centre[1], 'yo', label='Centre du cercle')
    plt.title(f"Cercle passant par A, B et C\nCentre: {centre}")
plt.show()
