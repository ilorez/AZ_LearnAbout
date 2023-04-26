from figure import Figure

class Carre(Figure):
    def __init__(self, centre: str = "O", coleur: str = 'black',cote:float = 0):
        super().__init__(centre, coleur)
        self.__cote = cote
        
    def position(self):
        return super().position()
    
    def affichage(self):
        return super().affichage()+f"\n\tCote:{self.__cote}"

    def periemtre(self):
        return f"Permetre = {self.__cote * 4}"
    