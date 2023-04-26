from AAFLivre import *
Tab_livres = []
for i in range(4):
    livre = Livre()
    Tab_livres.append(livre)

# livre1 = Livre('livre titre','livre acteur','livre pri','livre annee')
# livre1.affichage()
Tab_livres[0].affichage()
print('____________________________')
Tab_livres[1].titre = 'titre de livre'
Tab_livres[1].auteur = 'auteut de livre'
Tab_livres[1].prix = 'prix de livre'
Tab_livres[1].annee = 'annee de livre'
Tab_livres[1].affichage()
print('____________________________')
livre2 = Livre()
livre2.affichage()
