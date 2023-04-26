from AACCompt import *
# numOfCompt = int(input('Enter Number of compt you want creat : '))
# tabOfCompt = []
# for i in range(numOfCompt):
#     print('__________________________compt',i+1,':__________________________')
#     per = Compt()
#     per.saisir()
    
#     tabOfCompt.append(per)



## per.crediter(500)
## print('____________________________________________________')
## per.debiter(100)







# while True:
#     print('____________________________________________________')
#     indexOfCompt = int(input('Enter number of compt you want : '))
#     print('____________________________________________________')
#     tabOfCompt[indexOfCompt - 1].affichage()
#     print('____________________________________________________')
#     print('Enter "e" for Exit:')
#     print('Choices:')
#     print('\t1-Credit.')
#     print('\t2-debit.')
#     choix = input('Enter you Choix : ')
#     print('____________________________________________________')
#     if choix == 'e':
#         break
#     if choix == '1':
#         credit = float(input("How muc# 
# 
# h money you want : "))
#         tabOfCompt[indexOfCompt - 1].crediter(credit)
#     if choix == '2':
#         debit = float(input("How much money you want : "))
#         tabOfCompt[indexOfCompt - 1].debiter(debit)



'''# work with encapsulation''' 
persone = Compt()
print(persone)
print('\n'*5)
persone.numeroOfCompte = "000-000-000-000"
persone.nomOfPreprieter = "hamido"
persone.salair = 900
print(persone)