from tkinter import *
from DesigneOXG import *


def Start_Game(typ,s_tab):
    window.destroy()
    print(typ,s_tab)
    play = Designe(s_tab[0],s_tab[1],s_tab[2])
    play.set_designe()


window = Tk()
window.title('XOG')
window.geometry('545x330+400+100')
window.resizable(False, False)
window['bg'] = "#333"


lbl_set_color = Label(text='Set colors :',font=('Arial', 25), bg='#333', fg='#fff').place(x=200,y=20)

lbl_player1_color = Label(text='Player 1:',font=('Arial', 20), bg='#333', fg='#fff').place(x=10,y=100)
lbl_player2_color = Label(text='Player 2:',font=('Arial', 20), bg='#333', fg='#fff').place(x=250,y=100)
input_player1_color = Entry(justify='center',width=10)
input_player1_color.place(x=130,y=105)
input_player2_color = Entry(justify='center',width=10)
input_player2_color.place(x=370,y=105)

lbl_background_color = Label(text='Background:',font=('Arial', 20), bg='#333', fg='#fff').place(x=10,y=180)
input_background_color = Entry(justify='center',width=10)
input_background_color.place(x=250,y=185)
lbl_error = Label(text='',font=('Arial', 12), bg='#333', fg='#d00')
lbl_error.place(x=10,y=220)


#this function for get all entrys and put in tab and put this tab in parammetrs of Start_Game() function
def Call_Setting(ty):
    setting_tap = [input_player1_color.get(),input_player2_color.get(),input_background_color.get()]
    for i in range(len(setting_tap)):
        if setting_tap[i]== '':
            lbl_error['text']= 'Enter all informations ! '
            return
    if (setting_tap[0] == setting_tap[2])or (setting_tap[1] == setting_tap[2]):
        lbl_error['text']= 'background color can\'t = color of an player'
        return
    Start_Game(ty,setting_tap)


btn_player_vs_player = Button(text = 'Player vs Player',font=('Arial', 20), bg='#333', fg='#fff',width=15,command=lambda:Call_Setting(1)).place(x=10,y=260)
btn_player_vs_player = Button(text = 'Player vs Computer',font=('Arial', 20), bg='#333', fg='#fff',command=lambda:Call_Setting(2)).place(x=275,y=260)








window.mainloop()