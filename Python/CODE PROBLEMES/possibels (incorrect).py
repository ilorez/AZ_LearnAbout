import math
print("the code false because idea of it not true. from basic was false :( .i spend a lot of time in incorrect idea :'< .")
# print(math.factorial(4))
# def possible(t):
#     global Tab ,t_repeat
#     print(t_repeat)
#     for i in range(math.factorial(len(t))):
#         for q in range(t_repeat[i]):
#             if t_repeat[q] >= len(t_repeat[:q]):
#                 t_repeat[q] = 0
#         j = t[t_repeat.index(0)-1]
#         t_repeat[t_repeat.index(0)-1] += 1
#         t[j],t[j+1]=t[j+1],t[j]
#         Tab.append(t.copy())

t= []
for _ in range(int(input("len :"))):
    t.append(input(f"Char {_+1}: "))

Tab = []
t_repeat = [0 for i in range(len(t))]
t_possible_repeat = [i+1 for i in range(len(t))]
print(t_possible_repeat)
i = 0
while i < math.factorial(len(t)):
    t = t.copy()
    
    Tab.append(t.copy())
    # print(*t.copy())
    for q in range(len(t_repeat)):
        
        j = q
        if t_repeat[q] == t_possible_repeat[q]:
            continue

        t_repeat[j] += 1
        if t_repeat[q] <= t_possible_repeat[q]:
            for o in range(len(t_repeat[:q])):
                t_repeat[o] = 0
                
        if q == len(t_repeat)-1:
            j = -1 
            t_repeat[j] += 1
        break
        
    # t_repeat[j] += 1
    t[j],t[j+1]=t[j+1],t[j]
    i+=1

# t[i],t[i+1] = t[i+1],t[i]
print("_"*10)
for k in Tab:   
    print(*k)

