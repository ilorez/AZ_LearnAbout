def findDeuxMujWord(str):
    words = str.split(' ')
    T = []
    for word in words:
        count = 0
        for caracter in word:
            if 'A' <= caracter <= 'Z':
                count+=1
        if count > 1:
            T.append(word)
                
    return T


string = 'HI fin awa ghadi HoW wahd salamo aalikom ARE afin al3zawi ach yOU! somebody'
print(findDeuxMujWord(string))