from AAHVehicule import *
class Avion(Vehicule):
    def __init__(self, vitess: int = None, nombre_de_passage: int = None,nombre_de_moteurs:int = None):
        super().__init__(vitess, nombre_de_passage)
        self.__nombre_de_moteurs = nombre_de_moteurs
    def affichage(self):
        return super().affichage()+f' avec {self.__nombre_de_moteurs} moteurs.'
    def saisir(self):
        super().saisir()
        self.__nombre_de_moteurs = int(input("nombre de moteurs: "))

