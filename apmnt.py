from distutils.log import error
import tkinter
import tkinter.scrolledtext as st
import sqlite3
from turtle import width
import customtkinter
conn = sqlite3.connect("MDBA.db")
rootAA = None
rootapp = None


def set():
    global e3, e1, e2, e4, e5, e6, conn
    p1 = e1.get()
    p2 = e2.get()
    p3 = e3.get(tkinter.ACTIVE)
    p4 = e4.get()
    p5 = e5.get()
    p6 = e6.get(1.0, tkinter.END)
    conn = sqlite3.connect("MDBA.db")
    #print(p1, p3)
    if(len(str(p1)) == 0 or len(str(p3)) > 3):
        errorD = customtkinter.CTkLabel(
            rootAA, text_font="Verdana 12", text="Please fill all the required fields Properly(*)", fg_color='red')
        errorD.place(x=20, y=480)
        errorD.after(2000, errorD.place_forget)
    else:
        conn.execute("Insert into Appointment values(?,?,?,?,?,?)",
                     (p1, p2, p3, p4, p5, p6))
        conn.commit()
        label_mode = customtkinter.CTkLabel(
            rootAA, text_font="Verdana 12", text="Appointment set", fg_color="green")
        label_mode.pack(side=tkinter.BOTTOM, pady=10)
        label_mode.after(2000, label_mode.pack_forget)


def showframe(frame):
    frame.tkraise()


def appo():
    global rootAA, L, e1, e2, e3, e4, e5, e6, rootapp
    rootapp = customtkinter.CTk()
    rootapp.geometry("650x600")
    rootapp.title("Appointments")
    rootapp.rowconfigure(0, weight=1)
    rootapp.columnconfigure(0, weight=1)
    rootAA = customtkinter.CTkFrame(rootapp)

    va()
    for frame in (rootAA, rootAP):
        frame.grid(row=0, column=0, padx=30, pady=30, sticky='nsew')
    showframe(rootAA)
    H = customtkinter.CTkLabel(rootAA, text_font="Verdana 12", text="APOINTMENTS:-",
                               fg_color="black")
    H.place(x=55, y=15)
    e1 = customtkinter.CTkEntry(
        rootAA, text_font="Verdana 12", placeholder_text="patient id * ")
    e1.place(x=20, y=55)
    e2 = customtkinter.CTkEntry(
        rootAA, text_font="Verdana 12", placeholder_text="Doctor id")
    e2.place(x=170, y=55)
    l3 = customtkinter.CTkLabel(
        rootAA, text_font="Verdana 12", text="Appointment No. * (⬇⬆) ")
    l3.place(x=5, y=100)
    L = ['select', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15',
         'A16', 'A17', 'A18', 'A19', 'A20', 'A21', 'A22', 'A23', 'A24', 'A25', 'A26', 'A27', 'A28', 'A29', 'A30']
    e3 = tkinter.Listbox(rootAA, width=15, height=1,
                         selectmode='SINGLE', exportselection=0)
    for jjj in L:
        e3.insert(tkinter.END, jjj)
    e3.place(x=750, y=320)
    e4 = customtkinter.CTkEntry(
        rootAA, text_font="Verdana 12", placeholder_text="Appointment time:-(HH:MM:SS)", width=300)
    e4.place(x=20, y=145)
    e5 = customtkinter.CTkEntry(
        rootAA, text_font="Verdana 12", placeholder_text="Appointment Date:-(YYYY-MM-DD)", width=300)
    e5.place(x=20, y=190)
    l6 = customtkinter.CTkLabel(
        rootAA, text_font="Verdana 12", text="Description")
    l6.place(x=5, y=230)
    e6 = tkinter.Text(rootAA, width=20, height=3)
    e6.place(x=420, y=710)
    b1 = customtkinter.CTkButton(
        rootAA, text_font="Verdana 12", text="Set Appointment", command=set)
    b1.place(x=20, y=310)
    b2 = customtkinter.CTkButton(
        rootAA, text_font="Verdana 12", text="Delete Appointment", command=dela)
    b2.place(x=180, y=310)
    b4 = customtkinter.CTkButton(
        rootAA, text_font="Verdana 12", text="Today's Appointments", command=lambda: showframe(rootAP))
    b4.place(x=365, y=310)
    rootapp.mainloop()


def remove():
    global e7, edd
    edd = str(e7.get())
    v = list(conn.execute("select * from Appointment where AP_NO=?", (edd,)))
    if (len(v) == 0):
        errorD = customtkinter.CTkLabel(
            rootAA, text_font="Verdana 12", text="Patient Appointment Not Fixed", fg_color='red')
        errorD.place(x=20, y=480)
        errorD.after(2000, errorD.place_forget)
    else:
        conn.execute("Delete from Appointment where AP_NO=?", (edd,))
        disd1 = customtkinter.CTkLabel(
            rootAA, text_font="Verdana 12", text="Patient Appointment Deleted", fg_color='green')
        disd1.place(x=20, y=480)
        disd1.after(2000, disd1.place_forget)
        conn.commit()


def dela():
    global e1, e7
    l3 = customtkinter.CTkLabel(
        rootAA, text_font="Verdana 12", text="Enter Appointment no. to Delete")
    l3.place(x=20, y=360)
    e7 = customtkinter.CTkEntry(rootAA, text_font="Verdana 12")
    e7.place(x=20, y=390)
    b3 = customtkinter.CTkButton(
        rootAA, text_font="Verdana 12", text="Delete", command=remove)
    b3.place(x=20, y=430)


rootAP = None


def viewAppointment():
    global e8
    ap = str(e8.get())
    vv = list(conn.execute("select * from Appointment where AP_Date=?", (ap,)))
    if (len(vv) == 0):
        errorD = customtkinter.CTkLabel(
            rootAP, text_font="Verdana 12", text="No Appointment For Today", fg_color="red")
        errorD.place(x=20, y=420)
        errorD.after(2000, errorD.place_forget)
    else:
        s = conn.execute(
            "Select * from Appointment where AP_Date=?", (ap,))
        text_area = st.ScrolledText(rootAP,
                                    width=40,
                                    height=10,
                                    bg='black',
                                    fg="white",
                                    font=("Verdana",
                                          15))

        text_area.place(x=100, y=700)

        # Inserting Text which is read only
        for i in s:
            # s1 = customtkinter.CTkLabel(
            #     rootAP, text_font="Verdana 12", text="patient id : "+str(i[0]))
            # s2 = customtkinter.CTkLabel(
            #     rootAP, text_font="Verdana 12", text="Appointment no. : ("+i[2])
            text_area.insert(tkinter.INSERT, "  patient id : (" +
                             str(i[0])+") , "+"Appointment no. : ("+i[2]+')\n')
        # Making the text read only
        text_area.configure(state='disabled')


def va():
    global rootAP, e8
    rootAP = customtkinter.CTkFrame(rootapp)
    h1 = customtkinter.CTkLabel(
        rootAP, text_font="Verdana 12", text="Enter Date To View Appointments;")
    h1.place(x=20, y=20)
    e8 = customtkinter.CTkEntry(rootAP, text_font="Verdana 12")
    e8.place(x=20, y=50)
    b5 = customtkinter.CTkButton(
        rootAP, text_font="Verdana 12", text="Search", command=viewAppointment)
    b5.place(x=20, y=100)
    b4 = customtkinter.CTkButton(
        rootAP, text_font="Verdana 12", text="Back", command=lambda: showframe(rootAA))
    b4.place(x=20, y=150)


# appo()
