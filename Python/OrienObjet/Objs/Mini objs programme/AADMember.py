class Member:
    __name= ""
    def __init__(self,name:str):
        self.__name = name #prvite
        # self._name = name #prvite but not in python u need just do not use it 
        # self.name = name #public
    
    #la methode pour affichage de l'etat d'objet
    def __str__(self):
        return "votre nom est:" + (str)(self.__name) 
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, valuer):
        self.__name = valuer