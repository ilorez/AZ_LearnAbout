class Compt:
    __numeroOfCmpte = None
    __nomOfPreprieter = None
    __salair = None
    def __init__(self,__numeroOfCmpte=None,__nomOfPreprieter = None,__salair=None) :
        self.__numeroOfCmpte = __numeroOfCmpte
        self.__nomOfPreprieter = __nomOfPreprieter
        self.__salair = __salair
    def __str__(self):
        return ' Your Info:' + '\n nomOfPreprieter: ' +(str)( self.__nomOfPreprieter) + '\n numeroOfCmpte: '+(str)(self.__numeroOfCmpte )+ "\n salair: "+(str)(str(self.__salair))  
        
    def saisir(self):
        self.__numeroOfCmpte = input('Enter Numero of Compte: ')
        self.__nomOfPreprieter = input('Enter You name: ')
        self.__salair = int(input('How much money you want put in your compt: '))
    def crediter(self,creditSalaire=0):
        if creditSalaire > self.__salair:
            print('You will take ',self.__salair,'Dhs, Because this is all money in your compt','\nYour salaire in compte now is : ',0,' Dhs',sep='')
            self.__salair = 0
        else:
            self.__salair = self.__salair - creditSalaire
            print('You credit ',creditSalaire,'Dhs ,and stay in your compt ',self.__salair,' Dhs',sep='')
    def debiter(self,debiterSalaire=0):
        self.__salair = self.__salair + debiterSalaire
        print('your salaire now: ', self.__salair,' Dhs after add ',debiterSalaire,' Dhs',sep='')
    def affichage(self):
        print('Numero of compt is :', self.__numeroOfCmpte)
        print('Name of Property :', self.__nomOfPreprieter)
        print('Money on compt is :', self.__salair)
    
    
    @property
    def numeroOfCompte(self):
        return self.__numeroOfCmpte
    @numeroOfCompte.setter
    def numeroOfCompte(self,valuer):
        self.__numeroOfCmpte = valuer
    
        
    
    
    @property
    def nomOfPreprieter(self):
        return self.__nomOfPreprieter
    @nomOfPreprieter.setter
    def nomOfPreprieter(self,valuer):
        self.__nomOfPreprieter = valuer
    


    @property
    def salair(self):
        return self.__salair
    @salair.setter
    def salair(self,valuer):
        self.__salair = valuer
    

        