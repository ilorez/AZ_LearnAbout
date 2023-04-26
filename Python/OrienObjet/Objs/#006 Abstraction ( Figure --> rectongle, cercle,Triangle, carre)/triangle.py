from figure import Figure

class Triangle(Figure):
    def __init__(self, centre: str = "O", coleur: str = 'black',cote1:int=0,cote2:int=0,cote3:int=0):
        super().__init__(centre, coleur)
        self.__cote1 = cote1
        self.__cote2 = cote2
        self.__cote3 = cote3

        
    def position(self):
        return super().position()
    
    def affichage(self):
        return super().affichage()+f"\n\cotes:{self.__cote1,self.__cote2,self.__cote3}"

    def periemtre(self):
        return f"Permetre = {self.__cote1+self.__cote2+self.__cote3}"
    