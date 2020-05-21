from tkinter import *

def save():
    id2=id1.get()
    pass2=pass1.get()
    with open("id.txt","w") as i:
        i.write(id2)
        i.close
    with open("pass.txt","w") as p:
        p.write(pass2)
        p.close
    print("Save Successful")
r = Tk() 
r.title('Gmail Setup') 

Label(r, text='Email_id:').grid(row=1,pady=20)
Label(r, text='Password:').grid(row=2,pady=20)

id1 = Entry(r)
pass1 = Entry(r)
id1.grid(row=1, column=1,ipady=5)
pass1.grid(row=2, column=1,ipady=5)

v = IntVar()
v.set(1)
buttonP = Button(r, text='Save', width=25, command=save) 
buttonP.grid(row=8,ipady=20)
buttonS = Button(r, text='Exit', width=25, command=r.destroy) 
buttonS.grid(row=8,column=1,ipady=20)
r.mainloop()