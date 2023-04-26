from employer import *
class Chef(object):
    def __init__(self,nom:str =None,prenom:str =None,salair:float =None,age:int =None):
        self.__nom = nom
        self.__prenom = prenom
        self.__salair = salair
        self.__age = age
        self.__list_emps = []
        num_emps = int(input("nombre des Employes : "))
        for i in range(0,num_emps):
            self.__list_emps.append(Employer.ajouter())
            
    
    def ajouter():
        print("_"*10,"Ajout un Chef","_"*10)
        n = str(input("Nom: "))
        p = str(input("Prenom: "))
        s = float(input("Salair: "))
        a = int(input("Age: "))
        c = Chef(n,p,s,a)
        return c
        
    
    def affichage(self):
        res = f"\t\t|Nom:{self.__nom}\n\
                |Prenom:{self.__prenom}\n\
                |Salair:{self.__salair}\n\
                |Age:{self.__age}\n\
                |EMS:\n"
        for i in range(len(self.__list_emps)):
            res += f"\t\t   EM{i+1}:\n{self.__list_emps[i].affichage()} \n"
        return res