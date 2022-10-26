from tkinter import *
from tkinter import messagebox

def butten_clecked():
    messagebox.showinfo("message","submited")
    btn.pack()
def clecked():
    var=ent.get()
    messagebox.showinfo("message",var)
def clear():
    ent.delete(0,END)
    clr=Label(window)

def get_fun():
    if gender.get()==1:
         data=ra1.cget("text")

         messagebox.showinfo("message",data)
    elif gender.get()==2:
        data1=ra2.cget("text")
        messagebox.showinfo("message",data1)
    elif gender.get()==3:
        data2=ra3.cget("text")
        messagebox.showinfo("message",data2)
window=Tk()

window.geometry("800x800")
window.resizable(height="false",width="false")
window.title("python")
window.config(bg="#3d434f540")
#label
lab=Label(window,text="Python Programming",padx=20,pady=10,relief="raised",font="times",bg="yellow",fg="green",width=25)
lab.pack()
#button_submit
btn=Button(window,text="submit",padx=10,pady=10,relief="raised",font="times",bg="red",fg="blue",width=15,command=butten_clecked)
btn.pack()
#entry
ent=Entry(window,width=30,font="times",bg="gray",fg="blue",selectbackground="white",selectforeground="green")
ent.pack()
#button_submit1
btn1=Button(window,text="submit",padx=10,pady=10,relief="raised",font="times",bg="green",fg="white",width=15,command=clecked)
btn1.pack(side="left")

#clear_button1t
clr=Button(window,text="clear",padx=10,pady=10,relief="raised",font="italic",bg="orange",fg="red",width=15,command=clear)
clr.pack(side="right")
  #chechbutton
cours1=Checkbutton(window,text="python",font=("times",8,"italic"),bg="white",fg="black",width=10,relief="raised")
cours2=Checkbutton(window,text="c++",font=("times",8,"italic"),bg="white",fg="black",width=10,relief="raised")
cours3=Checkbutton(window,text="java",font=("times",8,"italic"),bg="white",fg="black",width=10,relief="raised")
cours4=Checkbutton(window,text="HTML",font=("times",8,"italic"),bg="white",fg="black",width=10,relief="raised")
cours1.pack()
cours2.pack()
cours3.pack()
cours4.pack()



#lable for radiobutton
lara=Label(window,text="Radiobutton",relief="raised",padx=30,pady=10,width=20,font=("times",20,"italic"))
lara.pack(fill=X)
gender=IntVar()
ra1=Radiobutton(window,text="male",variable=gender,value=1,width=8,padx=20,state="active")
ra1.pack(pady=5)
ra2=Radiobutton(window,text="female",variable=gender,value=2,width=8,state="active")
ra2.pack(pady=5)
ra3=Radiobutton(window,text="others",variable=gender,value=3,width=8,state="active")
ra3.pack(pady=5)


rabut=Button(window,text="Submit",font=("times",10,"bold"),command=get_fun)
rabut.pack(pady=10)
window.mainloop()


