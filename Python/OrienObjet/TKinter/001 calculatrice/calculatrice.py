from tkinter import *

# methods
def plus():
    result['text']= str(int(ent_nb1.get())+int(ent_nb2.get()))
def moins():
    result['text']= str(int(ent_nb1.get())-int(ent_nb2.get()))
def divise():
    result['text']= str(int(ent_nb1.get())/int(ent_nb2.get()))
def fois():
    result['text']= str(int(ent_nb1.get())*int(ent_nb2.get()))

# interface

WIDTH = 500
HEIGTH = 400
wind =Tk()
wind.title('calculatrice')
wind.geometry(f'{WIDTH}x{HEIGTH}')
wind.config(bg='#ccc')
lbl_nb1 = Label(wind,text='Nombre 1 : ')
lbl_nb1 .grid(column=1,row=1,columnspan=2,padx=20,pady=20)
lbl_nb2 = Label(wind,text='Nombre 2 : ')
lbl_nb2 .grid(column=1,row=2,columnspan=2,padx=20,pady=20)
lbl_res = Label(wind,text='Resultat : ')
lbl_res.grid(column=1,row=4,columnspan=2,padx=20,pady=20)
ent_nb1 = Entry(wind)
ent_nb1.grid(column=3,row=1,columnspan=2,padx=20,pady=20)

ent_nb2 = Entry(wind)
ent_nb2.grid(column=3,row=2,columnspan=2,padx=20,pady=20)
result = Label(wind,font='red')
result.grid(column=3,row=4,columnspan=2,padx=20,pady=20)



btn_puls = Button(wind,text='+',command=plus)
btn_puls.grid(column=1,row=3,padx=20,pady=20)
btn_mois = Button(wind,text='-',command=moins)
btn_mois.grid(column=2,row=3,padx=20,pady=20)

btn_divise = Button(wind,text='/',command=divise)
btn_divise.grid(column=3,row=3,padx=20,pady=20)
btn_fois = Button(wind,text='x',command=fois)
btn_fois.grid(column=4,row=3,padx=20,pady=20)

wind.mainloop()