from  tkinter import *
window=Tk()
window.geometry("500x500")
window.title("scrollbar")
title=Label(window,text="SCROLLBAR",font=("times",20,"italic"),fg="white",bg="black",pady=6)
title.pack(fill=X)

frame1=Frame(window)
frame1.pack(pady=40)

yscroll=Scrollbar(frame1,orient=VERTICAL)
xscroll=Scrollbar(frame1,orient=HORIZONTAL)
yscroll.pack(side=RIGHT,fill=Y)
xscroll.pack(side=BOTTOM,fill=X)

txtbox=Text(frame1,width=30,height=30,yscrollcommand=yscroll.set,xscrollcommand=xscroll.set,wrap="none")
txtbox.pack()
yscroll.config(command=txtbox.yview)
xscroll.config(command=txtbox.xview)

for i in range(50):
    print(txtbox.insert(END,"\npython is a high level programmig language"))



window.mainloop()