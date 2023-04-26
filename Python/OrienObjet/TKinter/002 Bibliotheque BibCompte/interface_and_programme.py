from tkinter import *
from tkinter import ttk
import customtkinter

WIDTH = 1300
HEIGTH = 600
window = Tk()
window.title('Bibliotheque')
window.geometry(f'{WIDTH}x{HEIGTH}')
window.config(bg='#ccc')

# TODO  numero id
ID = 0
idLbl = Label(window,text="Numeros: ")
idLbl.grid(column=1,row=1,padx=20,pady=10)

idValue = Label(window,text=f"{ID}",fg="#777")
idValue.grid(column=2,row=1,padx=20,pady=10)

# TODO Proprietaure:
proLbl = Label(window,text="Proprietaire: ")
proLbl.grid(column=1,row=2,padx=20,pady=10)

proInp = Entry(window, width=20)
proInp.grid(column=2,row=2)



# TODO Solde Initial
soldInLbl = Label(window,text="Solde Inial: ")
soldInLbl.grid(column=1,row=3,padx=20,pady=10)

soldInInp = Entry(window, width=20)
soldInInp.grid(column=2,row=3)

proLbl = Label(window,text="Dhs")
proLbl.grid(column=3,row=3,padx=20,pady=10)



# TODO Type
typeLbl = Label(window,text="Type: ")
typeLbl.grid(column=1,row=4,padx=20,pady=10)

typeValue = StringVar()

# rb1 = Radiobutton(window, text="Option 1", variable=var, value="1")
# rb1.grid(column=2,row=4,padx=20,pady=10)

# rb2 = Radiobutton(window, text="Option 2", variable=var, value="2")
# rb2.grid(column=3,row=4,padx=20,pady=10)
chk1 = customtkinter.CTkRadioButton(window,text="Courant",value="Courant",variable=typeValue,text_color="#000")
chk2 = customtkinter.CTkRadioButton(window,text="Epargne",value="Epargne",variable=typeValue,text_color="#000")
chk1.grid(column=2,row=4,padx=20,pady=10)
chk2.grid(column=3,row=4,padx=20,pady=10)

# TODO Taux Interet
tauxLbl = Label(window,text="Taux Interet: ")
tauxLbl.grid(column=1,row=5,padx=20,pady=10)

tauxInp = Entry(window, width=20)
tauxInp.grid(column=2,row=5) 

tauxLbl = Label(window,text="%")
tauxLbl.grid(column=3,row=5,padx=20,pady=10)

# TODO M. Decouvert
decouLbl = Label(window,text="M. Decouvert: ")
decouLbl.grid(column=1,row=6,padx=20,pady=10)

decouInp = Entry(window, width=20)
decouInp.grid(column=2,row=6)



#! table
# Create the frame inside the window
frame = Frame(window)
frame.grid(column=1,row=8,padx=20,pady=10,columnspan=30)

# Create the treeview widget with two columns
THeadrs = ['Numero', 'Proprietaire', 'solde lnitial', 'type', 'Taux Interet','Montant Decouvert']
table = ttk.Treeview(frame, columns=tuple(THeadrs))
# Define the headings for the columns
for i in range(len(THeadrs)):
    table.heading(f'{THeadrs[i]}', text=f'{THeadrs[i]}')
for col in table["columns"]:
    table.column(col, width=170, stretch=False)
# Pack the table widget into the frame
table.pack()

#! get & set info funtions
def setInfo(T):
    # Insert some data into the table
    table.insert('', 'end', text=' ', values=tuple(T))

def getInfo():
    global ID
    setInfo([ID,proInp.get(),soldInInp.get(),typeValue.get(),tauxInp.get(),decouInp.get()])
    ID+=1
    idValue['text'] = ID
    window.update()
    
# TODO Button Create compte

btn = Button(window, text='Creation Compte', command=getInfo)
btn.grid(column=2,row=7,padx=20,pady=10)


window.mainloop()