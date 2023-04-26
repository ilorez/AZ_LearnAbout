from chef import *
class Services(object):
    def __init__(self,nom:str =None):
        self.__nom = nom
        self.__chef = Chef.ajouter()
            
    
    def ajouter():
        print("_"*10,"Ajout un Service","_"*10)
        n = str(input("Nom: "))
        s = Services(n)
        return s
        
    
    def affichage(self):
        return f"\t   |Nom:{self.__nom} \n\t    Chef:\n{self.__chef.affichage()}"
                