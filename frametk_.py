from tkinter import *
window=Tk()
window.title("FRAME")
window.geometry("900x400")
window.resizable(height="false",width="false")
frame1=Label(window,text="REGESTATION",font=("times",20,"bold"),width=10,pady=30,padx=30,fg="black",bg='white')
frame1.grid(row=0,column=0)
lb_n=Label(frame1,text="Name",font=("times",15,"bold"),pady=20,padx=30,fg="black",bg='white')

window.mainloop()