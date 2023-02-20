import numpy as np


##### INDEXING

# une tableau possède un axe 0 qui correspond aux lignes et un axe 1 qui correspond aux colonnes.
# on indique un index pour les lignes et un index pour les colonnes. Donc A[0, 0] = [ligne 1, colonne 1]

# A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(A)

# print(A[0, 0])
# print(A[0, 1])
# print(A[1, 1])


##### SLICING

# # on précise un index de départ, un index de fin, on peut aussi préciser un index de pas

# A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# # pour imprimer tous les éléments de la première colonne: A[: -> tout ce qu'il y a du début à la fin de la ligne, 0 -> tout ce qu'il y a à l'index 0 de la colonne]
# print(A[:, 0])

# # pour imprimer tous les éléments de la première ligne: A[0, :]
# print(A[0, :])
# # ou car numpy comprend qu'on veut accéder à la totalité de la première ligne du tableau
# print(A[0])

# # pour sélctionner un bloc du tableau
# # les deux premières lignes et les deux premières colonnes
# print(A[0:2, 0:2])

# # subseting: on va créer un plus petit tableau à partir de notre grand tableau
# B = A[0:2, 0:2]
# # B est un tableau de dimension 2, 2
# print(B.shape)

# # on va transformer cette section de A
# A[0:2, 0:2] = 10
# print(A)

# # exemple de subset
# # on commence par dire qu'on imprime toutes les lignes puis on part de l'avant dernière colonne jusqu'aà la fin du tableau. A[:, -2 -> avant dernière colonne, : -> fin du tableau]
# A[:, -2:]
# print(A)

# # on crée un tableau B (un tuple()), de dimension 4x4, avec 4 lignes et 4 colonnes, remplies de zéros
# B = np.zeros((4, 4))
# print(B)

# # on va transformer le milieu du tableau B en la remplaçant par des 1
# # technique avec un point de début et un point de fin
# # les deux premières lignes du tableau donc de la ligne 1 à la ligne 3
# # les colonnes, on veut de l'index 1 à l'index 3
# B[1:3, 1:3] = 1
# print(B)

# # on crée un tableau C (un tuple()), de dimension 5x5, avec 5 lignes et 5 colonnes, remplies de zéros
# C = np.zeros((5, 5))
# print(C)

# # on va intégrer le pas dans cette mééthode de slicing
# # toutes les valeurs des lignes en sautant un pas de 2. C = [:: -> toutes les valeurs  2 en sautant un pas de 2]
# # toutes les valeurs des colonnes en sautant un pas de 2. C = [:: -> toutes les valeurs  2 en sautant un pas de 2]
# C[::2, ::2] = 1
# print(C)


##### BOOLEAN INDEXING

# # on créée un tableau avec des nombre random dans un tableau de dimension 5x5
# A = np.random.randint(0, 10, [5, 5])
# print(A)

# # on va chercher des résultats de type bool 
# # on va renvoyer en true tous les résultats < 5
# print(A < 5)

# # ce tableau est un mask qu'on va pouvoir réutiliser comme un index à l'intérieur de n'importe quel tableau numpy qui va être de même dimension. Ici 5x5
# # on va pouvoir convertir les valeurs d'un tableau
# # exemple: on reprend le tableau A. On va sélectionner tous les éléments dans A inférieurs à 5 et dire qu'ils sont égaux à 10
# A[A<5] = 10
# print(A)
# # exemple: on reprend le tableau A. On va sélectionner tous les éléments dans A inférieurs à 5 et supérieur à 2 et dire qu'ils sont égaux à 10
# A[(A<5) & (A>2)] = 10
# print(A)

# # avec un mask on va filtrer les données d'un tableau qui a la même dimension
# # exemple: on va retourner un tableeau dans lequel les valeurs sont inférieurs à 5
# print(A[A<5])


##### exercice

from scipy import misc
import matplotlib.pyplot as plt
face = misc.face(gray=True)
# plt.imshow(face, cmap=plt.cm.gray)
# plt.show()

# # face devient un tableau numpy
# # pour voir le type du tableau
# print(type(face))
# # c'est un tableau à trois dimensions, la dernière valeur "3" nous indique les trois couleurs (rouge, vert, bleu)
# # après modification on a changé la couleur en gray
# print(face.shape)

# zoomer 1/4 de la photo vers le milieu
# utiliser les dimensions de la photo avec tuple shape, enregistrer ces dimensions dans des variables et utiliser les techniques de slicing
# bonus: augmenter la luminosité de pixels qui sont déjà au dessus d'une certaine luminosité et réduire la luminosité des pixels qui sont déjà très très sombres en utilisant le boolean indexing

# on va créer une variable pour la hauteur et une variable pour la largueur qui sont les dimensions de notre image
# axe vertical
h = face.shape[0]

# axe horizontal
w = face.shape[1]

# on va créer une nouvelle variable qui comprendra le tableau face, on va diviser en absolu l'axe vertical puis l'axe horizontal en partant du début puis de la fin (avec les -)
# zoom_face = face[h//4 : -h//4, w//4 : -w//4]
# zoom_face[zoom_face > 150] = 255
# plt.imshow(zoom_face, cmap=plt.cm.gray)
# plt.show()

# bonus, on va compresser le poids de l'image sans perdre la qualité
# on va effectuer un slicing en effectuant un pas de 2
face = face[::2, ::2]
plt.imshow(face, cmap=plt.cm.gray)
plt.show()





