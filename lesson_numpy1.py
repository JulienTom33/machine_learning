import numpy as np

# # avec constructeur en dur
# A = np.array([1, 2, 3])
# print(A)

# # on vérifie le nombre de dimensions
# print(A.ndim)
# # il y a une dimension

# # on vérifie sa forme
# print(A.shape)
# # sur son unique dimension il y a trois éléments

# # on vérifie le nombre d'éléments
# print(A.size)

# # avec constructeur initialisé valeur 0
# #tuple avec 3 lignes et 2 colonnes
# B = np.zeros((3, 2))
# print(B)
# print(B.ndim)
# # il y a deux dimensions
# print(B.size)
# # il y a 6 éléments

# # avec constructeur initialisé valeur 1
# C = np.ones((4,3))
# print(C)

# # avec constructeur initalisé de nombre random
# # si on veut fixer le générateur aléatoire pour qu'il nnous produise tout le temps le même résultat on utilise la fonction seed
# D = np.random.seed(0)
# D = np.random.randn(3, 4)
# print(D)

# # avec constructeur linspace qui permet de créer un tableau à une dimension avec un point de début et un point de fin précis et une quantité d'éléments que l'on veut avoir dans notre tableau
# # cette quantité de nombre va être répartie de manière égale entre le point de début et le point de fin
# E = np.linspace(0, 10, 20)
# print(E)

# # avec constructeur arange qui permet de créer un tableau à une dimension avec un point de début et un point de fin précis et le pas qu'on veut entre chaque élément
# F = np.arange(0, 10, 2)
# print(F)

# #  on peut rajouter le type de données que l'on veut ajouter avec dtype
# G = np.linspace(0, 10, 30, dtype=np.float16)
# print(G)
# # on veut des nombres plus précis mais programme moins rapide
# H = np.linspace(0, 10, 30, dtype=np.float32)
# print(H)

##### MANIPULATION

I = np.zeros((3, 2))
J = np.ones((3, 2))
# print(I)
# print(J)

# on assemble les tableaux verticalement ou horizontalement
# horizontalement
K = np.hstack((I, J))
print(K)

#verticalement
L = np.vstack((I, J))
print(L)