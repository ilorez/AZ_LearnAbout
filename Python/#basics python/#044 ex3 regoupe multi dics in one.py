def sumDics(listOfDic):
    dicTotal = {}
    for dic in listOfDic:
        for k,v in dic.items():
            if (k in dicTotal):
                dicTotal[k] += v
            else:
                dicTotal[k] = v
    return dicTotal

dicPc = {'HP':11,'Acer':7,'Lenovo':17,'Del':23}
dicPhone = {'Sumsung':22,'Iphone':9,'Other':23}
dicTablette = {'Sumsung':15,'Other':13}

ListOfDic = [dicPc , dicPhone , dicTablette]
print(sumDics(ListOfDic))