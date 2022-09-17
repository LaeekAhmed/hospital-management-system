import tkinter
import tkinter.messagebox
from turtle import width
import customtkinter
import sqlite3
rootE = None
rootEmp = None
var = None


def inp():
    global e1, e2, e3, e4, e5, e6, e7, e8, e9, var
    e1 = t1.get()
    e2 = t2.get()
    e3 = str(var.get())
    e4 = t3.get()
    e5 = lb.get()
    e6 = t4.get()
    e7 = t5.get()
    e8 = t6.get()
    e9 = t7.get()
    if(len(str(e1)) == 0 or len(str(e2)) == 0):
        errorD = customtkinter.CTkLabel(
            rootE, text_font="Verdana 12", text="Please fill all the required fields (*)", corner_radius=8,fg_color='red')
        errorD.pack(side=tkinter.BOTTOM, pady=10)
        errorD.after(2000, errorD.pack_forget)
    else:
        conn = sqlite3.connect("MDBA.db")
        conn.execute("INSERT INTO employee VALUES(?,?,?,?,?,?,?,?,?)",
                     (e1, e2, e3, e4, e5, e6, e7, e8, e9,))
        conn.commit()
        label_mode = customtkinter.CTkLabel(
            rootE, text_font="Verdana 12", text="Employee Data added", corner_radius=8,fg_color="green")
        label_mode.pack(side=tkinter.BOTTOM, pady=10)


def showframe(frame):
    frame.tkraise()


def emp_screen():
    global rootEmp, rootE, t1, t2, r1, r2, t3, lb, t4, t5, t6, t7, var
    rootEmp = customtkinter.CTk()
    rootEmp.title("Employee Registration")
    rootEmp.geometry('500x500')
    rootEmp.rowconfigure(0, weight=1)
    rootEmp.columnconfigure(0, weight=1)
    var = tkinter.StringVar(master=rootEmp)
    rootE = customtkinter.CTkFrame(rootEmp)
    delo()
    for frame in (rootE, rootDE):
        frame.grid(row=0, column=0, padx=30, pady=30, sticky='nsew')
    showframe(rootE)

    H = customtkinter.CTkLabel(rootE, text_font="Verdana 13", text="Employee Registration ;",
                               corner_radius=8,fg_color='black')
    H.place(x=50, y=20)
    t1 = customtkinter.CTkEntry(
        rootE, text_font="Verdana 12", placeholder_text="Employee ID *")
    t1.place(x=30, y=60)
    t2 = customtkinter.CTkEntry(
        rootE, text_font="Verdana 12", placeholder_text="Employee Name *", width=200)
    t2.place(x=200, y=60)
    l3 = customtkinter.CTkLabel(rootE, text_font="Verdana 12", text="Sex:")
    l3.place(x=0, y=108)
    r1 = customtkinter.CTkRadioButton(
        rootE, text_font="Verdana 12", text="male", variable=var, value="Male")
    r1.place(x=90, y=110)
    r2 = customtkinter.CTkRadioButton(
        rootE, text_font="Verdana 12", text="Female", variable=var, value="Female")
    r2.place(x=180, y=110)
    t3 = customtkinter.CTkEntry(
        rootE, text_font="Verdana 12", placeholder_text="Age")
    t3.place(x=30, y=140)
    l5 = customtkinter.CTkLabel(
        rootE, text_font="Verdana 12", text="Employee type:")
    l5.place(x=30, y=170)
    lb = customtkinter.CTkOptionMenu(
        rootE, values=['Doctor','Nurse','Oher'], text_font="Verdana 12")
    lb.place(x=200, y=170)
    t4 = customtkinter.CTkEntry(
        rootE, text_font="Verdana 12", placeholder_text="Salary")
    t4.place(x=30, y=200)
    t5 = customtkinter.CTkEntry(
        rootE, text_font="Verdana 12", placeholder_text="Experience")
    t5.place(x=30, y=230)
    t6 = customtkinter.CTkEntry(
        rootE, text_font="Verdana 12", placeholder_text="Mobile no.")
    t6.place(x=30, y=260)
    t7 = customtkinter.CTkEntry(
        rootE, text_font="Verdana 12", placeholder_text="Email ID")
    t7.place(x=30, y=290)
    b1 = customtkinter.CTkButton(
        rootE, text_font="Verdana 12", text="Save", command=inp)
    b1.place(x=30, y=350)
    b2 = customtkinter.CTkButton(
        rootE, text_font="Verdana 12", text="Delete Employee", command=lambda: showframe(rootDE))
    b2.place(x=180, y=350)
    rootEmp.mainloop()


def delling():
    global d1, de
    de = str(d1.get())
    conn = sqlite3.connect("MDBA.db")
    p = list(conn.execute("select * from employee where EMP_ID=?", (de,)))
    if(len(str(de)) == 0):
        error = customtkinter.CTkLabel(
            rootDE, text_font="Verdana 12", text="Please fill all the required fields (*)", corner_radius=8,fg_color='red')
        error.pack(side=tkinter.BOTTOM, pady=10)
        error.after(2000, error.pack_forget)
    elif (len(p) != 0):
        conn.execute("DELETE from employee where EMP_ID=?", (de,))
        dme = customtkinter.CTkLabel(
            rootDE, text_font="Verdana 12", text="Employee Deleted from database", corner_radius=8,fg_color="green")
        #dme.place(x=20, y=100)
        dme.pack(side=tkinter.BOTTOM, pady=10)
        dme.after(2000, dme.pack_forget)
        conn.commit()
        print("cp1")
    else:
        error = customtkinter.CTkLabel(
            rootDE, text_font="Verdana 12", text="Employee Doesn't exist", corner_radius=8,fg_color="red")
        error.pack(side=tkinter.BOTTOM, pady=10)
        error.after(2000, error.pack_forget)
        print("cp2")


rootDE = None


def delo():
    global rootDE, d1
    rootDE = customtkinter.CTkFrame(rootEmp)
    d1 = customtkinter.CTkEntry(
        rootDE, text_font="Verdana 12", placeholder_text="Emp id to delete * ", width=170)
    d1.place(x=20, y=10)
    B1 = customtkinter.CTkButton(
        rootDE, text_font="Verdana 12", text="Delete", command=delling)
    B1.place(x=20, y=50)
    B2 = customtkinter.CTkButton(
        rootDE, text_font="Verdana 12", text="Back", command=lambda: showframe(rootE)).place(x=20, y=150)

#emp_screen()
