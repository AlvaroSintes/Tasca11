'''
def ec():
    l=["Pere","Pau","Paula","Puri","Polonia","Pedro","Paco"]
    x = list(filter(lambda x: len(x)>4,l))
    print(x)

from functools import reduce
a= [1, 5, 7, 9]
x= reduce(lambda x,y:x+y,a)
print(x)
'''

d=["Super","Hiper","Cata","Mini","Chachi"]
e=["Woman","Loop","Crack","Mouse","Piruli"]
f= list(zip(d,e))
print(f)