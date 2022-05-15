from tkinter import *
from tkinter.ttk import *
import time



from time import gmtime, strftime
root = Tk()
root.title(" RAHUL'S CLOCK")
def time():
    string = str('%H:%H:%S %p')
    label.config(text=string)
    label.after(1000, time())

label = Label(root, font=("ds-digital", 80), background= "black",foreground= "cyan")
label.pack(anchor='center')
time()

mainloop()