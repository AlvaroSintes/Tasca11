def ajuntar(l,d,c):
    a = []
    for i in range(len(l)):
        a.append(l[i]+c+d[i])
    print("La unió de les llistes {} i {} és {}".format(l,d,a))
#Pprincipal
l= ["Hola","Super","Mega"]
d=["Tete","Guapo","Amigo"]
ajuntar(l,d," ")
