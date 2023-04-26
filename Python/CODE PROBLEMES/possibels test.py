import math


def possible(t):
    Tab = []
    for i in range(len(t)):
        for j in range(len(t)-1):
            t[j],t[j+1] = t[j+1],t[j]
            Tab.append(t.copy())
    return Tab


T= []
for _ in range(int(input("len :"))):
    T.append(input(f"Char {_+1}: "))

t_repeat = [0 for i in range(len(T))]
t_poss_repeat = [math.factorial(len(T[:i])) for i in range(3,len(T))]
finalTable = []
for i in range(math.factorial(len(T))):
    T_edit = T.copy()
    for j in range(len(T)):
        
        t_repeat =[t_repeat[i]+1 for i in range(len(T))]














# print("_"*10)
# r = possible(T)
# for k in r:   
#     print(*k)

