from Personne import *
from Cadre import *
from Ouvrier import *
from Patron import *



T = []
while True:
    print('choose un  post: ')
    print('\t1-Ouvrier')
    print('\t2-Cadre')
    print('\t3-Parton')
    print('\t0-for exit')
    choix = int(input('Enter ton choix: '))
    if choix ==0:
        break
    elif choix ==1:
        p = Ouvrier()
        p.saisir()
        T.append(p)
    elif choix == 2:
        p = Cadre()
        p.saisir()
        T.append(p)
    elif choix == 3:
        p = Patron()
        p.saisir()
        T.append(p)
    else:
        print('sorry this choix not found')
print('_'*10)
for i in range(len(T)):
    print(T[i].getInfo())
# p = Ouvrier('nom','prenom','societe',123456789,yearEnter= 2020,monthEnter= 5,dayEnter= 15,SMIG= 300000,age= 18)

# p = Peronne('nom','prenom','societe',123456789)

# # p = Ouvrier('nom','prenom','societe',123456789,yearEnter= 2020,monthEnter= 5,dayEnter= 15,SMIG= 300000,age= 18)
# num  = 1
# num = 2
# # print(p.affichage())
# print(p.getSalaire())

