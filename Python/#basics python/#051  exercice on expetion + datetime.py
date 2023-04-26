from datetime import *
'''
this a exercice for take to date 
date one for coming date and date2 for going date
oui see if this date input correct using exeption 
and see if date comiong < date going 
just...
'''




print('Enter with THis format year/month/day')
date_coming = input('Enter coming date: ')
date_going = input('Enter going date: ')

date_coming = date_coming.split('/')
date_going = date_going.split('/')

for i in range(3):
    date_coming[i] = int(date_coming[i])
    date_going[i] = int(date_going[i])

try:
    date_coming = datetime(date_coming[0],date_coming[1],date_coming[2])
    date_going = datetime(date_going[0],date_going[1],date_going[2])
    
    if(date_coming<date_going):
        print('nice')
    else:
        print('date de coming >= date de going !!!')
except:
    print('your dates not corrcety enter valid date')
