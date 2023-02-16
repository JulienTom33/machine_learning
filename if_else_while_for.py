##### STRUCTURE DE CONTROLES 

######condition if else

# x = 1
# if x > 0:
#     print(x, 'positif')
    
# x = -1
# if x > 0:
#     print(x, 'positif')
# else:
#     print(x, 'negatif')
    
# x = 0    
# if x > 0:
#     print(x, 'positif')
# elif x == 0:
#     print(x, 'nul')
# else:
#     print(x, 'negatif')  
    
# x = 1
# y = 2
# if (x > 0) & (y > x):
#     print(x, y, 'positif')
# elif x == 0:
#     print(x, 'nul')
# else:
#     print(x, 'negatif')    
    
# def signe(x):
#     if (x > 0):
#         print(x, 'positif')
#     elif x == 0:
#         print(x, 'nul')
#     else:
#         print(x, 'negatif') 
# print(signe(0))  


######boucle for   

# # la fonction range permet de générer une séquence de nombres
# for i in range(10):
#     print(i)
    

######boucle while

# x = 0
# while x < 10:
#     print(x)
#     x += 1  
    

### exercice
def fibonacci(n):
    # retourne une liste contenant la suite de fibonacci jusqu'a n
    a = 0
    b = 1
    while b < n:
      a, b = b, a+b
      print(a)

fibonacci(1000)  

          
    
           