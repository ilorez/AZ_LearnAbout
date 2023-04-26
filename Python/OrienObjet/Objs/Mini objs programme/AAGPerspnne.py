class Personne(object):
    def __init__(self,nom:str=None,prenom:str=None,age:int=None,ville:str=None):
        self._nom = nom
        self._prenom = prenom
        self._age = age
        self._ville = ville
    def affichage(self):
        return f"je m\'appele {self._nom} {self._prenom}, j\'ai {self._age} et j\'habite a {self._ville}"
    def saisir(self):
        self._nom = str(input("Nom:"))
        self._prenom = str(input("Prenom:"))
        self._age = int(input('Age:'))
        self._ville = str(input("ville"))
