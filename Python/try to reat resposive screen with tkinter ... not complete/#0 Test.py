from tkinter import *
import time
window = Tk()
window.resizable(True,True)
window['bg'] = "#333"

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = screen_width
window_height = screen_height
window.geometry(f'{window_width}x{window_height}+400+100')
window.update()
window.minsize('200','200')
window.mainloop()
