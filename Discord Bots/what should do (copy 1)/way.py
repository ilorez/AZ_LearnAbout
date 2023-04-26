import json


# Start

#open file and put it in info att after convert json format to dic
with open('Data_Q.json',"r") as f:
    info = json.load(f)
tab = ["Devellopement Digital","Infrascracture digital","Marketing Digital","Design"]


# bring Q and his As and notes of ansowers from json file
async def get_info(q_nu,user):
    global q_info
    globals()[f"q_num{user.replace('#','')}"] = q_nu
    
    print("_"*10)
    print(q_nu)
    print(len(list(info)))
    print("_"*10)

    q_info = [list(info)[q_nu],info[list(info)[q_nu]]] # E:[quesiton , [true,{"ch1":[0,1,0,1]}]]
    return q_info
async def r_q_num(user,n = -1):
    
    globals()[f"q_num{user.replace('#','')}"] = n

async def fetch_q_num(user):
    return globals()[f"q_num{user.replace('#','')}"]

async def stock_name(name):
    global f_u_data
    f_u_data = {}
    with open(f"./data/{name}.json","w") as f:
        pass

async def filter_answer(choix,tab):
    t = {}
    for index in tab:
        t[list(choix)[index]] = choix[list(choix)[index]]
    return t

async def last_question(user):
    if globals()[f"q_num{user.replace('#','')}"]+1 == len(list(info)):
        return True
    return False

async def stock(username,tab):
    f_u_data[q_info[0]]= await filter_answer(q_info[1][1],tab)
    if await last_question():
        with open(f"./data/{username}.json","a") as f:
            json.dump(f_u_data,f ,ensure_ascii=False)
        
