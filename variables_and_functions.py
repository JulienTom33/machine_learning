# x = 1
# y = 2.5
# print(x != y)


# fonction de type mathématique
# f = lambda x: x**2
# print(f(3))
# f = lambda x, y: x**2 + y
# print(f(3, 5))


# fonction
def e_potentielle(masse, hauteur, e_limite, g=9.81):
  energie = masse * hauteur * g 
  return energie > e_limite

print(e_potentielle(masse=10, hauteur=10, e_limite=800)) 
        




