class Employer(object):
    def __init__(self,nom:str =None,prenom:str =None,salair:float =None,age:int =None):
        self.__nom = nom
        self.__prenom = prenom
        self.__salair = salair
        self.__age = age
    
    def ajouter():
        print("_"*10,"Ajout un Employer","_"*10)
        n = str(input("Nom: "))
        p = str(input("Prenom: "))
        s = float(input("Salair: "))
        a = int(input("Age: "))
        e = Employer(n,p,s,a)
        return e
        
    
    def affichage(self):
        return f"\t\t\t|Nom:{self.__nom}\n\
                \t|Prenom:{self.__prenom}\n\
                \t|Salair:{self.__salair}\n\
                \t|Age:{self.__age}"
    