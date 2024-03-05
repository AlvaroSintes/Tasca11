def div(a,b):
    try:
        c= a/b
        print("La divisio de {} entre {} és {}".format(a,b,c))
    except ZeroDivisionError:
        print("El segon parametre no pot ser zero")
    
#PPrincipal
a= int(input("Escriure el numerador: "))
b= int(input("Escriure el denominador: "))
div(a,b)