##### LIST COMPREHENSION

# import time

# le processus de création dans la mémoire de l'ordinateur se fait plus rapidement

# # tous les carrés de 0 à 9
# liste_1 = []
# for i in range(10):
#     liste_1.append(i**2)
    
# print(liste_1)

# # ce qui donne

# liste_2 = [i**2 for i in range(10)]
# print(liste_2) 


# # module pour calculer le temps mis par le processus
# start = time.time()

# liste_1 = []
# for i in range(10000000):
#     liste_1.append(i**2)
# end = time.time()
# print(end-start)

# start = time.time()      

# liste_2 = [i**2 for i in range(10000000)]
# end = time.time()
# print(end-start)


# # Nested list = liste dans une liste

# liste_3 = [[i for i in range(3)] for j in range(4)]
# print(liste_3)



##### DICT COMPREHENSION

# dictionnaire = {
#     "0": "Pierre",
#     "1": "Jean",
#     "2": "Julie",
#     "3": "Sophie"
# }

# prenoms = ["Pierre", "Jean", "Julie", "Sophie"]

# dico = {k:v for k, v in enumerate(prenoms)}
# print(dico)
# print(dico.keys())

# ages = [24, 62, 10 ,23]

# # on créer un dictionnaire dans le quel les clés sont les prénoms et les valeurs sont les ages
# dico_2 = {prenom:age for prenom, age in zip(prenoms, ages)}
# print(dico_2)

# #on rajoute une condition à la boucle for
# dico_3 = {prenom:age for prenom, age in zip(prenoms, ages) if age > 20}
# print(dico_3)


##### TUPLE COMPREHENSION

# # ceci crée un générateur
# tuple_1 = (i**2 for i in range(10))
# print(tuple_1)

# #on engloble avec la fonction tuple affin de crééer un tuple
# tuple_1 = tuple((i**2 for i in range(10)))
# print(tuple_1)



# exercice
carres_pairs = {
    str(k) : k**2 for k in range(0, 20)
}
print(carres_pairs)