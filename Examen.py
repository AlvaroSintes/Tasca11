from functools import reduce
def menu():
    opcio=0
    while opcio<1 or opcio>5:
        print("""
            Menu principal:
            1.Programacio estructurada
            2.Programacio funcional
            3.Programacio Orientada a objectes
            4. Acces a fitxers
            5.Sortir
        """)
        opcio= int(input("Seleccioni l'opcio que vulgui executar: "))
        if opcio<1 or opcio>5:
            print ("Opcio no valida i no se perque !")
        else:
            return opcio

def programacio_estructurada():
    print("Molt be, has entrat a la programacio estructurada! ")
    l=["Pere","Pau","Paula","Puri","Polonia","Pedro","Paco"]
    x = list(filter(lambda x: len(x)>4,l))
    print(x)
def programacio_funcional():
    print("Molt be, has entrat a la programacio funcional! ")
    a= [1, 5, 7, 9]
    x= reduce(lambda x,y:x+y,a)
    print(x)
    d=["Super","Hiper","Cata","Mini","Chachi"]
    e=["Woman","Loop","Crack","Mouse","Piruli"]
    f= list(zip(d,e))
def programacio_oo():
    print("Molt be, has entrat a la programacio oo! ")
def acces_fitxers():
    print("Molt be, has entrat a l'acces a fitxers! ")
#Pprincipal
op=1
while op!=5:
    op= menu()
    match(op):
        case 1:
            programacio_estructurada()
        case 2:
            programacio_funcional()
        case 3:
            programacio_oo()
        case 4:
            acces_fitxers()
        case 5:
            print("Gracies per haber emprat el programa! ")
        case other:
            print("Opcio no valida! ")


