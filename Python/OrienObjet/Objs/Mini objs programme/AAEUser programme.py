from AAEUser import User
per1 = User()
per2 = User('salma','salmaPassword')
per3 = User()
per4 = User()

per1.name_ = 'mehdi'
per1.password_ = 'mehdipassword'
per1.affichage()

print(per2)

per3.saisir()
print(per3)

User.number_of_compte()

per4.affichage()