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

    # Vérifier que les positions sont valides
    if position_valide(i1, j1, n, m) and position_valide(i2, j2, n, m):
        # Échanger les éléments
        matrice[i1][j1], matrice[i2][j2] = matrice[i2][j2], matrice[i1][j1]
        return True
    else:
        print("Position invalide.")
        return False

# Afficher la matrice initiale
print("Matrice initiale :")
afficher_matrice(matrice)

# Boucle interactive
while True:
    try:
        # Demander à l'utilisateur l'élément à déplacer
        pos1 = tuple(map(int, input("Entrez la position de l'élément à déplacer (ligne colonne) : ").split()))
        
        # Demander la nouvelle position
        pos2 = tuple(map(int, input("Entrez la nouvelle position souhaitée (ligne colonne) : ").split()))
        
        # Essayer de déplacer l'élément
        if deplacer(matrice, pos1, pos2):
            print("Matrice après déplacement :")
            afficher_matrice(matrice)
        else:
            print("Le déplacement a échoué.")
    except ValueError:
        print("Entrée invalide. Veuillez entrer des nombres pour les positions.")
    
    # Demander si l'utilisateur veut continuer
    continuer = input("Voulez-vous effectuer un autre déplacement ? (oui/non) : ").strip().lower()
    if continuer != "oui":
        print("Fin du programme.")
        break
