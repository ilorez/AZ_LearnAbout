from figure import Figure

class Rectongle(Figure):
    def __init__(self, centre: str = "O", coleur: str = 'black',longeur:float = 0,largeur:float = 0):
        super().__init__(centre, coleur)
        self.__longeur = longeur
        self.__largeur = largeur
    
    def position(self):
        return super().position()
    
    def affichage(self):
        return super().affichage()+f"\n\tlongeur:{self.__longeur}\n\tlargeur:{self.__largeur}"

    def periemtre(slef):
        return f"Permetre = {(slef.__largeur+slef.__longeur)*2}"
    