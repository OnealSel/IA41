# Fonction pour encoder une matrice avec les positions des éléments
def encode_matrix(matrix):
    # Liste pour stocker les éléments et leurs positions
    encoded_matrix = []
    
    # Parcourir la matrice et récupérer les indices de ligne et de colonne
    for i in range(len(matrix)):  # Parcourir les lignes
        for j in range(len(matrix[i])):  # Parcourir les colonnes
            # Ajouter l'élément avec sa position (ligne, colonne)
            encoded_matrix.append(((i, j), matrix[i][j]))
    
    return encoded_matrix

# Exemple de matrice
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Encoder la matrice avec les positions
encoded_matrix = encode_matrix(matrix)

# Affichage des résultats
print("Matrice encodée :")
for pos, val in encoded_matrix:
    print(f"Position: {pos}, Valeur: {val}")
