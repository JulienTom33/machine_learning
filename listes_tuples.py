##### STRUCTURE DE DONNEES : SEQUENCES

# une séquence est un ensebmle d'éléments ordonnés

#### Listes

liste_1 = [1, 4 ,2 ,7 ,35 ,84]
villes = ["Paris", "Berlin", "Londres", "Bruxelles"]
liste_2 = [liste_1, villes]
liste_3 = []


#### Tuple

# un tuple est comme une liste mais qu'on ne peut pas modifier

tuple_1 = (1, 2, 6, 1, 7)


#### String

prenom = 'Nicolas'


#### Indexing

# print(villes[0]) #premier élément
# print(villes[1]) #deuxième élément
# print(villes[-1]) #dernier élément
# print(villes[-2]) #avant dernier


#### Slicing

# print(villes[0:3])
# print(villes[2:])
# print(villes[1:3])
# print(villes[0:3:2])

# print(prenom[:3])


#### Méthodes sur une liste

# villes.append("Dublin")
# print(villes)

# villes.insert(2, "Madrid")
# print(villes)

# villes_2 = ["Amsterdam", "Rome"]
# villes.extend(villes_2)
# print(villes)

# len(villes)
# print(len(villes))

# villes.sort()
# print(villes)
# villes.sort(reverse=True)
# print(villes)

# villes.count('Paris')
# print(villes.count('Paris'))


# if 'Paris' in villes:
#     print('Oui')
# else:
#     print('Non')
    
# for i in villes:
#     print(i)
    
# for index, valeur in enumerate(villes): 
#     print(index, valeur)  

# for a, b in zip(villes, liste_1):
#     print(a, b)


# exercice
# retourne une liste qui comprend tous les éléments de la suite de fibonacci
def fibonacci(n):
    # retourne une liste contenant la suite de fibonacci jusqu'a n
    a = 0
    b = 1
    c = []
    while b < n:
      a, b = b, a+b
      c.append(a)
    return c  

print(fibonacci(1000))          





