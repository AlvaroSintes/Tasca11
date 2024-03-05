def Imprimir_fitxer(m):
    a=[]
    with open(m,"r") as f:
        for e in f:
            c = e.split("\n")
            if c!="":
                a.append(c[0])
    print(a)

def afegir_fitxer(m,llista):
    with open(m,"a+") as f:
        for e in llista:
            f.write(e+"\n")
#Pprincipal

fitxer = "/home/cicles/AO/Tasca11/ex11.txt"
llista = ["Jordi","Oscar","Anas","David"]
afegir_fitxer(fitxer,llista)
Imprimir_fitxer(fitxer)