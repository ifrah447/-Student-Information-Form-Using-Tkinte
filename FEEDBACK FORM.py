import tkinter
from tkinter import *
def save():
    text=E1.get()+"\n"+E2.get()+E3.get()+"\n"+E4.get()+"\n"+E5.get()+"\n"+E6.get()+"\n"+E7.get()+"\n"+E8.get()+"\n"+E9.get()
    with open("text.txt",'w') as f:
        f.writelines(text)
gui=tkinter.Tk()
gui.title('Student information')
gui.geometry('800x690')
gui.configure(bg="black")
title=Label(gui,text='student information',font=('Ariel 30 bold italic'),fg='white',bg='black').grid(row=0,column=2)

l1=Label(gui,text='Student Name: ',font=('Ariel 12 bold italic')).grid(row=1,column=1,padx=20,sticky='w')
E1=Entry(gui,bd=5,relief=GROOVE,width=60)
E1.grid(row=1,column=2,pady=10,padx=20,sticky='e')

l2=Label(gui,text='Father Name: ',font=('Ariel 12 bold italic')).grid(row=2,column=1,padx=20,sticky='w')
E2=Entry(gui,bd=5,relief=GROOVE,width=60)
E2.grid(row=2,column=2,pady=10,padx=20,sticky='e')

l3=Label(gui,text='E-mail: ',font=('Ariel 12 bold italic')).grid(row=3,column=1,padx=20,sticky='w')
E3=Entry(gui,bd=5,relief=GROOVE,width=60)
E3.grid(row=3,column=2,pady=10,padx=20,sticky='e')

l4=Label(gui,text='Section: ',font=('Ariel 12 bold italic')).grid(row=4,column=1,padx=20,sticky='w')
E4=Entry(gui,bd=5,relief=GROOVE,width=60)
E4.grid(row=4,column=2,pady=10,padx=20,sticky='e')

l5=Label(gui,text='department Name: ',font=('Ariel 12 bold italic')).grid(row=5,column=1,padx=20,sticky='w')
E5=Entry(gui,bd=5,relief=GROOVE,width=60)
E5.grid(row=5,column=2,pady=10,padx=20,sticky='e')

l6=Label(gui,text='seat no.: ',font=('Ariel 12 bold italic')).grid(row=6,column=1,padx=20,sticky='w')
E6=Entry(gui,bd=5,relief=GROOVE,width=60)
E6.grid(row=6,column=2,pady=10,padx=20,sticky='e')
l7=Label(gui,text='enrollement: ',font=('Ariel 12 bold italic')).grid(row=7,column=1,padx=20,sticky='w')
E7=Entry(gui,bd=5,relief=GROOVE,width=60)
E7.grid(row=7,column=2,pady=10,padx=20,sticky='e')
l8=Label(gui,text='Academic year: ',font=('Ariel 12 bold italic')).grid(row=8,column=1,padx=20,sticky='w')
E8=Entry(gui,bd=5,relief=GROOVE,width=60)
E8.grid(row=8,column=2,pady=10,padx=20,sticky='e')
l9=Label(gui,text='CGPA: ',font=('Ariel 12 bold italic')).grid(row=9,column=1,padx=20,sticky='w')
E9=Entry(gui,bd=5,relief=GROOVE,width=60)
E9.grid(row=9,column=2,pady=10,padx=20,sticky='e')
#save information button
button_ok=Button(gui,text='okay',font=('Ariel 9 bold italic'),borderwidth=2,highlightthickness=3,highlightbackground='green',relief=GROOVE,command=save)
button_ok.grid(row=10,column=2)
#quit information button
button_quit=Button(gui,text='quit',font=('Ariel 9 bold italic'),borderwidth=2,highlightthickness=3,highlightbackground='green',relief=GROOVE,command=gui.destroy)
button_quit.grid(row=11,column=2)
gui.mainloop()
