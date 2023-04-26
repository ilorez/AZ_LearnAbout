from datetime import * 
print('year/month/day')
date1 = input('Enter date1: ')
print(date1)
date1 = date1.split('/')
date1 = datetime(int(date1[0]),int(date1[1]),int(date1[2]))
print(date1,'\n')
result1 = datetime.strftime( date1,"%A %m %b %y")
print(result1)


