from AAAPersonne import *
# per = Personne()

# tabOfInformation = []
# for i in range(2):
#     print('Ecrire Information de Persone',str(i+1))
#     per = Personne()
#     per.saisir()    
    # tabOfInformation.append([per.descripToi(),per.retrait()])
# print(tabOfInformation)
# per = Personne()
numberOfPersone = int(input('Enter number of Persones: '))
tabOfInformation = []
for i in range(numberOfPersone):
    print('\n'*2,'Ecrire Information de Persone ',str(i+1),'.',sep='')
    per = Personne()
    per.saisir() 
       
    tabOfInformation.append(per)
    print('*---------------------------------------------*')
while True:
    print('\n'*3)
    personne = int(input('Enter a personne number (Enter "e" for Exit): '))
    if personne == 'e':
        break
    print('\n'*2,tabOfInformation[personne-1].descripToi(),'\n---\n',tabOfInformation[personne-1].retrait(80),sep='')
    