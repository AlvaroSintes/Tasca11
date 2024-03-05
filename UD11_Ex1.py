def lenp(frase):
    b = frase.split(" ")
    c = list (map(len, b))
    print("La frase {} te les següents longituds {}".format(frase,c))

# Pprincipal
a = "Bon dia avui vaig a pescar"
lenp(a)