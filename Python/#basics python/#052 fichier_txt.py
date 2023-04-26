#open types 
'''
x   creat a fichier 
w   write with delete everything en fichier
r   read
a   contune writing en fichier without delete the content on it
'''




file = open('/home/najdaoui/Desktop/file1.txt','x')
file.close()
file = open('/home/najdaoui/Desktop/file1.txt','w',encoding='utf-8')
for i in range(4):
    file.write('hello word '+str(i+1) +'\n')
file.close()
file = open('/home/najdaoui/Desktop/file1.txt','r',encoding='utf-8')
lines = file.readlines()
file.close()
file = open('/home/najdaoui/Desktop/file1.txt','w',encoding='utf-8')
file.write(lines[0].rstrip('\n'))
file.close()
file = open('/home/najdaoui/Desktop/file1.txt','a',encoding='utf-8')
file.write(lines[1].rstrip('\n'))
file.close()







file = open('/home/najdaoui/Desktop/file1.txt','r',encoding='utf-8')
print(file.readlines())