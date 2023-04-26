from figure import Figure
import math
class Cercle(Figure):
    def __init__(self, centre: str = "O", coleur: str = 'black',raiyon:float = 0):
        super().__init__(centre, coleur)
        self.__raiyon = raiyon
        
    def position(self):
        return super().position()
    
    def affichage(self):
        return super().affichage()+f"\n\traiyon:{self.__raiyon}"

    def periemtre(self):
        return f"Permetre = {math.pow(self.__raiyon,2)*math.pi}"
    