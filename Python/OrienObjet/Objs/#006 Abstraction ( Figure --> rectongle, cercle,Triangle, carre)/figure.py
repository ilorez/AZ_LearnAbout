from abc import ABC, abstractmethod

class Figure(ABC):
    def __init__(self,centre:str = "O",coleur:str = 'black'):
        super().__init__() # ??
        self.__centre = centre
        self.__coleur = coleur

    
    @abstractmethod
    def periemtre(slef):
        pass

    def affichage(self):
        return f"info:\n\tCentre:{self.__centre}\n\tColeur:{self.__coleur}"
    
    def position(self):
        y = float(input("entre y:"))
        z = float(input("entre z:"))
        return f"y={y},z={z}"
    


    