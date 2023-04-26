from AAGPerspnne import *
class Employe(Personne):
    def __init__(self,nom:str=None,prenom:str=None,age:int=None,ville:str=None,salaire:float=None,societe:str=None):
        super().__init__(nom,prenom,age,ville)
        self.__salaire = salaire
        self.__societe = societe
    def affichage(self):
        return super().affichage() + f' en societe {self.__societe} et mon salaire est: {self.__salaire}'
    def saisir(self):
        super().saisir()
        self.__salaire = str(input('salaire'))
        self.__societe = str(input("societe"))
    

