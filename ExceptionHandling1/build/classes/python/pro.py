from tkinter import *
from PIL import ImageTk
#FINCTIONALITY PART
def on_enter(event):
    if userentry.get()=='Username':
        userentry.delete(0,END)
    

#GUI PART
login_window=Tk()
login_window.resizable(0,0)
login_window.title('Login Page')    
bgImage=ImageTk.PhotoImage(file='airplane.jpg')
bgLabel=Label(login_window,image=bgImage)
bgLabel.pack()

#bgLabel.grid(row=0,column=0)
heading=Label(login_window,text='WELCOME TO ACET AIRLINES!',font=('Horizon',30,'bold'),fg='midnight blue')
heading.place(x=425,y=50)
heading=Label(login_window,text='  USER LOGIN   ',font=('Microsoft Yahei UI Light',23,'bold'),bg='white',fg='midnight blue')
heading.place(x=625,y=175)

userentry=Entry(login_window,width=30,font=('Microsoft Yahei UI Light',11))
userentry.place(x=625,y=240)
userentry.insert(0,'Username')
userentry.bind('<FocusIn>',on_enter)
Frame(login_window,width=245,height=2).place(x=625,y=270)
login_window.mainloop()

