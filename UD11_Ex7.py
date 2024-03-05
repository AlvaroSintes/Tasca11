def stringtolist(c):
    r=[ x for x in c]
    print ("De la cadena {} hem creat la llista {}".format(c,r))

#Pprincipal
c=input("Introdueixi una paraula: ")
stringtolist(c)