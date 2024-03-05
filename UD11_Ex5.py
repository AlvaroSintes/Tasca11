def crear_diccionari(llista):
    dic={}
    for i,e in enumerate(llista):
        dic[e]=i
    print("De la llista {} hem creat el diccionari {}".format(llista,dic)) 

#Pprincipal
llista=["Cotxe","Casa","Vaixell","Colom","Ca","Mussol","Lleo"]
crear_diccionari(llista)