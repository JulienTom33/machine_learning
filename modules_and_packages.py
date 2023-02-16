import package_function1 as p1
from package_function1 import fibonacci

import math
import random
import statistics
import os
import glob

# liste = p1.fibonacci(50)
# print(liste)

liste = fibonacci(50)
# print(liste)


##### Module Math
# les formules de mathématiques
# print(math.pi)


# ##### Module Statistics
# # faire une moyenne
# print(statistics.mean(liste))
# # faire uen variance
# print(statistics.variance(liste))


# ##### Module Random
# # un choix aléatoire dans la liste
# print(random.choice(liste))


# ##### Module OS
# # Operating System
# print(os.getcwd())


##### Module Glob
# # fonction qui retourne une liste qui contient tous les noms des fichiers que l'on a dans notre répertoire de travail 
# print(glob.glob("*"))

filenames = glob.glob('*.txt')
d = {}
for file in filenames:
    with open(file, 'r') as f:
        d[file] = f.read().splitlines()
print(d)



                
    