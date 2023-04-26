import tkinter
import customtkinter
import json



WINDOW_HEIGHT = 720
WINDOW_WIDTH = 1280


#* Get window and screen info
window_width = WINDOW_WIDTH

window_height = WINDOW_HEIGHT

# loads json file
with open('Data_Q.json',"r") as f:
    info = json.load(f)


# give you first Question with his choixs and table of notes
q_num = -1
def get_info():
    global q_num
    q_num += 1
    result =  [list(info)[q_num],info[list(info)[q_num]]] 
    # E:[quesiton , [true,{"ch1":[0,1,0,1]}]
    return result

# sum of all notes tab
final_tab = [0 for i in range(4)]
def filiers_notes(tab):
    global final_tab
    for i in range(len(final_tab)):
        final_tab[i] += tab[i]
# max index notes
def best_filier():
    return final_tab.index(max(final_tab))
tab = ["Devellopement Digital","Infrastracture Digital","Marketing Digital","Design"]

# stock infos
def stock(): # [q, [true,{q1:[1,2,3,4]}]]
    global var_stock, questions_choixs
    select_items = {}

    #! Single Choix
    if questions_choixs[1][0] == False : 
            print(var_stock[0].get())
            select_items[ list(questions_choixs[1][1])[var_stock[0].get()-1]] = questions_choixs[1][1][list(questions_choixs[1][1])[var_stock[0].get()-1]]

    #! Multiple Choix
    elif questions_choixs[1][0] == True : 
        for i in range(len(var_stock)):
            print(var_stock[i].get())
            if var_stock[i].get() == 1:
                select_items[ list(questions_choixs[1][1])[i]] = questions_choixs[1][1][list(questions_choixs[1][1])[i]]
       
    data = [questions_choixs[0],select_items]
    print(data)
    file = open("data.csv","a",encoding='utf-8')
    if q_num == 0:
        file.write(f"\nUsername: {app.title()}\n")
    t = [0 for t in range(4) ]
    for i in range(len(list(data[1]))):
        for j in range(4):
            t[j] += data[1][list(data[1])[i]][j]
    filiers_notes(t)
    file.write(f"{data[0]};{list(data[1])};{t}\n")
    
    file.close()
    if q_num+1 < len(list(info)):
        lbl_q.place_forget()
        for _ in del_ch:
            _.place_forget()
        display()
        return
    
    #! Display Finale Result
    else :
        file = open("data.csv","a",encoding='utf-8')
        file.write(f"Best Filiere ; <<<< {tab[best_filier()]} >>>>\n")

        lbl_q.place_forget()
        for _ in del_ch:
            _.place_forget()
        btn.place_forget()
        
        frm = customtkinter.CTkFrame(master=app,height=650,width=1200,corner_radius=20)
        frm.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)

        text0 = customtkinter.CTkLabel(master=frm,text=f"Merci d'avoir utilisé notre chatbot d'orientation ! En fonction de vos réponses, \nnous avons identifié l’option de carrière suivante qui correspond à vos intérêts, \nvos compétences et vos motivations :",font=("Arial",25))
        text0.place(relx=0.5,rely=0.25,anchor=tkinter.CENTER)
        text1 = customtkinter.CTkLabel(master=frm,text=f"{tab[best_filier()]}.",font=("Arial",30),text_color="#0a5")
        text1.place(relx=0.5,rely=0.4,anchor=tkinter.CENTER)
        text2 = customtkinter.CTkLabel(master=frm,text=f"Nous vous encourageons à explorer cette option pour en savoir plus sur elle, \net à consulter des professionnels pour obtenir des conseils sur la façon \nde poursuivre cette carrière. Nous espérons que cette expérience vous a été utile et \nvous a aidé à explorer de nouvelles idées pour votre avenir professionnel.",font=("Arial",25))
        text2.place(relx=0.5,rely=0.6,anchor=tkinter.CENTER)





def display():
    global questions_choixs,lbl_q,del_ch,btn
    app.title(entry.get())
    text.place_forget()
    entry.place_forget()
    btn0.place_forget()
    questions_choixs = get_info()

    # Display questions
    lbl_q = customtkinter.CTkLabel(master=app,text=f"{questions_choixs[0]}",font=("Arial",29),text_color="#f70")
    lbl_q.place(relx=0.05,rely=0.1)

    # Display Choix
    del_ch = []
    y = 0.12
    global var_stock
    var_stock = [tkinter.IntVar() for i in range(9)]


    #! Multiple Choix
    choixs = list(questions_choixs[1][1])
    if questions_choixs[1][0] == True :
        for i,v in enumerate(choixs) :
            var_stock[i].set(0)
            chk = customtkinter.CTkCheckBox(master=app,text=f"{i+1}-{v}",variable=var_stock[i],onvalue=1,offvalue=0,font=("Arial",20))
            del_ch.append(chk)
            y += 0.05
            chk.place(relx=0.2,rely=y)

    #! Single Choix
    elif questions_choixs[1][0] == False : 
        s = tkinter.IntVar()
        var_stock = [s]
        var_stock[0].set(0)
        for i,v in enumerate(choixs) :
            chk = customtkinter.CTkRadioButton(master=app,text=f"{i+1}-{v}",variable=var_stock[0],value=i+1,font=("Arial",20))
            del_ch.append(chk)
            y += 0.05
            chk.place(relx=0.2,rely=y)

    if q_num == 0:
        btn = customtkinter.CTkButton(master=app,text="Send",font=("Arial",50),corner_radius=10,command=stock)
        btn.place(relx=0.92,rely=0.92,anchor=tkinter.CENTER)
    




customtkinter.set_appearance_mode('systeme') #can set light or dark
customtkinter.set_default_color_theme("green") #themes: blue, dark-blue or green

app = customtkinter.CTk() # creating custom tkinter window

app.resizable(False,False)
app.title("ChatBot")


screen_width = app.winfo_screenwidth()

screen_height = app.winfo_screenheight()

#* Center a window
x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))
app.geometry(f"{window_width}x{window_height}+{x}+{y}")


text = customtkinter.CTkLabel(master=app,text="Bienvenue sur notre chatbot d'orientation !\nPour commencer, veuillez répondre aux questions suivantes \npour nous aider à mieux comprendre vos intérêts, vos compétences \net vos motivations. Nous utiliserons ces informations \npour vous suggérer des options de carrière qui correspondent \nà votre personnalité. Nous vous remercions d'avance pour votre participation !\n\n\n\n\nEnter your name:",font=("Arial",25))
text.place(relx=0.5,rely=0.4,anchor=tkinter.CENTER)

entry = customtkinter.CTkEntry(master=app,height=50,width=300,font=("Arial",50))
entry.place(relx=0.5,rely=0.7,anchor=tkinter.CENTER)

btn0 = customtkinter.CTkButton(master=app,text="Start",font=("Arial",50),corner_radius=10 ,command=display)
btn0.place(relx=0.92,rely=0.92,anchor=tkinter.CENTER)



app.mainloop()