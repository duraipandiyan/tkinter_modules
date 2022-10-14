from tkinter import *
window=Tk()
window.title("FRAME")
window.geometry("900x400")
window.resizable(height="false",width="false")
frame1=Label(window,text="REGESTATION",font=("times",20,"bold"),width=10,pady=30,padx=30,fg="black",bg='white')
frame1.grid(columnspan=2)


window.mainloop()
