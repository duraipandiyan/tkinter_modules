from tkinter import *

import tkinter.messagebox  as mb

window=Tk()

def name():
    data=ent.get()
    data1=ent1.get()
    if data=="duraipandiyan" and data1=="duraipandiyandp1@":
        #lab2=Label(window,text="verifid",font=("times",10,'bold'),fg="blue")
        #lab2.place(x=160, y=280)
        mb.showinfo("massage","varified")

    else:
        #lab2 = Label(window, text="invalid username or password", font=("times",10,"bold"), fg="blue")
        #lab2.place(x=160, y=280)
        mb.showinfo("massage", "invalid user name or password")





window.geometry("500x500")
window.title("Login")
window.config(bg="pink")
window.resizable(height="false",width="false")
font=("times",20,"bold")
lab=Label(window,text="Gmail Login",padx=30,pady=10,relief="raised",font=font,bg="lightgreen")
lab.grid(row=0,column=1)

lab1=Label(window,text="Username",padx=20,pady=5,relief="raised",bg="blue",font=("times",15,"bold"),width=10)
lab1.grid(row=1,column=0,pady=5)
a=StringVar

ent=Entry(window,relief="raised",bg="white",fg="black",font=("time",10,"bold"),width=27)
ent.grid(row=1,column=1)


lab2=Label(window,text="Password",padx=20,pady=5,relief="raised",bg="blue",font=("times",15,"bold"),width=10)
lab2.grid(row=2,column=0,pady=5)

b=StringVar
ent1=Entry(window,relief="raised",bg="white",fg="black",font=("time",10,"bold"),width=27,show="*",)
ent1.grid(row=2,column=1)

btn=Button(window,text="submit",relief="raised",bg="red",fg="green",font=("time",15,"bold",),width=18,command=name)
btn.grid(row=3,column=1)

window.mainloop()

