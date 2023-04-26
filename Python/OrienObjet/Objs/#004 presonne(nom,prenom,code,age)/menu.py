from personnev2 import *

while True:
    print("*"*20)
    print('Menu:')
    
    print('\t1- Ajout un personne')
    print('\t2- affichage tout personne')
    print('\t3- modifier nom de un personee')
    print('\t4- Supprime un personne')
    print('\t5- Cherche pour un personne')
    print('\t6- affiche les nombre des personne ')
    print('\t7- affiche catigory de pesonne')
    
    print('\t0- Quitte')
    choix = int(input('Enter ton choix:'))
    ### avic Match
    match choix:
        case 0:
            break
            
        case 1:
            Personne.ajout()
            
        case 2:
            Personne.affichage()
            
        case 3:
            Personne.modifier()
            
        case 4:
            Personne.supprime()
            
        case 5:
            Personne.cherche()
            
        case 6:
            Personne.count()
            
        case 7:
            Personne.catigory()
       
