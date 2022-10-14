from tkinter import *
from  tkinter import ttk
import tkinter.messagebox as mb
window=Tk()

def combo(event):
    data=cobox.get()
    mb.showinfo("message",data)


window.title("Combobox")
window.geometry("500x500")
window.resizable(height="false",width="false")
lacb=Label(window,text="COMBOBOX",font=("time",20,'bold'),fg='white',bg='black')
lacb.pack(fill=X)
cobox=ttk.Combobox(window,width=30,state="readonly")
cobox["values"]=("python","c","c++","java","php","c#","asp.net")
cobox.bind("<<ComboboxSelected>>",combo)
cobox.pack(pady=5)

window.mainloop()