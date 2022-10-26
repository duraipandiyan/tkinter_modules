from tkinter import *
window=Tk()
window.title("MENUBAR")
window.geometry("500x500")
menubor=Menu(window,)

def new():
    filenwe=Toplevel(window)
    filenwe.title("NEW")
    filenwe.geometry("250x250")
    lblnew=Label(filenwe,text="NEW WINDOW",fg="black",font=("times",15,"bold"))
    lblnew.pack()
    btnnew=Button(filenwe,text="close button",bg="blue",fg="white",font=("times",15,"bold"),command=filenwe.destroy)

    btnnew.pack(pady=30,fill=X)


def open():
    filenwe = Toplevel(window)
    filenwe.title("OPEN")
    filenwe.geometry("250x250")
    lblnew = Label(filenwe, text="OPEN WINDOW", fg="black", font=("times", 15, "bold"))
    lblnew.pack()
    btnnew = Button(filenwe, text="close button", bg="blue", fg="white", font=("times", 15, "bold"),command=filenwe.destroy)

    btnnew.pack(pady=30, fill=X)


filemenu=Menu(menubor,tearoff=0)
filemenu.add_command(label="New",command=new)
filemenu.add_command(label="open",command=open)
filemenu.add_separator()
filemenu.add_command(label="save")
filemenu.add_command(label="save as")
filemenu.add_separator()
filemenu.add_command(label="Exit",command=window.destroy)
menubor.add_cascade(label="File",menu=filemenu)


editmenu=Menu(menubor,tearoff=0)
editmenu.add_command(label="edit")
editmenu.add_command(label="cut")
editmenu.add_separator()
editmenu.add_command(label="copy")
editmenu.add_command(label="past")
editmenu.add_separator()
editmenu.add_command(label="rename")
editmenu.add_command(label="Exit")
menubor.add_cascade(label="Edit",menu=editmenu)






window.config(menu=menubor)



window.mainloop()