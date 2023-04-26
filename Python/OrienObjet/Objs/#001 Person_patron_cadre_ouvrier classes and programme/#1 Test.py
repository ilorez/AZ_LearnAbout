from Personne import *
from Cadre import *
from Ouvrier import *
from Patron import *

p = Ouvrier('nom','prenom','societe',123456789,yearEnter= 2020,monthEnter= 5,dayEnter= 15,SMIG= 300000,age= 18)
# print(p.getInfo()) 
#with getinfo in ouvrier ==> print all att of personne and ouvrier
#delet getinfo from ouvrier ==> print just personne att

p1 = Peronne('nom1','prenom1','societe1',111111111)
print(p1.getInfo()) 
#with getingo in personne ==> work
#without getingo in personne  ==> deosn't work



