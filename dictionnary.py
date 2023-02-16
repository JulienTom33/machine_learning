##### STRUCTURE DE DONNEES 

# on peut voir un dictionnaire comme un ensemble de clés, valeurs

# traduction = {
#     "chien": "dog",
#     "chat": "cat",
#     "souris": "mouse",
#     "oiseau": "bird"
# }

# inventaire = {
#     "bananes": 5000,
#     "pommes": 2094,
#     "poires": 402456,
#     "cerises": 2893
# }

# print(inventaire.values())
# print(inventaire.keys())
# print(len(inventaire))

# inventaire["abricots"] = 4902
# print(inventaire)

# print(inventaire.get("cerises", 1))

# villes = ["Paris", "Berlin", "Londres", "Bruxelles"]
# print(inventaire.fromkeys(villes, 'defaut'))

# print(inventaire.pop('abricots'))

# for i in inventaire:
#     print(i)
    
# for i in inventaire.values():
#     print(i) 
    
# for k, v in inventaire.items():
#     print(k, v)       

# dictionnaire_3 = {
#     "dict_1": traduction,
#     "dict_2": inventaire    
# }


# exercice

classeur = {
    "positif": [],
    "negatif": []
}

def trier(classeur, nombre):
    # classeur: dictionnaire taille 2
    # nombre: int
    # Range nombre dans positif ou negatif de classeur selon le signe de nombre
    if nombre >= 0:
        classeur['positif'].append(nombre)
    else:
        classeur['negatif'].append(nombre)    
    return classeur

print(trier(classeur, 9))
print(trier(classeur, -2))
print(trier(classeur, -4))
print(trier(classeur, 5))


