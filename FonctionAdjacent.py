# Matrice initiale
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Fonction pour afficher la matrice
def afficher_matrice(matrice):
    for ligne in matrice:
        print(" ".join(map(str, ligne)))
    print()

# Fonction pour vérifier si une position est valide
def position_valide(i, j, n, m):
    return 0 <= i < n and 0 <= j < m

# Fonction pour déplacer un élément dans la matrice
def deplacer(matrice, pos1, pos2):
    i1, j1 = pos1
    i2, j2 = pos2

    # Taille de la matrice
    n, m = len(matrice), len(matrice[0])

    # Vérifier que les positions sont valides et adjacentes
    if position_valide(i1, j1, n, m) and position_valide(i2, j2, n, m):
        # Vérifier que les positions sont directement connectées
        if abs(i1 - i2) + abs(j1 - j2) == 1:
            # Échanger les éléments
            matrice[i1][j1], matrice[i2][j2] = matrice[i2][j2], matrice[i1][j1]
            return True
        else:
            print("Les positions ne sont pas adjacentes.")
    else:
        print("Position invalide.")
    return False

# Afficher la matrice avant le déplacement
print("Matrice initiale :")
afficher_matrice(matrice)

# Déplacement : échanger (0,0) avec (1,0) (ca c'est juste un exemple mais on peut aussi ask à l'utilisateur )
if deplacer(matrice, (0, 0), (1, 0)):
    print("Matrice après déplacement :")
    afficher_matrice(matrice)
else:
    print("Échec du déplacement.")
