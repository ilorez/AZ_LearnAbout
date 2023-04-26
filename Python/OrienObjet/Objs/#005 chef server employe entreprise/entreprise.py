from services import *
class Entreprise(object):
    
    def __init__(self,nom:str =None):
        self.__nom = nom
        self.__list_servers = []
        num_services = int(input("nombre des services : "))
        for i in range(0,num_services):
            self.__list_servers.append(Services.ajouter())
    
    def affichage(self):
        print("_"*10,"Affichege Tree","_"*10)
        res = f"Entreprise: {self.__nom} \n"
        for i in range(len(self.__list_servers)):
            res += f"\tSesrvice {i+1}:\n{self.__list_servers[i].affichage()}"
        return res

    
    


    # Getters and setters 
    # nom
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, valeur):
        self.__nom = valeur
    
        
