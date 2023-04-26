

class Date(object):
    def __init__(self,year:int=None,month:int=None,day:int=None):
        self.__year = year
        self.__month = month
        self.__day = day
        


    def fix(self,year:int=None,month:int=None,day:int=None):
        self.__year = year
        self.__month = month
        self.__day = day
        
    

    def affichage(self):
        return f"{self.__day}/{self.__month}/{self.__year}"
    

    def saisir(self):
        self.__year = int(input("Enter year: "))
        self.__month = int(input("Enter month: "))
        self.__day = int(input("Enter day: "))

        

