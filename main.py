from tkinter import *
import time as t
win =Tk()
win.title("Time")
win.minsize(500,50)


def tim():
    ct=t.strftime("%H:%M:%S")
    LA.config(text=ct)
    LA.after(1000,tim)


LA=Label(text=win,font=('calibiri',100,'bold'),background='grey',foreground='blue')
LA.pack()
tim()
win.mainloop()
