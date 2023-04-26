
## py for code string 

tab = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
str = input('string:').upper()
list_str = list(str)
''' 
It's important here make a copy of str by add copy method
because we wan't list_str_copy take same referece of list_str
'''
list_str_copy = list_str.copy()


for i in range(len(list_str)):
    '''
    we need to skip spaces because in this code we not code it
    '''
    if list_str[i] == ' ':
        continue
    times = list_str.count(list_str[i])
    if times % 2 == 0:
        list_str_copy[i] = tab[((tab.index(list_str[i])) + times//2 )%26]
        
    else:
        list_str_copy[i] = tab[((tab.index(list_str[i])) + times*2 )%26]
    
str_after_code =''.join(list_str_copy)
print(str_after_code)
'''
    index(): give you index of an element by his value
    count(): tell you how much this elemet repeated in the list
    join(): convert list to string
'''

