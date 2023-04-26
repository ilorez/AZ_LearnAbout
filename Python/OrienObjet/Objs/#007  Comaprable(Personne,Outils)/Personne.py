from comparable import Comparable
tab = [0,0,0]
class Personne(Comparable):
    def __init__(self,prix:int = None,longeur:int=None) -> None:
        self.__prix =prix
        self.__longeur = longeur
    def ajout(self):
        p = int(input("Pri :"))
        l = int(input("longuer :"))
    
    def compareTo(self):
        pass

    