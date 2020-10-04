from tkinter import *

from tkinter import messagebox
top=Tk()
top.geometry("100x100")
def hellocallback():
    msg=messagebox.showinfo("Hello python","Hello world")

B=Button(top,Text="Click ME",command=hellocallback)
B.place(x=0,y=50)
top.mainloop()