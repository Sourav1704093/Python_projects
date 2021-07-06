from tkinter import Label,Tk 
import time

window = Tk()
window.title("Digital Clock")
window.geometry("420x160")
window.resizable(1,1)

text_font = ("Boulder",65,'bold')
background = "#f2e750"
foreground = "#363529"
border_width = 25

label = Label(window,font = text_font,bg = background,fg= foreground, bd = border_width)
label.grid(row = 0,column=1)

def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text = time_live)
    label.after(200,digital_clock)
    
digital_clock()
window.mainloop()