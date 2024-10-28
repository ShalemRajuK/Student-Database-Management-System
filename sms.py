from tkinter import *
import time
import ttkthemes
from tkinter import ttk
import pymysql
from tkinter import messagebox,filedialog
import pandas

#functionality part

# Function to confirm exit
def iexit():
    result=messagebox.askyesno("confirm",'Do you want to exit')
    if result:
        root.destroy()
    else:
        pass

#Function to export student data to a CSV file
def export_data():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=studentTable.get_children()    
    newlist=[]
    for index in indexing:
        content = studentTable.item(index)
        datalist= content["values"]
        newlist.append(datalist)

 # Create DataFrame and save to CSV   
    table=pandas.DataFrame(newlist,columns=['ID','Name','Mobile','email','Address','Gender','DOB','addeddate','addedtime'])
    #table.to_csv(url,index=False)
    #messagebox.showinfo("success","data saved succefully")
    print(table)
 

# Function to update a student's details
def update_student():

    def update_data():
         #SQL query to update a student's data
        query="update student set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,joindate=%s,jointime=%s where id=%s"
        mycursor.execute(query,(nameEntry.get(),phoneEntry.get(),emailEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get(),date,currenttime,idEntry.get()))
        con.commit()
        messagebox.showinfo("SUCCESS",f'{idEntry.get()} ID has been successfully modified',parent=update_window)
        update_window.destroy()
        show_student()

    # Window to capture updated student details
    update_window=Toplevel()
    update_window.title("Update Student")
    update_window.grab_set()
    update_window.resizable(False,False)

     # Add labels and entry fields to capture updated data
    idLabel= Label(update_window,text='ID',font=("times new roman",20,'bold'))
    idLabel.grid(row=0,column=0,padx=10,pady=15)
    idEntry = Entry(update_window,font=('times new roman',18))
    idEntry.grid(row=0,column=1,padx=20)

    nameLabel= Label(update_window,text='Name',font=("times new roman",20,'bold'))
    nameLabel.grid(row=1,column=0,padx=10,pady=15)
    nameEntry = Entry(update_window,font=('times new roman',18))
    nameEntry.grid(row=1,column=1,padx=20)   

    phoneLabel= Label(update_window,text='Phone',font=("times new roman",20,'bold'))
    phoneLabel.grid(row=2,column=0,padx=10,pady=15)
    phoneEntry = Entry(update_window,font=('times new roman',18))
    phoneEntry.grid(row=2,column=1,padx=20) 

    emailLabel= Label(update_window,text='Email',font=("times new roman",20,'bold'))
    emailLabel.grid(row=3,column=0,padx=10,pady=15)
    emailEntry = Entry(update_window,font=('times new roman',18))
    emailEntry.grid(row=3,column=1,padx=20)

    addressLabel= Label(update_window,text='Address',font=("times new roman",20,'bold'))
    addressLabel.grid(row=4,column=0,padx=10,pady=15)
    addressEntry = Entry(update_window,font=('times new roman',18))
    addressEntry.grid(row=4,column=1,padx=20)

    genderLabel= Label(update_window,text='Gender',font=("times new roman",20,'bold'))
    genderLabel.grid(row=5,column=0,padx=10,pady=15)
    genderEntry = Entry(update_window,font=('times new roman',18))
    genderEntry.grid(row=5,column=1,padx=20)

    doblabel= Label(update_window,text='DOB',font=("times new roman",20,'bold'))
    doblabel.grid(row=6,column=0,padx=10,pady=15)
    dobEntry = Entry(update_window,font=('times new roman',18))
    dobEntry.grid(row=6,column=1,padx=20)

    # Button to confirm the update
    update_student_button=ttk.Button(update_window,text="UPDATE",command=update_data)
    update_student_button.grid(row=7,column=1,pady=10)

    # Pre-fill fields with selected student's data
    indexing=studentTable.focus()
    print(indexing)
    content=studentTable.item(indexing)
    listdata=content['values']
    idEntry.insert(0,listdata[0])
    nameEntry.insert(0,listdata[1])
    phoneEntry.insert(0,listdata[2])
    emailEntry.insert(0,listdata[3])
    addressEntry.insert(0,listdata[4])
    genderEntry.insert(0,listdata[5])
    dobEntry.insert(0,listdata[6])

# Function to display students in the table
def show_student():
    query="select * from student"
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    # Clear current table and repopulate with data from the database
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)

# Function to delete a selected student
def delete_student():
    indexing= studentTable.focus()
    print(indexing)
    content=studentTable.item(indexing)
    content_id=content["values"][0]
    query = "delete from student where id =%s"
    mycursor.execute(query,content_id)
    con.commit
    messagebox.showinfo("Deleted",f"{content_id}deleted sucessfully")
    query="select * from student"
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert("",END,values=data)

#Function for search student
def search_student():
    def search_data():
        query = "select * from student where id=%s or name=%s or mobile=%s or email=%s or address=%s or gender=%s or dob=%s"
        mycursor.execute(query,(idEntry.get(),nameEntry.get(),emailEntry.get(),phoneEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get()))
        studentTable.delete(*studentTable.get_children())
        fetched_data= mycursor.fetchall()
        for data in fetched_data:
            studentTable.insert('',END,values=data)


    search_window=Toplevel()
    search_window.title("Search Student")
    search_window.grab_set()
    search_window.resizable(False,False)

    idLabel= Label(search_window,text='ID',font=("times new roman",20,'bold'))
    idLabel.grid(row=0,column=0,padx=10,pady=15)
    idEntry = Entry(search_window,font=('times new roman',18))
    idEntry.grid(row=0,column=1,padx=20)

    nameLabel= Label(search_window,text='Name',font=("times new roman",20,'bold'))
    nameLabel.grid(row=1,column=0,padx=10,pady=15)
    nameEntry = Entry(search_window,font=('times new roman',18))
    nameEntry.grid(row=1,column=1,padx=20)   

    phoneLabel= Label(search_window,text='Phone',font=("times new roman",20,'bold'))
    phoneLabel.grid(row=2,column=0,padx=10,pady=15)
    phoneEntry = Entry(search_window,font=('times new roman',18))
    phoneEntry.grid(row=2,column=1,padx=20) 

    emailLabel= Label(search_window,text='Email',font=("times new roman",20,'bold'))
    emailLabel.grid(row=3,column=0,padx=10,pady=15)
    emailEntry = Entry(search_window,font=('times new roman',18))
    emailEntry.grid(row=3,column=1,padx=20)

    addressLabel= Label(search_window,text='Address',font=("times new roman",20,'bold'))
    addressLabel.grid(row=4,column=0,padx=10,pady=15)
    addressEntry = Entry(search_window,font=('times new roman',18))
    addressEntry.grid(row=4,column=1,padx=20)

    genderLabel= Label(search_window,text='Gender',font=("times new roman",20,'bold'))
    genderLabel.grid(row=5,column=0,padx=10,pady=15)
    genderEntry = Entry(search_window,font=('times new roman',18))
    genderEntry.grid(row=5,column=1,padx=20)

    doblabel= Label(search_window,text='DOB',font=("times new roman",20,'bold'))
    doblabel.grid(row=6,column=0,padx=10,pady=15)
    dobEntry = Entry(search_window,font=('times new roman',18))
    dobEntry.grid(row=6,column=1,padx=20)

    search_student_button=ttk.Button(search_window,text="Search Student",command=search_data)
    search_student_button.grid(row=7,column=1,pady=10)

#function to add student
def add_student():
    def add_data():
        if idEntry.get=='' or nameEntry.get=='' or phoneEntry.get=='' or emailEntry.get=='' or addressEntry.get=='' or genderEntry.get=='' or dobEntry.get=='':
            messagebox.showerror("error",'All fields are required',parent=add_window)
        else:
            
            try:
                query="insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                mycursor.execute(query,(idEntry.get(),nameEntry.get(),phoneEntry.get(),emailEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get(),date,currenttime))
                con.commit()
                result=messagebox.askyesno("CONFIRM",'Data added Successfully. Do you want to clean the from ?', parent=add_window)
                if result:
                    idEntry.delete(0,END)
                    nameEntry.delete(0,END)
                    phoneEntry.delete(0,END)
                    emailEntry.delete(0,END)
                    addressEntry.delete(0,END)
                    genderEntry.delete(0,END)
                    dobEntry.delete(0,END)
                else:
                    pass
            except:
                messagebox.showerror("Error","ID already Exists",parent=add_window)  
                return


            query = "select * from student"
            mycursor.execute(query)
            fetched_data = mycursor.fetchall() #to fetch data from database
            studentTable.delete(*studentTable.get_children())
            for data in fetched_data:
                datalist =list(data) # data is in the form of touples initially and we are converting it to list
                studentTable.insert('',END,values=datalist)


    add_window=Toplevel()
    add_window.grab_set()
    add_window.resizable(False,False)

    idLabel= Label(add_window,text='ID',font=("times new roman",20,'bold'))
    idLabel.grid(row=0,column=0,padx=10,pady=15)
    idEntry = Entry(add_window,font=('times new roman',18))
    idEntry.grid(row=0,column=1,padx=20)

    nameLabel= Label(add_window,text='Name',font=("times new roman",20,'bold'))
    nameLabel.grid(row=1,column=0,padx=10,pady=15)
    nameEntry = Entry(add_window,font=('times new roman',18))
    nameEntry.grid(row=1,column=1,padx=20)   

    phoneLabel= Label(add_window,text='Phone No:',font=("times new roman",20,'bold'))
    phoneLabel.grid(row=2,column=0,padx=10,pady=15)
    phoneEntry = Entry(add_window,font=('times new roman',18))
    phoneEntry.grid(row=2,column=1,padx=20) 

    emailLabel= Label(add_window,text='Email',font=("times new roman",20,'bold'))
    emailLabel.grid(row=3,column=0,padx=10,pady=15)
    emailEntry = Entry(add_window,font=('times new roman',18))
    emailEntry.grid(row=3,column=1,padx=20)

    addressLabel= Label(add_window,text='Address',font=("times new roman",20,'bold'))
    addressLabel.grid(row=4,column=0,padx=10,pady=15)
    addressEntry = Entry(add_window,font=('times new roman',18))
    addressEntry.grid(row=4,column=1,padx=20)

    genderLabel= Label(add_window,text='Gender',font=("times new roman",20,'bold'))
    genderLabel.grid(row=5,column=0,padx=10,pady=15)
    genderEntry = Entry(add_window,font=('times new roman',18))
    genderEntry.grid(row=5,column=1,padx=20)

    doblabel= Label(add_window,text='D.O.B',font=("times new roman",20,'bold'))
    doblabel.grid(row=6,column=0,padx=10,pady=15)
    dobEntry = Entry(add_window,font=('times new roman',18))
    dobEntry.grid(row=6,column=1,padx=20)

    add_student_button=ttk.Button(add_window,text="Add Student",command=add_data)
    add_student_button.grid(row=7,column=1,pady=10)

#function to connect to database
def connect_database():
    def connect():
        global mycursor,con
        try:
            con = pymysql.connect(host=hostEntry.get(),user=userNameEntry.get(),password=passwordEntry.get())
            mycursor=con.cursor()
            
        except:
            messagebox.showerror("Error","Invalid Details",parent=connectWindow)
            return
        try:    
            query = "create database studentmanagementsystem"
            mycursor.execute(query)
            query = "use studentmanagementsystem"
            mycursor.execute(query)
            query= "create table student(id int not null primary key, name varchar(30), mobile varchar(30), email varchar(30), address varchar(100), gender varchar(20), dob varchar(20), joindate varchar(30), jointime varchar(30))"
            mycursor.execute(query)
        except:
            query = "use studentmanagementsystem"
            mycursor.execute(query)
        messagebox.showinfo('sucess',"connected Successfully",parent=connectWindow)
        connectWindow.destroy()
        addstudentButton.config(state=NORMAL)
        searchstudentButton.config(state=NORMAL)
        deletestudentButton.config(state=NORMAL)
        updatestudentButton.config(state=NORMAL)
        showstudentButton.config(state=NORMAL)
        exportstudentButton.config(state=NORMAL)
       




    connectWindow=Toplevel() 
    #connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title("Database Connection")
    connectWindow.resizable(False,False)
    connectWindow.configure(bg="White")

    hostnamelabel=Label(connectWindow,text="Host Name",font=('arial',20,"bold"),bg="white",fg="black")
    hostnamelabel.grid(row=0,column=0,pady=10)

    hostEntry=Entry(connectWindow,font=('arial',18),bg="white",fg="black")
    hostEntry.grid(row=0,column=1,padx=20)

    userNameLabel=Label(connectWindow,text="User Name",font=('arial',20,"bold"),bg="white",fg="black")
    userNameLabel.grid(row=1,column=0,pady=10)

    userNameEntry=Entry(connectWindow,font=('arial',18),bg="white",fg="black")
    userNameEntry.grid(row=1,column=1,padx=20)

    passwordLabel=Label(connectWindow,text="Password",font=('arial',20,"bold"),bg="white",fg="black")
    passwordLabel.grid(row=2,column=0,pady=10)

    passwordEntry=Entry(connectWindow,font=('arial',18),bg="white",fg="black")
    passwordEntry.grid(row=2,column=1,padx=20)

    connectButton = ttk.Button(connectWindow,text="Connect",command=connect)
    connectButton.grid(row=3,column=1)
    



def clock(): 
    global date,currenttime
    date = time.strftime("%d/%m/%Y")
    currenttime =time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f"date : {date}\n\nTime:{currenttime}")
    datetimeLabel.after(1000,clock)


#gui part
root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')

root.geometry('1280x700+0+0')
root.title("Student Management System")
root.resizable(False,False)
root.configure(bg="white")

datetimeLabel = Label(root,font=("times new roman",18,'bold'))
datetimeLabel.place(x=5,y=5)
clock()
sliderLabel = Label(root,text="Student Management System",font=("arial",18,"italic bold"));
sliderLabel.place(x=520,y=0)

connectButton = ttk.Button(root,text="connect to database",command=connect_database)
connectButton.place(x=1120,y=0)

leftFrame = Frame(root, bg="white")
leftFrame.place(x=10,y=90,width=300,height=600)

addstudentButton =ttk.Button(leftFrame,text="Add Student",width=25,state=DISABLED,command=add_student)
addstudentButton.grid(row=1,column=0,pady=20)

searchstudentButton =ttk.Button(leftFrame,text="search Student",width=25,state=DISABLED,command=search_student)
searchstudentButton.grid(row=2,column=0,pady=20)

deletestudentButton =ttk.Button(leftFrame,text="delete Student",width=25,state=DISABLED,command=delete_student)
deletestudentButton.grid(row=3,column=0,pady=20)

updatestudentButton =ttk.Button(leftFrame,text="update Student",width=25,state=DISABLED,command=update_student)
updatestudentButton.grid(row=4,column=0,pady=20)

showstudentButton =ttk.Button(leftFrame,text="show Student",width=25,state=DISABLED,command=show_student)
showstudentButton.grid(row=5,column=0,pady=20)

exportstudentButton =ttk.Button(leftFrame,text="Export Data",width=25,state=DISABLED,command=export_data)
exportstudentButton.grid(row=6,column=0,pady=20)

exitButton = ttk.Button(leftFrame,text="Exit",width=25,command=iexit)
exitButton.grid(row=7,column=0,pady=20)

rightFrame = Frame(root, bg="white")
rightFrame.place(x=300,y=60,width=920,height=600)

studentTable=ttk.Treeview(rightFrame,columns=('ID','Name','Mobile No','Email','Address','Gender','D.O.B','Added date','Added time'))
studentTable.pack(fill=BOTH,expand=1)

studentTable.heading('ID',text='ID')
studentTable.heading('Name',text='Name')
studentTable.heading('Mobile No',text='Mobile No')
studentTable.heading('Email',text='Email')
studentTable.heading('Address',text='Address')
studentTable.heading('Gender',text='Gender')
studentTable.heading('D.O.B',text='D.O.B')
studentTable.heading('Added date',text='Added date')
studentTable.heading('Added time',text='Added time')

style=ttk.Style()
style.configure('Treeview',rowheight = 40,foreground='black',background='white')

studentTable.config(show='headings')

root.mainloop()
