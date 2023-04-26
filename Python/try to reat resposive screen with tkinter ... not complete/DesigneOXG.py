from tkinter import *
import time
class Designe:
    def __init__(self,p1c='red',p2c='blue',b='black'):
        self.__p1color = p1c
        self.__p2color = p2c
        self.__background = b
        if b == 'black':
            self.__color = 'white'
        else:
            self.__color = 'black'


        
   
    def set_designe(self):
        def set_x_o(num):
            print('hi',num)
        window = Tk()
        window.title('XOG')
        window.resizable(True,True)
        window['bg'] = self.__background
        #take screen width
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        window_width = screen_width
        window_height = screen_height
        window.geometry(f'{window_width}x{window_height}+400+100')
        window.update()
        window_width = window.winfo_width()
        window_height = window.winfo_height()
        print(window_width,window_height)
        
        #put here all frms and button without (width/height/place)

        # Frames
        
        frm_player2 = Canvas(bg=self.__background)
        frm_main = Frame(bg=self.__background)
        frm_player1 = Canvas(bg=self.__background)
        # columns
        column1 = Frame(frm_main,bg=self.__color)
        column2 = Frame(frm_main,bg=self.__color)
        # rows
        row1 = Frame(frm_main,bg=self.__color)
        row2 = Frame(frm_main,bg=self.__color)
        
        
        def set_resposive():
            
            while True:
                
                
                window_width = window.winfo_width()
                window_height = window.winfo_height()
                window.update()
                
                
                #player1
                player_can_w = window_width
                player_can_h = window_height/10
                frm_player1['width']=player_can_w
                frm_player1['height']=player_can_h
                frm_player1.place(x=0,y=0)
                #player2
                frm_player2['width']=player_can_w
                frm_player2['height']=player_can_h
                frm_player2.place(x=0,y=window_height-(player_can_h))
                #main
                
                main_h = window_height-(window_height/4)
                main_w = main_h
                window.minsize(f'{int(round(main_h,0))}','100')
                frm_main['width']=main_w 
                frm_main['height']=main_h 
                frm_main.place(x=(window_width -main_w)/2,y=window_height/8)
                
                #columns
                    #1
                column1['width']=main_w/240
                column1['height']=main_h
                column1.place(x=main_w/3,y=0)
                    #2
                column2['width']=main_w/240
                column2['height']=main_h
                column2.place(x=(main_w/3)*2,y=0)
                #rows
                    #1
                row1['width']=main_w
                row1['height']=main_w/240
                row1.place(x=0,y=main_h/3)
                    #2
                row2['width']=main_w
                row2['height']=main_w/240
                row2.place(x=0,y=(main_h/3)*2)

                #player 1 and 2 
                try:
                    frm_player1.delete('profile')
                    frm_player2.delete('profile')
                except:
                    pass
                    #1
                frm_player1.create_oval(player_can_h/10, player_can_h/10,player_can_h-(player_can_h/10) ,player_can_h-(player_can_h/10), fill=self.__p1color,tags='profile')
                frm_player1.create_text(player_can_h-(player_can_h/10)+50 ,player_can_h/2,text='Player 1',tags='profile',fill=self.__color)
                    #2
                frm_player2.create_oval(player_can_h/10, player_can_h/10,player_can_h-(player_can_h/10) ,player_can_h-(player_can_h/10), fill=self.__p2color,tags='profile')
                frm_player2.create_text(player_can_h-(player_can_h/10)+50 ,player_can_h/2,text='Player 2',tags='profile',fill=self.__color)
                
                
                
                
                window.update()
                time.sleep(0.01)
        set_resposive()