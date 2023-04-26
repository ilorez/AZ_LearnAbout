
class Personne(object):
    tab_per =[]
    def __init__(self,nom:str=None,prenom:str=None,age:int=None,code:str=None):
        self.__nom = nom
        self.__prenom = prenom
        self.__code = code
        self.__age = age
    def getInfo(self):
        return f"Info:\
                \n\tNom:{self.__nom}\
                \n\tPrenom:{self.__prenom}\
                \n\tAge:{self.__age}\
                \n\tCode:{self.__code}"
    # ajout an peronne to tab_per
    def loopy():
        c = str(input("Code: "))
        found = False
        for p in Personne.tab_per:
            if p.code == c:
                return p
        
        print("ne pas exist.")
        return
    def ajout():
        print("_"*10,"Ajout","_"*10)
        n = str(input("Nom:"))
        p = str(input("Prenom:"))
        a = int(input("Age:"))
        c = str(input("Code:"))
        per = Personne(n,p,a,c)
        Personne.tab_per.append(per)
    
    # cherche un persone en tab_per avec code
    def cherche():
        print("_"*10,"cherche","_"*10)
        t = Personne.loopy()
        if t:
            print(t.getInfo())
        
    # modifier un nom de personne from tab_per avec code
    def modifier():
        print("_"*10,"Modifier","_"*10)
        t = Personne.loopy()
        if t:
            n = str(input("Nouveu nom: "))
            t.nom = n
            print("done")
        
    # suprimme un personne from tab_per avec code
    def supprime():
        print("_"*10,"Suprime","_"*10)
        t = Personne.loopy()
        if t:
            Personne.tab_per.remove(t)
            print("done")
        
    # affiche nombre des personne en list tab_per
    def count():
        print("_"*10,"Number des personnes","_"*10)
        print(len(Personne.tab_per))
    
    #affiche catigory de personne en list tab_per (petite,jeune,grand)
    def catigory():
        print("_"*10,"Catigory","_"*10)
        t = Personne.loopy()
        if t:
            if t.age <= 18:
                print("P")
            elif t.age > 18 and t.age <= 35:
                print("j")
            else:
                print("g")
        
    #affiche ifo de chaque personne en list tab_per
    def affichage():
        print("_"*10,"Affichage","_"*10)
        found = False
        for p in Personne.tab_per:
            print(p.getInfo())
            found = True
           
        if not found:
            print("ne peronne exist.")

    #getters and setters
    #nom
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, valuer):
        self.__nom = valuer
    
    #prenom
    @property
    def prenom(self):
        return self.__prenom
    @prenom.setter
    def prenom(self, valuer):
        self.__prenom = valuer
    
    #age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, valuer):
        self.__age = valuer
    
    #code
    @property
    def code(self):
        return self.__code
    @code.setter
    def code(self, valuer):
        self.__code = valuer
