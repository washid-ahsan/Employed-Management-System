#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import customtkinter
from tkinter import messagebox


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("1000x600")
app.title("Employee Database Management")
app.resizable(False, False)

Label=customtkinter.CTkLabel(master=app,text="Employed Management System",font=("Footlight MT Light",30),text_color="#FFCC70")
Label.pack()

def search():
    import sqlite3
    conobj=sqlite3.connect(database="file.sqlite")
    curobj=conobj.cursor()
    eid=int(Entry_1.get())
    curobj.execute("select * from emp where empid=?",(eid,))
    rows=curobj.fetchall()
    for row in rows:
        rslt.configure(text_color='black',text=f"Name:{row[1]}\nSal:{row[2]}\nDep:{row[3]}")
    if(len(rows)==0):
        rslt.configure(text="empid does not exist",text_color='#A52A2A')
    conobj.close()

def delete():
 # Use a messagebox for confirmation
    result = messagebox.askokcancel("Delete Employee", "Are you sure you want to delete this employee?")
    
    if result:
        import sqlite3
        conobj = sqlite3.connect(database="file.sqlite")
        curobj = conobj.cursor()
        eid = int(Entry_1.get())
        curobj.execute("delete from emp where empid=?", (eid,))
        conobj.commit()
        count = curobj.rowcount
        if count != 0:
            rslt.configure(text_color='black', text="Emp deleted")
        if count == 0:
            rslt.configure(text="empid does not exist", text_color="#A52A2A")
        conobj.close()

def insert():
    import sqlite3
    conobj=sqlite3.connect(database="file.sqlite")
    curobj=conobj.cursor()
    eid=int(Entry_id.get())
    ename=Entry_name.get()
    esal=float(Entry_sal.get())
    edep=Entry_dept.get()
    try:
        curobj.execute("insert into emp values(?,?,?,?)",(eid,ename,esal,edep))
        conobj.commit()
        rslt_add.configure(text_color='black',text="Emp Inserted")
    except:    
        rslt_add.configure(text="something went wrong",text_color='#A52A2A')
    conobj.close()

def clear():
    Entry_id.delete(0,"end")
    Entry_name.delete(0,"end")
    Entry_sal.delete(0,"end")
    Entry_dept.delete(0,"end")
    Entry_id.focus()


#to search the existing employee
frame_1 = customtkinter.CTkFrame(master=app,width=360,height=250,fg_color="#8D6F3A",border_color="#FFCC70",border_width=2,)
frame_1.place(x=20,y=100)

Entry_1 = customtkinter.CTkEntry(master=app, placeholder_text="Write Emp Id...", width=200)
Entry_1.place(x=80, y=160)

btn_search=customtkinter.CTkButton(master=app,width=80,height=30,text="search",bg_color="#8D6F3A" ,corner_radius=30, fg_color="transparent", hover_color="#EE1289", border_color="#FFCC70", border_width=2,command=search)
btn_search.place(x=210,y=210)

btn_delete=customtkinter.CTkButton(master=app,width=80,height=30,text="delete",bg_color="#8D6F3A" ,corner_radius=30, fg_color="transparent", hover_color="#000000", border_color="#FFCC70", border_width=2,command=delete)
btn_delete.place(x=80,y=210)

rslt=customtkinter.CTkLabel(master=app,text="",font=("Arial",20),bg_color="#8D6F3A",text_color="white")
rslt.place(x=100,y=260)

#to add new employee
frame_2 = customtkinter.CTkFrame(master=app,width=400,height=300,fg_color="#556B2F",border_color="#CAFF70",border_width=2,)
frame_2.place(x=500,y=100)

Entry_id = customtkinter.CTkEntry(master=app, placeholder_text="Write Emp Id...", width=200)
Entry_id.place(x=600, y=140)

Entry_name = customtkinter.CTkEntry(master=app, placeholder_text="Write Emp Name...", width=200)
Entry_name.place(x=600, y=190)

Entry_sal = customtkinter.CTkEntry(master=app, placeholder_text="Write Emp Salary...", width=200)
Entry_sal.place(x=600, y=240)

Entry_dept = customtkinter.CTkEntry(master=app, placeholder_text="Write Emp Department...", width=200)
Entry_dept.place(x=600, y=290)

btn_clr=customtkinter.CTkButton(master=app,width=80,height=30,text="Clear",bg_color="#556B2F" ,corner_radius=30, fg_color="transparent", hover_color="#000000", border_color="#CAFF70", border_width=2,command=clear)
btn_clr.place(x=580,y=340)

btn_insrt=customtkinter.CTkButton(master=app,width=80,height=30,text="Insert",bg_color="#556B2F" ,corner_radius=30, fg_color="transparent", hover_color="#4158D0", border_color="#CAFF70", border_width=2,command=insert)
btn_insrt.place(x=750,y=340)

rslt_add=customtkinter.CTkLabel(master=app,text="",font=("Arial",15),bg_color="#556B2F",text_color="white")
rslt_add.place(x=660,y=367)

app.mainloop()

