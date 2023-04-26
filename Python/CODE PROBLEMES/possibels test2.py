import math

T= []
for _ in range(int(input("len :"))):
    T.append(input(f"Char {_+1}: "))



t_repeat = [0 for i in range(len(T))]
t_poss_repeat = [len(T[:i]) for i in range(len(T))]
f_Tab = []

times = math.factorial(len(T))
i = 0 
pos = 0

while True:
    if len(f_Tab) == times:
         break
    T_edit = T.copy()
    T_edit[pos],T_edit[pos - t_repeat[pos-1]+1]=T_edit[pos - t_repeat[pos-1]+1],T_edit[pos]
    print(T_edit.copy())
    f_Tab.append(T_edit.copy())
    if t_poss_repeat[pos] == t_repeat[pos]:
        pos += 1
        
        continue

    # T_edit[pos],T_edit[pos - t_repeat[pos]+1]=T_edit[pos - t_repeat[pos]+1],T_edit[pos]
    
    t_repeat[pos] += 1
    i+= 1
    if t_poss_repeat[pos] > t_repeat[pos]:
        
        for o in range(len(t_repeat[:pos])):
                t_repeat[o] = 0
        pos = 0
    
    
        
    










print("_"*10)

for k in f_Tab:   
    print(*k)

