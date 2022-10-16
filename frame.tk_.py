from tkinter import *
from tkinter import messagebox as mb
window=Tk()
window.title("FRAME")
window.geometry("1200x600")
window.resizable(height="false",width="false")

def submit():
    data1 = txtn.get()
    data2 = txtm.get()
    data3 = txtadd.get()
    if data1=="duraipandiyan"   and data2=="duraidurai77dp@gmail.com" and data3=="thiruvannamalai":
       mb.showinfo("message","varified sucessfully")
    else:
      mb.showerror("error",'invalid name or mail id')



def clear():
     txtn.delete(0)
     txtm.delete(0)
     txtadd.delete(0)


def sub():
    data=texname.get()
    data2=texpass.get()
    data3=texcpass.get()
    if data == "duraipandiyan" and data2 == "duraipandiyandp1" and data3=="duraipandiyandp1":
        mb.showinfo("message","verified sucessfully")

    else:
        mb.showerror("error", 'invalid name or mail id')
def clr():
    texname.delete(0)
    texpass.delete(0)
    texcpass.delete(0)

frame1=Frame(window,highlightbackground="black",highlightthickness=4,height=200)
frame1.grid(row=0,column=0)
lb_n=Label(frame1,text="Name",font=("times",15,"bold"),pady=10,padx=10,fg="black")
lb_n.grid(row=1,column=0)

lb_n=Label(frame1,text="REGISTATION",font=("times",20,"italic"),pady=10,padx=10,fg="green")
lb_n.grid(row=0,column=1)


txtn=Entry(frame1,width=30,font=("times",15,"bold"))
txtn.grid(row=1,column=1)


lb_mail=Label(frame1,text="Mail",font=("times",15,"bold"),pady=10,padx=10,fg="black")
lb_mail.grid(row=2,column=0)

txtm=Entry(frame1,width=30,font=("times",15,"bold"))
txtm.grid(row=2,column=1)

lb_add=Label(frame1,text="Address",font=("times",15,"bold"),pady=10,padx=10,fg="black")
lb_add.grid(row=3,column=0)

txtadd=Entry(frame1,width=30,font=("times",15,"bold"))
txtadd.grid(row=3,column=1)

btnsub=Button(frame1,text="Submit",font=("times",15,"bold"),padx=10,pady=10,fg="white",bg="green",command=submit)
btnsub.grid(row=4,column=1,sticky=W,padx=13)

btnclr=Button(frame1,text="clear",font=("times",15,"bold"),padx=10,pady=10,fg="white",bg="red",command=clear)
btnclr.grid(row=4,column=1,padx=8)

#frame 2

frame2=Frame(window,highlightbackground="gray",highlightthickness=5,padx=30)
frame2.grid(row=0,column=1,padx=30)

lb_title=Label(frame2,text="LOGIN PROCESS",font=("times",20,"italic"),pady=10,padx=10,fg="green")
lb_title.grid(columnspan=2)

lb_name1=Label(frame2,text="Name",font=("times",15,"bold"),pady=10,padx=10,fg="black")
lb_name1.grid(row=1,column=1)


texname=Entry(frame2,width=30,font=("times",15,"bold"))
texname.grid(row=2,column=1)

lb_pass=Label(frame2,text="Password",font=("times",15,"bold"),pady=10,padx=10,fg="black")
lb_pass.grid(row=3,column=1)


texpass=Entry(frame2,width=30,font=("times",15,"bold"),show="*")
texpass.grid(row=4,column=1)



lb_cpass=Label(frame2,text="ConformPassword",font=("times",15,"bold"),pady=10,padx=10,fg="black")
lb_cpass.grid(row=5,column=1)


texcpass=Entry(frame2,width=30,font=("times",15,"bold"),show="*")
texcpass.grid(row=6,column=1)


btnsub1=Button(frame2,text="Submit",font=("times",15,"bold"),padx=10,pady=10,fg="white",bg="green",command=sub)
btnsub1.grid(row=7,column=1,sticky=W,padx=80)

btnclr1=Button(frame2,text="clear",font=("times",15,"bold"),padx=10,pady=10,fg="white",bg="red",command=clr)
btnclr1.grid(row=7,column=1,sticky=E,padx=40)


window.mainloop()