import json
from colorama import Fore
import os

# Start
os.system('clear')
print(f"{Fore.BLUE}Bienvenue sur notre chatbot d'orientation ! Pour commencer, veuillez répondre aux questions suivantes pour nous aider à mieux comprendre vos intérêts, vos compétences et vos motivations. Nous utiliserons ces informations pour vous suggérer des options de carrière qui correspondent à votre personnalité. Nous vous remercions d'avance pour votre participation !\n{Fore.RESET}")
name = input(f"{Fore.GREEN}Enter your name : {Fore.RESET}")

#open file and put it in info att after convert json format to dic
with open('Data_Q.json',"r") as f:
    info = json.load(f)
tab = ["Devellopement Digital","Infrascracture digital","Marketing Digital","Design"]


# bring Q and his As and notes of ansowers from json file
q_num = -1
def get_info():
    global q_num
    q_num += 1
    return [list(info)[q_num],info[list(info)[q_num]]] # E:[quesiton , [true,{"ch1":[0,1,0,1]}]]

# show quesiont in screen and return answer
def display(q):
    os.system('clear')
    print(f"{Fore.YELLOW}{q[0]}")
    for i in range(len(list(q[1][1]))):
        print(f"{Fore.CYAN}\t{i+1}-",list(q[1][1])[i])
    
    if q[1][0]:
        c = input(f"{Fore.GREEN}your choose(s) : ")
        c = c.split(",")
        ans_select = {}
        for i in range(len(c)):
            ans_select[list(q[1][1])[int(c[i])-1]] = q[1][1][list(q[1][1])[int(c[i])-1]] #(XD) this code for take choix and his table of token that cheked and put in ans_select dict
        return [q[0],ans_select] # E:[quesiton ,{"ch1":[0,1,0,1]}] ? Only choix that user check

    c = int(input(f"{Fore.GREEN}your choose :"))
    ans_select = list(q[1][1])[c-1]
    # print([q[0],{ans_select:q[1][1][ans_select] }])
    return [q[0],{ans_select:q[1][1][ans_select] }] 
    

# best choi tab
final_tab = [0 for i in range(4)]
def filiers_notes(tab):
    global final_tab
    for i in range(len(final_tab)):
        final_tab[i] += tab[i]
    

# stock answers in csv file
def stock(data): # [q, {q1:[1,2,3,4]}]
    file = open("data.csv","a")
    if q_num == 0:
        file.write(f"Username:{name}\n")
    
    t = [0 for t in range(4) ]
    for i in range(len(list(data[1]))):
        for j in range(4):
            t[j] += data[1][list(data[1])[i]][j]
    filiers_notes(t)
    file.write(f"{data[0]};{list(data[1])};{t}\n")

    # add empty line between every personne and best felier
    if q_num+1 >= len(list(info)):
        file.write(f"^^^^^{tab[best_filier()]}^^^^^\n\n")
    print(f"{Fore.RESET}")
    file.close()


# best filier
def best_filier():
    return final_tab.index(max(final_tab))

# conrole info 
def controller():
    q_Info = get_info()
    q_Ans = display(q_Info)
    
    stock(q_Ans)
    if q_num+1 < len(list(info)):
        controller()
        return

controller()
print(f"Merci d'avoir utilisé notre chatbot d'orientation ! En fonction de vos réponses, nous avons identifié l’option de carrière suivante qui correspond à vos intérêts, vos compétences et vos motivations : {Fore.GREEN}{tab[best_filier()]}{Fore.RESET}. Nous vous encourageons à explorer cette option pour en savoir plus sur elle, et à consulter des professionnels pour obtenir des conseils sur la façon de poursuivre cette carrière. Nous espérons que cette expérience vous a été utile et vous a aidé à explorer de nouvelles idées pour votre avenir professionnel.")