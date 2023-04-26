# ************************************
# Ping Pong game
# ************************************
from tkinter import *
import random

GAME_WIDTH = 1280
GAME_HEIGHT = 600
SPEED = 10
SPACE_SIZE = 5
BALLE_COLOR = "#00FF00"
BRACKET_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

window = Tk()
window.title("PingPong")
window.resizable(True, True)

def change_direction(b):
    print("nice")

# label = Label(window, text="{} Vs {}".format(1,2), font=('consolas', 40))
# label.pack()

class PingPong:
    def __init__(self):
        pass

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()


x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")



window.bind('w', lambda event: change_direction('up'))
window.bind('s', lambda event: change_direction('down'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

wool_1 = Canvas(window,width=10,bg ="red",height=window_height)
wool_1.place(x=window_width-10,y=0)
wool_2 = Canvas(window,width=10,bg ="red",height=window_height)
wool_2.place(x=0,y=0)



window.mainloop()