class User:
    __contuer = 0
    def __init__(self,name=None,password=None):
        self.__name = name
        self.__password = password
        User.contuer_()
        # User.__contuer += 1

    @classmethod
    def contuer_():
        User.__contuer += 1


    def saisir(self):
        self.__name = input('Enter your name: ')
        self.__password = input('Enter password: ')
    
    def affichage(self):
        print(f'I am {self.__name}, and my passwrod is {self.__password}.')

    def __str__(self):
        return (f'I am {self.__name}, and my passwrod is {self.__password} and number of all users is {User.__contuer}')

    @classmethod
    def number_of_compte(cls):
        print('number of compet is : ',User.__contuer)
    
    #edit name
    @property
    def name_(self):
        return self.__name
    @name_.setter
    def name_(self, valuer):
        self.__name = valuer

    # edit password 
    @property
    def password_(self):
        return self.__password
    @password_.setter
    def password_(self, valuer):
        self.__password = valuer