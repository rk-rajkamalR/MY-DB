from tkinter import*
from tkinter import ttk
from tkinter import Button
from tkinter import messagebox
from tabulate import tabulate
import tkinter as tk
import mysql.connector

con=mysql.connector.connect(host="localhost",user="root",password="######",database="store")
root=Tk()

root.geometry('1920x1080')
root.title("tiME")
root.state('zoomed')
root.config(bg='black')

Frame1=Frame(root,bg="black")
Frame1.grid(columnspan=2)

#======================Label============================================================#
label=Label(Frame1,text="📝 Note's",font=("times",50,"bold","italic"),bg="black",fg="white")
label.grid(row=0,column=0)


Name=Label(Frame1,text="Name:",font=("times",25,"bold","italic"),bg="black",fg="white")
Name.grid(row=1,column=1,ipady=20)

Phone=Label(Frame1,text="Phone:",font=("times",25,"bold","italic"),bg="black",fg="white")
Phone.grid(row=2,column=1,ipady=20)

City=Label(Frame1,text="District:",font=("times",25,"bold","italic"),bg="black",fg="white")
City.grid(row=3,column=1,ipady=20)

State=Label(Frame1,text="State:",font=("times",25,"bold","italic"),bg="black",fg="white")
State.grid(row=4,column=1,ipady=20)

work=Label(Frame1,text="Work:",font=("times",25,"bold","italic"),bg="black",fg="white")
work.grid(row=5,column=1,ipady=20)

Date=Label(Frame1,text="Date:",font=("times",25,"bold","italic"),bg="black",fg="white")
Date.grid(row=6,column=1,ipady=20)

Month=Label(Frame1,text="Month:",font=("times",25,"bold","italic"),bg="black",fg="white")
Month.grid(row=7,column=1,ipady=20)

Year=Label(Frame1,text="Year:",font=("times",25,"bold","italic"),bg="black",fg="white")
Year.grid(row=8,column=1,ipady=20)
#==================================function==========================================================================================#
def insert():
    Name = Name_var.get()
    Phone = Phone_var.get()
    City = City_var.get()
    State =State_var.get()
    work= work_var.get()
    Date = Date_var.get()
    Month= Month_var.get()
    Year= Year_var.get()
    Name_var.set("")
    Phone_var.set("")
    City_var.set("")
    State_var.set("")
    work_var.set("")
    Date_var.set("")
    Month_var.set("")
    Year_var.set("")
    box=con.cursor()
    sql="insert into vivo(Name,Phone,City,State,work,Date,Month,Year) values(%s,%s,%s,%s,%s,%s,%s,%s)"
    box.execute(sql,(Name,Phone,City,State,work,Date,Month,Year))
    con.commit()
    messagebox.showinfo("infromation","Data insert is sueccessfuly!")
    
def update():
    Name = Name_var.get()
    Phone = Phone_var.get()
    City = City_var.get()
    State =State_var.get()
    work= work_var.get()
    Date = Date_var.get()
    Month= Month_var.get()
    Year= Year_var.get()
    Name_var.set("")
    Phone_var.set("")
    City_var.set("")
    State_var.set("")
    work_var.set("")
    Date_var.set("")
    Month_var.set("")
    Year_var.set("")
    box=con.cursor()
    sql="update vivo set Phone=%s,City=%s,State=%s,work=%s,Date=%s,Month=%s,Year=%s where Name=%s"
    box.execute(sql,(Phone,City,State,work,Date,Month,Year,Name))
    con.commit()
    messagebox.showinfo("infromation","Data update is sueccessfuly!")
    
def newtable():
    new2=Tk()
    new2.config(bg="Orange")
    new2.geometry('720x720')
    new2.state('zoomed')
    new2.title("Pixel Plus Analysis-RK")
    label=Label(new2,text="Comming Soon !.......",font=("times",100,"bold","italic"),bg="gray")
    label.pack(fill=X,pady=300)
    new2.mainloop()

def delete():
    Name= Name_var.get()
    Name_var.set("")
    box=con.cursor()
    sql="delete from vivo where Name=%s"
    box.execute(sql,(Name,))
    con.commit()
    messagebox.showinfo("🙃","Data delete successfully!")

def select():
    box=con.cursor()
    sql="select Name,Phone,City,State,work,Date,Month,Year from vivo"
    box.execute(sql)
    temp=box.fetchall()
    house=tabulate(temp,headers=['NAME','PHONE_NUMBER','CITY','STATE','WORK','DATE','MONTH','YEAR'])
    new_windows=Tk()
    label=Label(new_windows,text=house,font=("times",20,"bold","italic"),fg="white",bg="gray",)
    label.pack(fill=X)
    new_windows.geometry('720x720')
    new_windows.config(bg="blue")
    new_windows.title('tiME')
    new_windows.state('zoomed')
    new_windows.mainloop()
 
 
    

    

label=Label(Frame1,text="👆 click",font=("times",50,"bold","italic"),bg="black",fg="white")
label.grid(row=0,column=100)

Name_var=tk.StringVar()
Name_entry = tk.Entry(Frame1, textvariable=Name_var,cursor="arrow",font=("calibre", 15, "normal"),borderwidth=10,bg="gray",fg="white")
Name_entry.grid(row=1,column=2)

Phone_var=tk.StringVar()
Phone_entry = tk.Entry(Frame1, textvariable=Phone_var, cursor="arrow",font=("calibre", 15, "normal"),borderwidth=10,bg="gray",fg="white")
Phone_entry.grid(row=2,column=2)

City_var=tk.StringVar()
City_entry = tk.Entry(Frame1, textvariable=City_var, cursor="arrow",font=("calibre", 15, "normal"),borderwidth=10,bg="gray",fg="white")
City_entry.grid(row=3,column=2)

State_var=tk.StringVar()
State_entry = tk.Entry(Frame1, textvariable=State_var, cursor="arrow",font=("calibre", 15, "normal"),borderwidth=10,bg="gray",fg="white")
State_entry.grid(row=4,column=2)

work_var=tk.StringVar()
work_entry = tk.Entry(Frame1, textvariable=work_var, cursor="arrow",font=("calibre", 15, "normal"),borderwidth=10,bg="gray",fg="white")
work_entry.grid(row=5,column=2)

Date_var=tk.StringVar()
Date_entry = tk.Entry(Frame1, textvariable=Date_var, cursor="arrow",font=("calibre", 15, "normal"),borderwidth=10,bg="gray",fg="white")
Date_entry.grid(row=6,column=2)

Month_var=tk.StringVar()
Month_entry = tk.Entry(Frame1, textvariable=Month_var, cursor="arrow",font=("calibre", 15, "normal"),borderwidth=10,bg="gray",fg="white")
Month_entry.grid(row=7,column=2)

Year_var=tk.StringVar()
Year_entry = tk.Entry(Frame1, textvariable=Year_var, cursor="arrow",font=("calibre", 15, "normal"),borderwidth=10,bg="gray",fg="white")
Year_entry.grid(row=8,column=2)

#=====================================================cretae a button========================================================================================

insert=Button(Frame1,text="INSERT✍️ ",command=insert,borderwidth=10,activeforeground="black",activebackground="black",font=("times",30,"bold"),bg="Teal",fg="black")
insert.grid(row=2,column=100)

update=Button(Frame1,text="UPDATE🙃",command=update,borderwidth=10,activeforeground="black",activebackground="black",font=("times",30,"bold"),bg="magenta",fg="black")
update.grid(row=2,column=110)

#more=Button(Frame1,text="New💻Table",command=newtable,borderwidth=10,activeforeground="black",activebackground="black",font=("times",30,"bold"),bg="magenta",fg="black")
#more.grid(row=2,column=113,columnspan=20)

delete=Button(Frame1,text="DELETE✂️",command=delete,borderwidth=10,activeforeground="black",activebackground="black",font=("times",30,"bold"),bg="green",fg="black")
delete.grid(row=4,column=100,padx=100)

select=Button(Frame1,text=" SELECT 📞",command=select,borderwidth=10,activeforeground="black",activebackground="black",font=("times",30,"bold"),bg="orange",fg="black")
select.grid(row=4,column=110)





root.mainloop()#call the main function in tkinter
