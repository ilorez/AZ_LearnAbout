class Personne:
        # les propriete
    __nom = ""
    __prenom = ""
    __age = 0

    def __init__(self,__nom=None  , __prenom=None , __age=None):
        self.__nom = __nom
        self.__prenom = __prenom
        self.__age = __age

        
    def saisir(self) :
        self.__nom = str(input('Enter first name : '))
        self.__prenom = str(input('Enter last name : '))
        self.__age = int(input('Enter your age : '))


 

    def descripToi(self):
        t = 'Nom:'+str(self.__nom)+',   Prenom:'+str(self.__prenom)+ ",   Age:"+str(self.__age)
        return t
    def retrait(self,retrait__age=64):
        year = retrait__age - self.__age
        if year <= 0:
            return 'deja retrait'
        else:
            return 'l\'age qui vous reste le retrait est: '+str(year)+' ans'
