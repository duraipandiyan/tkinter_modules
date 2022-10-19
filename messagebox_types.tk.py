#show info
#show error
#show warinig
#Ask question
#Ask okcancel
#Ask yesno
#Ask yesnocancle

from tkinter import *
from tkinter import messagebox as mb
def info():
    mb.showinfo("message","show info")

def error():
    mb.showerror("message","show error")


def warning():
    mb.showwarning("message","showwarnig")

def ask():
    mb.askquestion("message","askquestion")

def askok():
    mb.askokcancel("message","askokcancel")

def askyesno():
    mb.askokcancel("message", "askyesno")

def askyesnocancel():
    mb.askokcancel("message", "askyesnocancel")

window=Tk()
window.geometry("500x500")
window.title("messagebox types")
#show info
showinfo=Button(window,text="show info",font=("times",15,"bold"),fg="white",bg="green",width=15,command=info)
showinfo.pack(pady=10)
# shoew Error
showError=Button(window,text="Error",font=("times",15,"bold"),fg="white",bg="pink",width=15,command=error)
showError.pack(pady=5)

#show warnig
showwarnig=Button(window,text="show warnig",font=("times",15,"bold"),fg="white",bg="blue",width=15,command=warning)
showinfo.pack(pady=10)

#ask question
askqu=Button(window,text="Ask quetion",font=("times",15,"bold"),fg="white",bg="yellow",width=15,command=ask)
askqu.pack(pady=10)

#ask okcancel
askok=Button(window,text="Ask okcancel",font=("times",15,"bold"),fg="white",bg="gray",width=15,command=askok)
askok.pack(pady=10)

#ask yesno
askyesno=Button(window,text="Ask yesno",font=("times",15,"bold"),fg="white",bg="lightgreen",width=15,command=askyesno)
askyesno.pack(pady=10)

#ask yesnocancel
#ask yesno
askyesnocl=Button(window,text="Ask yesnocancel",font=("times",15,"bold"),fg="white",bg="green",width=15,command=askyesnocancel)
askyesnocl.pack(pady=10)
window.mainloop()