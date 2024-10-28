from tkinter import *
from tkinter import messagebox

def login():
    if usernameEntry.get() =="" or passwordEntry.get() =="":
        messagebox.showerror("ERROR", "Fields cannot be empty")
    elif usernameEntry.get() == "username" and passwordEntry.get() =="password":
        messagebox.showinfo("SUCCESS","You have successfully logged in")
        window.destroy()
        import sms
        

    else:
        messagebox.showinfo("Error","please enter valid details")


window = Tk()


window.geometry('1280x700+0+0')
window.title("LOGIN PAGE")
#window.resizable(False,False)
window.configure(bg="white")


loginFrame=Frame(window)
loginFrame.place(x=500,y=200)

usernameLabel = Label(loginFrame,text="USERNAME",font=("times new roman",20,"bold"),fg="black",bg="white")
usernameLabel.grid(row=1,column=0,padx=0) 

passwordLabel = Label(loginFrame,text="PASSWORD",font=("times new roman",20,"bold"),fg="black",bg="white")
passwordLabel.grid(row=2,column=0,padx=0,pady=10)

usernameEntry=Entry(loginFrame,bd=1,fg="black",bg="white")
usernameEntry.grid(row=1,column=1,padx=0)

passwordEntry = Entry(loginFrame,bd=1,fg="black",bg="white")
passwordEntry.grid(row=2,column=1,padx=0,pady=10)

loginButton=Button(loginFrame,text="LOG IN",width=15,cursor="hand2",command=login)
loginButton.grid(row=3,column=1,pady=10)

window.mainloop()