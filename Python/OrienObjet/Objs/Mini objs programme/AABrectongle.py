class Rectongle:
    _largeur = 0
    _langeur = 0
    def __init__(self,_largeur=0,_langeur=0):
        self._largeur = _largeur
        self._langeur = _langeur
    def saisair(self):
        self._largeur = float(input('Entre Larguer: '))
        self._langeur = float(input('Entre Languer: '))
    def affichage(self):
        print('larguer Est: ',self._largeur,'languer Est: ',self._langeur)
    def perimetre(self):
        return (self._largeur + self._langeur)*2
    def surface(self):
        return self._largeur * self._langeur