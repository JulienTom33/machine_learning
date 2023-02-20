import numpy as np

np.random.seed(0)
A = np.random.randint(0, 10, [2, 3])
# print(A)

# # faire la somme du tableau
# print(A.sum())

# utiliser la fonction sum sur l'un des axes du tableau
# l'axe 0 est l'axe vertical, l'axe 1 est l'axe horizontal

# on va faire la somme des éléments qui se suivent horizontalement
print(A.sum(axis=0))

# on va faire la somme des éléments qqui se suivent verticalement
print(A.sum(axis=1))


