from Personne import *
from Cadre import *
from Ouvrier import *
from Patron import *

objs = [Peronne() for i in range(8)]
for obj in objs:
    obj.saisir()
    print("--------------")

objs[0] = Patron()
objs[0].saisir()

for i in range(1,6):
    objs[i] = Ouvrier()
    objs[i].saisir()
    print("--------------")
for i in range(6,8):
    objs[i] = Cadre()
    objs[i].saisir()
    print("--------------")

for obj in objs:
    print("++++++++++++++++++++++++++++")
    print(obj.getInfo())
    print("++++++++++++++++++++++++++++")







