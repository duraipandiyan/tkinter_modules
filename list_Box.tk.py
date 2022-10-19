from tkinter import *
from tkinter import messagebox as mb
window=Tk()


def submit():
   data=txt.get()
   lisbox.insert(END,data)
   mb.showinfo("message","submited")

def select():
    data=lisbox.get(ANCHOR)
    mb.showinfo("message",data)

def update():
      pass

def lisbind(event):
    #id=lisbox.curselection()
    #mb.showinfo("message",id)
    data=lisbox.get(ANCHOR)
    #mb.showinfo("messsage",data)
    #tex box place or set
    set.set(data)

set=StringVar()
window.geometry("700x800")
window.title("listbox")
txt=Entry(window,width=30,textvariable=set)
txt.pack(pady=10)
lisbox=Listbox(window,width=30,height=20)
lisbox.pack(pady=10)

lisbox.insert(END,"java")
lisbox.insert(END,"python")
lis=["c","c++","php","ruby","angular","recact",'htm',"css","javascript"]
for i in lis:
    lisbox.insert(END,i)
for j  in range(1,11):
     print(lisbox.insert(END,"durai is python programmer"))


lbsub=Button(window,text="submit",font=("times",15,"bold"),width=10,padx=5,pady=5,fg="white",bg="green",command=submit)
lbsub.pack(pady=5)

lbsel=Button(window,text="Select",font=("times",15,"bold"),width=10,padx=5,pady=5,fg="white",bg="black",command=select)
lbsel.pack(pady=5)


lbup=Button(window,text="update",font=("times",15,"bold"),width=10,padx=5,pady=5,fg="white",bg="orange",command=update)
lbup.pack(pady=5)

#bind function
lisbox.bind("<<ListboxSelect>>",lisbind)
lisbox.pack()

window.mainloop()
