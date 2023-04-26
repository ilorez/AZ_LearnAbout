str = ' learning to program in python is easier than leaning to program in java'
file  = open("file.txt", 'x', encoding='utf8')
file.close()
file  = open("file.txt", 'w', encoding='utf8')
file.write(str)
file.close()
def IsFound(mot):
    file  = open("file.txt", 'r', encoding='utf8')
    myFileTxt = file.read()
    if mot in myFileTxt.split(' '):
        print(myFileTxt.split(' ').count(mot))
    else:
        print(mot,'not FOund')
    file.close()
IsFound('in')
