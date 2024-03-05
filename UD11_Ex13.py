class Animal():
    def __init__(self,atribut, edat):
        self.atribut=atribut
        self.edat=edat
    def xerrar():
        pass
    def mourem():
        pass
    def quisoc():
        print("Soc un animal ")
    
class Cavall (Animal):
    def xerrar(self):
        print("Iiiiiii")
    def mourem(self):
        print("Hem moc a trot")
    def quisoc(self):
        print("Soc un cavall ")
class Dofi (Animal):
    def xerrar(self):
        print("IchIchIch")
    def mourem(self):
        print("Hem moc nedant")
    def quisoc(self):
        print("Soc un Dofi ")
class Abella (Animal):
    def xerrar(self):
        print("Sssssss")
    def mourem(self):
        print("Hem moc volant")
    def quisoc(self):
        print("Soc una Abella ")
    def picar(self):
        print("Si m'emprenyes et picare")
class Huma(Animal):
    def __init__(self,nom, atribut, edat):
        self.nom=nom
        self.atribut=atribut
        self.edat=edat
    def xerrar(self):
        print("Hola! Nosaltres utilizem un idioma per parlar")
    def mourem(self):
        print("Hem moc caminant")
    def quisoc(self):
        print("Soc un Huma ")
class Centaure (Huma, Cavall):
    def xerrar(self):
        print("Hola! Nosaltres utilizem un idioma per parlar")
    def mourem(self):
        print("Hem moc a trot")
    def quisoc(self):
        print("Soc un Centaure ")
class Fiet(Huma):
    def __init__(self,nom,atribut, edat,llpares):
        self.nom=nom
        self.atribut=atribut
        self.edat=edat
        self.pares=llpares
    def xerrar(self):
        print("Ueeeeeeeueee")
    def mourem(self):
        print("Hem moc gatetjant")
    def quisoc(self):
        print("Soc un Fiet ")

class xou():
    def xerrar(self):
        print("Xou")
    def mourem(self):
        print("Hem moc fent xou")
    def quisoc(self):
        print("Soc un Xou ")

#Pprincipal

a=[Cavall("Marro","4"),Dofi("Gris","10"),Abella("Negra i groga","0,5"),Huma("Sibilia","Cristia","7"),Centaure("Fiona","Marro","18"),Fiet("Jordi","Moreno","9",["Fiona","Marc"]),xou()]
for e in a:
    e.xerrar()
    e.mourem()
    e.quisoc()
    