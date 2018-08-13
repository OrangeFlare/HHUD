from tkinter import Tk, Label
from random import randint

root = Tk()
root.configure(background='black')

# https://gist.github.com/TravisJoe/5576258
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.focus_set()
root.bind("<Escape>", lambda e: e.widget.quit())

speed = Label(root)
speed.pack()

def speedometer():
    speedData = randint(0,60)
    speedText = str(speedData)+" mph"
    speed.config(text=speedText, bg='black', fg='#F4511E', font=("Helvetica", 72, "bold"))
    speed.place(anchor='center', relx=0.5, rely=0.5)
    root.after(1000, speedometer) # Update speedometer every second

speedometer()

root.mainloop()