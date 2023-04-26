from tkinter import *
import time
# ------------
def possiblePositions(n):
    
    possibel_position = Frame(game_frm, width='80',height='80',bg='#a22')
    possibel_position.place(x=dama_cordonne[0][0],y=dama_cordonne[0][1])
    
    

def moveFun(n):
    possiblePositions(n)
    pass
# ------------
window = Tk()
window.title('Dama')
window.geometry('1200x680+0+0')
window.resizable(False, False)
window['bg'] = "#333"
game_frm = Frame(window,width='960',height='640',bg='#fff')
game_frm.place(x=120,y=20)
#dama face----------------------------------------------
dama_cordonne = []
for i in range(0,12,2):
    for j in range(0,8):
        o = 0
        if not(j%2 == 0):
            o = 80
        black_box = Frame(game_frm, width='80',height='80',bg='#000')
        black_box.place(x=i*80+o,y=j*80)
        dama_cordonne.append([i*80+o,j*80])
#order tab--------------------------------------------
t0 = []
for i in range(0,len(dama_cordonne),8):
    t1 = []
    t2 = []
    for j in range(i,i+8,2):
        t1.append(dama_cordonne[j])
        t2.append(dama_cordonne[j+1])
    t0 += t1 + t2
dama_cordonne = t0
    
#----------------------------------------------
#---------------------label
for i in range(len(dama_cordonne)):
    lbl_left_to_right_order = Label(game_frm,text=str(i+1),fg='#fff',bg='#000')
    lbl_left_to_right_order.place(x=dama_cordonne[i][0],y=dama_cordonne[i][1])
    lbl_right_to_left_order = Label(game_frm,text=str(i+1),fg='#fff',bg='#000')
    lbl_right_to_left_order.place(x=dama_cordonne[len(dama_cordonne)-i-1][0],y=dama_cordonne[len(dama_cordonne)-i-1][1]+20)
#---------------------label
#ghla9at coca-------------------------------------
for i in range(0,12):
    btnCoca = Button(game_frm,bg='#f00',text='COCA',command=lambda:moveFun(1))
    btnCoca.place(x=dama_cordonne[i][0]+8,y=dama_cordonne[i][1]+25)
for i in range(0,12):
    btnBota = Button(game_frm,bg='#0f0',text='Bota',command=lambda:moveFun(-1))
    btnBota.place(x=dama_cordonne[len(dama_cordonne)-i-1][0]+8,y=dama_cordonne[len(dama_cordonne)-i-1][1]+25)


print(dama_cordonne)
window.mainloop()