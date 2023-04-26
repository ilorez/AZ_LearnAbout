from datetime import *

#today time
today = datetime.now()
print(today)

#cutom date
myBirth = datetime(2003,8,25)
print('myBirth: ',myBirth)

#change format
print(today.year,today.month,today.day,sep='/')

#legal format codes
'''
%a weekday short version ex:wed
%A weekday fall version ex:wednesday
%d day of month 0-31 ex:31
%b month short version ex:dec
%B month fall version ex:december
%m month as number 01-12 ex:12
%y year short version ex:2018=>18
%Y year fall version ex:2018
%H hour 00-23 ex:15
%I hour 00-12 ex:05
%p AM/PM ex:PM
%M minute 00-59 ex:41
%S second 00-59 ex:49
...
'''


