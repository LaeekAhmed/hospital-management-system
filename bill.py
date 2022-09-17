from logging import PlaceHolder
import sqlite3
import tkinter
import tkinter.messagebox
from turtle import width
import customtkinter
conn = sqlite3.connect("MDBA.db")

# variables
rootB = None


def date_up():
    global b1, b2
    b1 = P_id.get()
    b2 = dd.get()
    conn.execute(
        "UPDATE ROOM SET DATE_DISCHARGED=? where PATIENT_ID=?", (b2, b1,))
    conn.commit()
    label_mode = customtkinter.CTkLabel(
        rootB, text_font="Verdana 12", text="Appointment set", corner_radius=8, fg_color="green")
    label_mode.place(x=200, y=400)
    label_mode.after(2000, label_mode.place_forget)


def up():
    global c1, b1, P_id, b3, b4, b5, b6, dd, treat_1, treat_2, cost_t, b7, b8, med, med_q, price, u
    conn = sqlite3.connect("MDBA.db")
    c1 = conn.cursor()
    b1 = P_id.get()
    b3 = treat_1.get()
    b4 = treat_2.get()
    b5 = cost_t.get()
    b6 = med.get()
    b7 = med_q.get()
    b8 = price.get()
    if(list(c1.execute("SELECT * FROM ROOM WHERE PATIENT_ID=?", (b1,))) == []):
        errorD = customtkinter.CTkLabel(
            rootB, text_font="Verdana 12", text="Error - Patiet must have an allocated room", corner_radius=8, fg_color="red")
        errorD.place(x=100, y=410)
        errorD.after(2000, errorD.place_forget)
    elif(list(conn.execute("Select * from treatment where PATIENT_ID=?", (b1,))) != []):
        errorD = customtkinter.CTkLabel(
            rootB, text_font="Verdana 12", text="ID Error - Patient's bill is already registered ", corner_radius=8, fg_color="red")
        errorD.place(x=100, y=410)
        errorD.after(2000, errorD.place_forget)
    else:
        conn.execute("INSERT INTO TREATMENT VALUES(?,?,?,?)",
                     (b1, b3, b4, b5,))
        conn.execute("INSERT INTO MEDICINE VALUES(?,?,?,?)", (b1, b6, b7, b8,))
        conn.commit()
        msg = customtkinter.CTkLabel(
            rootB, text_font="Verdana 12", text="details updated", corner_radius=8, fg_color="green")
        msg.place(x=200, y=400)
        msg.after(2000, msg.place_forget)


def calci():
    global b1
    b1 = P_id.get()
    conn = sqlite3.connect("MDBA.db")
    u = conn.execute(
        "Select sum(T_COST+ (M_COST*M_QTY) +(DATE_DISCHARGED-DATE_ADMITTED)*RATE) FROM ROOM NATURAL JOIN TREATMENT natural JOIN MEDICINE where PATIENT_ID=?", (b1,))
    conn.commit()
    for ii in u:
        pp = customtkinter.CTkLabel(
            rootB, text_font="Verdana 12", corner_radius=8, fg_color='green', text="Total cost :")
        pp.place(y=350, x=50)
        uu = customtkinter.CTkLabel(
            rootB, corner_radius=8, fg_color='green', text_font="Verdana 12", text='$ '+str(ii[0]))
        uu.place(y=350, x=200)


L1 = None
L2 = None
L3 = None
L4 = None


def showframe(frame):
    frame.tkraise()


def exitt():
    rootB.destroy()


def BILLING():
    global rootB, L1, treat1, P_id, dd, cost, med, med_q, price, treat_1, treat_2, cost_t, j, jj, jjj, jjjj, L2, L3, L4
    rootbil = customtkinter.CTk()
    rootbil.geometry("600x600")
    rootbil.rowconfigure(0, weight=1)
    rootbil.columnconfigure(0, weight=1)
    rootbil.title("BILLING SYSTEM")

    rootB = customtkinter.CTkFrame(rootbil)
    rootB.grid(row=0, column=0, padx=15, pady=20, sticky='nsew')
    head = customtkinter.CTkLabel(
        rootB, text_font="Verdana 13", text="Patient bill ;",corner_radius=8,fg_color='black')
    head.place(x=30,y=10)
    P_id = customtkinter.CTkEntry(
        rootB, text_font="Verdana 12", placeholder_text="patient id")
    P_id.place(x=30,y=50)
    dd = customtkinter.CTkEntry(
        rootB, text_font="Verdana 12",width=180, placeholder_text="Date discharged")
    dd.place(x=30,y=90)
    ddp = customtkinter.CTkButton(
        rootB, text_font="Verdana 12", text="Upd discharge date", command=date_up)
    ddp.place(x=310, y=500)
    treat = customtkinter.CTkLabel(
        rootB, text_font="Verdana 12", text="Select treatment:")
    treat.place(x=330,y=50)
    L1 = ["quarantine", "surgery", "lab test", "consultaion"]
    treat_1 = customtkinter.CTkOptionMenu(
        rootB, values=L1, text_font="Verdana 12")
    treat_1.place(x=330,y=80)
    treat_c = customtkinter.CTkLabel(
        rootB, text_font="Verdana 12", text="code:")
    treat_c.place(x=330,y=130)
    L2 = ["C_1", "S_1", "L_1"]
    treat_2 = customtkinter.CTkOptionMenu(
        rootB, values=L2, text_font="Verdana 12")
    treat_2.place(x=330,y=160)
    med1 = customtkinter.CTkLabel(
        rootB, text_font="Verdana 12", text="Select medicine:")
    med1.place(x=330,y=210)
    L3 = ["chloroquine", "favilavir", "brufen", "disprin", "bandage", "digene"]
    med = customtkinter.CTkOptionMenu(
        rootB, values=L3, text_font="Verdana 12")
    med.place(x=330,y=240)
    med_ql = customtkinter.CTkLabel(
        rootB, text_font="Verdana 12", text="Quantity:")
    med_ql.place(x=30,y=220)
    L4 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    x = map(str,L4)
    med_q = customtkinter.CTkOptionMenu(
        rootB, values=list(x), text_font="Verdana 12")
    med_q.place(x=30,y=250)
    cost_t = customtkinter.CTkEntry(
        rootB, text_font="Verdana 12", placeholder_text="cost")
    cost_t.place(x=30,y=170)
    price = customtkinter.CTkEntry(
        rootB, text_font="Verdana 12", placeholder_text="price")
    price.place(x=30,y=130)
    b1 = customtkinter.CTkButton(
        rootB, text_font="Verdana 12", text="Generate bill", command=calci)
    b1.place(x=160, y=500)
    b2 = customtkinter.CTkButton(
        rootB, text_font="Verdana 12", text="Submit", command=up)
    b2.place(x=10, y=500)
    rootbil.mainloop()

# BILLING()
