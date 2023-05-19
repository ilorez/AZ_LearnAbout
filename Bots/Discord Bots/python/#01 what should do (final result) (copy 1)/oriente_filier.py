import json
with open('Data_Q.json',"r") as f:
    info = json.load(f)
class OrieteF(object):
    def __init__(self,name:str) -> None:
        self.__name = name
        self.__q_num = -1
        self.__final_data = {}
        self.__done = False
        with open(f"./data/{self.__name}.json","w") as f:
            pass
    
    def get_info(self):
        self.__q_num += 1
        return [list(info)[self.__q_num],info[list(info)[self.__q_num]]] # E:[quesiton , [true,{"ch1":[0,1,0,1]}]]

    def get_q_c(self):
        self.__q_num_info = self.get_info()
        q_c = self.__q_num_info[0]
        for i in range(len(list(self.__q_num_info[1][1]))):
            q_c += f"\n   {i+1}-{list(self.__q_num_info[1][1])[i]}"
        if self.__q_num == 0:
            q_c += "\nSélectionnez vos réponses parmi les choix ci-dessus.\n`Example:1`\nVous pouvez sélectionner plusieurs choix seulement pour certaines questions.\n`Example:1,3,5`"
        return q_c 
    def stock(self,username,check):
        if not(self.__q_num_info[1][0]):
            check = [check[0]]
        t = {}
        list_choix = list(self.__q_num_info[1][1])
        for index in check:
            t[list_choix[index]] = self.__q_num_info[1][1][list_choix[index]]
    
        self.__final_data[self.__q_num_info[0]]= t
        if self.__q_num+1 == len(list(info)):
            self.__done = True
            with open(f"./data/{username}.json","a") as f:
                json.dump(self.__final_data,f ,ensure_ascii=False)
    
    def done(self):
        return self.__done

    

    
