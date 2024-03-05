from functools import reduce
def Passar_a_Numero(llista):
    a = list(map(lambda a: str(a), llista))
    b = reduce(lambda x,y:x+y,a)
    print("La llista {} és el numero {}". format(llista,b))

#Pprincipal
a = [1, 3, 5, 6]
Passar_a_Numero(a)