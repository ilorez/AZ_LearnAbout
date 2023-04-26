class Vehicule:
    def __init__(self,vitess:int = None,nombre_de_passage:int = None):
        self._vitess = vitess
        self._nombre_de_passage = nombre_de_passage
    def affichage(self):
        return f'vitess est {self._vitess} km/s et le nombre de passage est {self._nombre_de_passage}'
    def saisir(self):
        self._vitess = int(input("vitess: "))
        self._nombre_de_passage = int(input("nombre de passag: "))
