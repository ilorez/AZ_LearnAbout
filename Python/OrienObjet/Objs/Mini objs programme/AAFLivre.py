class Livre:
    
    def __init__(self,obj=None,titre=None,auteur=None,prix=None,annee=None):
        if obj is not None:
            self.copy(obj)
        else:
            self.nocopy()

    @classmethod
    def copy(self,obj):
        self.__titre = obj.__titre
        self.__auteur = obj.__auteur
        self.__prix = obj.__prix
        self.__annee = obj.__annee

    @classmethod
    def nocopy(self):
        self.__titre = 'titre'
        self.__auteur = 'auteur'
        self.__prix = 'prix'
        self.__annee = 'annee'
        
    #titre
    @property
    def titre(self):
        return self.__titre
    @titre.setter
    def titre(self,valuer):
        self.__titre = valuer


    #auteur
    @property
    def auteur(self):
        return self.__auteur
    @auteur.setter
    def auteur(self,valuer):
        self.__auteur = valuer
    
    
    #prix
    @property
    def prix(self):
        return self.__prix
    @prix.setter
    def prix(self,valuer):
        self.__prix = valuer
    
    
    #annee
    @property
    def annee(self):
        return self.__annee
    @annee.setter
    def annee(self,valuer):
        self.__annee = valuer
    
    #affichage methode
    def affichage(self):
        print('Info:\nTitre:',self.__titre ,'\nAuteur: ',self.__auteur,'\nPrix: ', self.__prix ,'\nannee: ',self.__annee ,sep='')

    #methode type
    def type(self):
        if self.__prix < 100:
            print('<100')
        elif self.__prix > 500:
            print('>500')
        else:
            print('100-500')
    


