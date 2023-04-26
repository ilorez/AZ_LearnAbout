lignes = [['Nom', 'Prénom', 'Age'], ['Benhanouch','hatim', 21], ['Ait abdellah', 'ismail', 18],['Hamza', 'Abdelah', 15],['Youssef', 'najdaoui', 20],['Ghebbari', 'Anas', 29]]
ptrWrite = open("file#2.csv", 'w', encoding='utf8')
for i in range(len(lignes)): 
    lignes[i][2] = str(lignes[i][2])
    ptrWrite.write(';'.join(lignes[i])+'\n')
ptrWrite.close()
