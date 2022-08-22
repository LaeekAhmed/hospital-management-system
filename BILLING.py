from logging import PlaceHolder
import sqlite3
import tkinter
import tkinter.messagebox
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
        rootB, text_font="Verdana 12", text="Appointment set", fg_color="green")
    label_mode.place(x=200, y=400)
    label_mode.after(2000, label_mode.place_forget)


def up():
    global c1, b1, P_id, b3, b4, b5, b6, dd, treat_1, treat_2, cost_t, b7, b8, med, med_q, price, u
    conn = sqlite3.connect("MDBA.db")
    c1 = conn.cursor()
    b1 = P_id.get()
    b3 = treat_1.get(tkinter.ACTIVE)
    b4 = treat_2.get(tkinter.ACTIVE)
    b5 = cost_t.get()
    b6 = med.get(tkinter.ACTIVE)
    b7 = med_q.get(tkinter.ACTIVE)
    b8 = price.get()
    if(list(c1.execute("SELECT * FROM ROOM WHERE PATIENT_ID=?", (b1,))) == []):
        errorD = customtkinter.CTkLabel(
            rootB, text_font="Verdana 12", text="Error - Patiet must have an allocated room", fg_color="red")
        errorD.place(x=100, y=410)
        errorD.after(2000, errorD.place_forget)
    elif(list(conn.execute("Select * from treatment where PATIENT_ID=?", (b1,))) != []):
        errorD = customtkinter.CTkLabel(
            rootB, text_font="Verdana 12", text="ID Error - Patient's bill is already registered ", fg_color="red")
        errorD.place(x=100, y=410)
        errorD.after(2000, errorD.place_forget)
    else:
        conn.execute("INSERT INTO TREATMENT VALUES(?,?,?,?)",
                     (b1, b3, b4, b5,))
        conn.execute("INSERT INTO MEDICINE VALUES(?,?,?,?)", (b1, b6, b7, b8,))
        conn.commit()
        msg = customtkinter.CTkLabel(
            rootB, text_font="Verdana 12", text="details updated", fg_color="green")
        msg.place(x=200, y=400)
        msg.after(2000, msg.place_forget)


def calci():
    global b1
    conn = sqlite3.connect("MDBA.db")
    u = conn.execute(
        "Select sum(T_COST+ (M_COST*M_QTY) +(DATE_DISCHARGED-DATE_ADMITTED)*RATE) FROM ROOM NATURAL JOIN TREATMENT natural JOIN MEDICINE where PATIENT_ID=?", (b1,))
    conn.commit()
    for ii in u:
        pp = customtkinter.CTkLabel(
            rootB, text_font="Verdana 12", fg_color='green', text="TOTAL AMOUNT OUTSTANDING :")
        pp.place(y=300, x=50)
        uu = customtkinter.CTkLabel(
            rootB, fg_color='green', text_font="Verdana 12", text='$ '+str(ii[0]))
        uu.place(y=300, x=350)


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
        rootB, text_font="Verdana 12", text="PATIENT BILL :")
    head.grid(row=10, column=5)
    P_id = customtkinter.CTkEntry(
        rootB, text_font="Verdana 12", placeholder_text="patient id")
    P_id.grid(row=20, column=5)
    dd = customtkinter.CTkEntry(
        rootB, text_font="Verdana 12", placeholder_text="Date discharged")
    dd.grid(row=50, column=5)
    ddp = customtkinter.CTkButton(
        rootB, text_font="Verdana 12", text="UPDATE DISCHARGE DATE", command=date_up)
    ddp.grid(row=45, column=15)
    treat = customtkinter.CTkLabel(
        rootB, text_font="Verdana 12", text="SELECT TREATMENT:")
    treat.grid(row=60, column=15)
    L1 = ["QUARANTINE", "SURGERY", "LAB TEST", "CONSULTAION"]
    treat_1 = tkinter.Listbox(
        rootB, width=15, height=1, selectmode='SINGLE', exportselection=0)
    for j in L1:
        treat_1.insert(tkinter.END, j)
    treat_1.grid(row=65, column=15)
    treat_c = customtkinter.CTkLabel(
        rootB, text_font="Verdana 12", text="CODE:")
    treat_c.grid(row=60, column=5)
    L2 = ["C_1", "S_1", "L_1"]
    treat_2 = tkinter.Listbox(rootB, width=6, height=1,
                              selectmode='SINGLE', exportselection=0)
    for jj in L2:
        treat_2.insert(tkinter.END, jj)
    treat_2.grid(row=65, column=5)
    cost_t = customtkinter.CTkEntry(
        rootB, text_font="Verdana 12", placeholder_text="cost")
    cost_t.grid(row=77, column=5)
    med1 = customtkinter.CTkLabel(
        rootB, text_font="Verdana 12", text="SELECT MEDICINE:")
    med1.grid(row=87, column=5)
    L3 = ["CHLOROQUINE", "FAVILAVIR", "BRUFEN", "DISPRIN", "BANDAGE", "DIGENE"]
    med = tkinter.Listbox(rootB, width=15, height=1,
                          selectmode='SINGLE', exportselection=0)
    for jjj in L3:
        med.insert(tkinter.END, jjj)
    med.grid(row=92, column=5)
    med_ql = customtkinter.CTkLabel(
        rootB, text_font="Verdana 12", text="QUANTITY")
    med_ql.grid(row=87, column=15)
    L4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    med_q = tkinter.Listbox(rootB, width=4, height=1,
                            selectmode='SINGLE', exportselection=0)
    for jjjj in L4:
        med_q.insert(tkinter.END, jjjj)
    med_q.grid(row=92, column=15)
    price = customtkinter.CTkEntry(
        rootB, text_font="Verdana 12", placeholder_text="price")
    price.grid(row=100, column=5)
    b1 = customtkinter.CTkButton(
        rootB, text_font="Verdana 12", text="Generate bill", command=calci)
    b1.place(x=190, y=500)
    b2 = customtkinter.CTkButton(
        rootB, text_font="Verdana 12", text="Submit", command=up)
    b2.place(x=10, y=500)
    rootbil.mainloop()


# BILLING()
