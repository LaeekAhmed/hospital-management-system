from distutils.log import error
import sqlite3
import tkinter
import customtkinter
import tkinter.messagebox
conn = sqlite3.connect("MDBA.db")

P_id = None
rootR = None
rootaloc = None
rootRD = None

# room BUTTON


def room_button():
    global P_id, r1, r2, room_t, da, dd, rate, room_no, r3, r4, r5, r6, conn
    conn = sqlite3.connect("MDBA.db")
    r1 = P_id.get()
    r2 = room_t.get()
    r3 = room_no.get()
    r4 = rate.get()
    r5 = da.get()
    r6 = dd.get()
    pid = list(conn.execute("Select * from room where PATIENT_ID=?", (r1,)))
    if(len(str(r1)) == 0 or str(r3) == "select"):
        errorD = customtkinter.CTkLabel(
            rootR, text_font="Verdana 12", text="Please fill all the required fields (*)", corner_radius=8,fg_color='red')
        errorD.pack(side=tkinter.BOTTOM, pady=10)
        errorD.after(2000, errorD.pack_forget)
    else:
        p = list(conn.execute("Select * from room where ROOM_NO=?", (r3,)))
        if(list(conn.execute("SELECT * FROM PATIENT WHERE PATIENT_ID=?", (r1,))) == []):
            print("cp1")
            errorP = customtkinter.CTkLabel(
                rootR, text_font="Verdana 12", text="Error - Patient must be registered", corner_radius=8, fg_color="red")
            errorP.pack(side=tkinter.BOTTOM, pady=10)
            errorP.after(2000, errorP.pack_forget)
        elif(len(pid)!=0):
            label_mode2 = customtkinter.CTkLabel(
                rootR, text_font="Verdana 12", text="Patient has a booked room/use update", corner_radius=8,fg_color="red")
            label_mode2.pack(side=tkinter.BOTTOM, pady=10)
            label_mode2.after(2000, label_mode2.pack_forget)
        elif len(p) == 0:
            conn.execute('INSERT INTO room VALUES(?,?,?,?,?,?)',
                         (r1, r3, r2, r4, r5, r6,))
            label_mode = customtkinter.CTkLabel(
                rootR, text_font="Verdana 12", text="Room Allocated", corner_radius=8,fg_color="green")
            label_mode.pack(side=tkinter.BOTTOM, pady=10)
            label_mode.after(2000, label_mode.pack_forget)
        else:
            print("hello")
            label_mode = customtkinter.CTkLabel(
                rootR, text_font="Verdana 12", text="Room Already Occupied", corner_radius=8,fg_color="red")
            label_mode.pack(side=tkinter.BOTTOM, pady=10)
            label_mode.after(2000, label_mode.pack_forget)
    conn.commit()
    c1 = conn.cursor()
    c1.execute("select * from room")
    results = c1.fetchall()
    print("records : \n")
    for x in results:
        print(x)


def update_button():
    global P_id, r1, r2, room_t, da, dd, rate, room_no, r3, r4, r5, r6, conn
    r1 = P_id.get()
    r2 = room_t.get()
    r3 = room_no.get()
    r4 = rate.get()
    r5 = da.get()
    r6 = dd.get()
    p = list(conn.execute("Select * from room where PATIENT_ID=?", (r1,)))
    pr = list(conn.execute("Select * from room where ROOM_NO=?", (r3,)))
    if(len(pr)!=0):
        label_mode8 = customtkinter.CTkLabel(
            rootR, text_font="Verdana 12", text="Room Already Occupied", corner_radius=8,fg_color="red")
        label_mode8.pack(side=tkinter.BOTTOM, pady=10)
        label_mode8.after(2000, label_mode8.pack_forget)
    elif len(p) != 0:
        conn.execute(
            'UPDATE room SET room_NO=?,room_Type=?,RATE=?,DATE_ADMITTED=?,DATE_DISCHARGED=? where PATIENT_ID=?', (r3, r2, r4, r5, r6, r1,))
        label_mode = customtkinter.CTkLabel(
            rootR, text_font="Verdana 12", text="Details Updated", corner_radius=8,fg_color="green")
        label_mode.pack(side=tkinter.BOTTOM, pady=10)
        label_mode.after(2000, label_mode.pack_forget)
        conn.commit()
    else:
        label_mode = customtkinter.CTkLabel(
            rootR, text_font="Verdana 12", text="Error - Patient Not Registered", corner_radius=8,fg_color="red")
        label_mode.pack(pady=10, side=tkinter.BOTTOM)
        label_mode.after(2000, label_mode.pack_forget)
    c1 = conn.cursor()
    c1.execute("select * from room")
    results = c1.fetchall()
    print("records : \n")
    for x in results:
        print(x)

# FUNCTION FOR room DISPLAY BUTTON


def roomD_button():
    global r1, lr1, dis1, lr2, dis2, c1, ii, conn, c1, P_iid
    conn = sqlite3.connect("MDBA.db")
    c1 = conn.cursor()
    r1 = P_iid.get()
    p = list(c1.execute('select * from  room  where PATIENT_ID=?', (r1,)))
    if (len(p) == 0):
        label_mode = customtkinter.CTkLabel(
            rootRD, text_font="Verdana 12", text="Error - Patient Not Registered", corner_radius=8,fg_color="red")
        label_mode.pack(pady=10, side=tkinter.BOTTOM)
        label_mode.after(2000, label_mode.pack_forget)
    else:
        ii = p[0]
        lr0 = customtkinter.CTkLabel(
            rootRD, text_font="Verdana 12", text="Patient ID : ")
        dis0 = customtkinter.CTkLabel(
            rootRD, text_font="Verdana 12", text=ii[0])
        lr0.place(x=50, y=260)
        dis0.place(x=200, y=260)
        lr1 = customtkinter.CTkLabel(
            rootRD, text_font="Verdana 12", text="room NO : ")
        dis1 = customtkinter.CTkLabel(
            rootRD, text_font="Verdana 12", text=ii[1])
        lr1.place(x=50, y=290)
        dis1.place(x=200, y=290)
        lr2 = customtkinter.CTkLabel(
            rootRD, text_font="Verdana 12", text="room Type : ")
        dis2 = customtkinter.CTkLabel(
            rootRD, text_font="Verdana 12", text=ii[2])
        lr2.place(x=50, y=320)
        dis2.place(x=200, y=320)
    c1 = conn.cursor()
    c1.execute("select * from room")
    results = c1.fetchall()
    print("records : \n")
    for x in results:
        print(x)


def showframe(frame):
    frame.tkraise()


def roomDD():
    global rootRD, ra1, ss, P_iid
    rootRD = customtkinter.CTkFrame(rootaloc)
    P_iid = customtkinter.CTkEntry(
        rootRD, text_font="Verdana 12", placeholder_text="patient id")
    ss = customtkinter.CTkButton(
        rootRD, text_font="Verdana 12", text="Search", command=roomD_button)
    P_iid.place(x=50, y=50)
    ss.place(x=50, y=100)
    e = customtkinter.CTkButton(
        rootRD, text_font="Verdana 12", text="Back", command=lambda: showframe(rootR))
    e.place(x=150, y=200)


L = None
L1 = None


def room_all():
    global rootaloc, rootR, r_head, P_id, id, room_tl, L, i, room_t, room_nol, room_no, L1, j, ratel, rate, da_l, da, dd_l, dd, Submit, Update, cr
    rootaloc = customtkinter.CTk()
    rootaloc.title("room Allocation")
    rootaloc.geometry("550x500")
    rootaloc.rowconfigure(0, weight=1)
    rootaloc.columnconfigure(0, weight=1)
    rootR = customtkinter.CTkFrame(rootaloc)
    roomDD()
    for frame in (rootR, rootRD):
        frame.grid(row=0, column=0, padx=30, pady=30, sticky='nsew')
    showframe(rootR)

    r_head = customtkinter.CTkLabel(
        rootR, text_font="Verdana 13", text="Room Allocation ;",corner_radius=8,fg_color='black')
    r_head.place(x=30, y=15)
    P_id = customtkinter.CTkEntry(
        rootR, text_font="Verdana 12", placeholder_text="Patient id * ")
    P_id.place(x=50, y=60)
    room_tl = customtkinter.CTkLabel(
        rootR, text_font="Verdana 12", text="Room Type: (⬆⬇)")
    room_tl.place(x=30, y=110)
    room_t = customtkinter.CTkOptionMenu(
        rootR, values=["select","SINGLE room: $ 600","TWIN SHARING : $ 500","TRIPLE SHARING: $ 400"], text_font="Verdana 12")  # value selected will be arg for the func()
    room_t.place(x=200, y=110)
    room_nol = customtkinter.CTkLabel(
        rootR, text_font="Verdana 12", text="Room Number * (⬆⬇)")
    room_nol.place(x=30, y=170)
    L1 = ['select', '101', '102-AA', '102-BB', '103', '104-AA', '104-BB', '105', '206-AAA', '206-BBB',
          '206-CCC', '207', '208-AAA', '208-BBB', '208-CCC', '210', '211', '302', '304-AA', '304-BB']
    room_no = customtkinter.CTkOptionMenu(
        rootR, values=L1, text_font="Verdana 12")
    room_no.place(x=220, y=170)
    rate = customtkinter.CTkEntry(
        rootR, text_font="Verdana 12", placeholder_text="Room Charges")
    rate.place(x=50, y=220)
    da = customtkinter.CTkEntry(
        rootR, text_font="Verdana 12", placeholder_text="Date dmitted")
    da.place(x=50, y=260)
    dd = customtkinter.CTkEntry(
        rootR, text_font="Verdana 12", placeholder_text="Date discharged", width=150)
    dd.place(x=50, y=300)
    Submit = customtkinter.CTkButton(
        rootR, text_font="Verdana 12", text="Submit", command=room_button)
    Submit.pack(side=tkinter.BOTTOM, pady=10)
    Update = customtkinter.CTkButton(
        rootR, text_font="Verdana 12", text="Update", command=update_button)
    Update.place(x=20, y=402)
    cr = customtkinter.CTkButton(
        rootR, text_font="Verdana 12", text='Room Details', command=lambda: showframe(rootRD))
    cr.place(x=330, y=402)
    rootaloc.mainloop()


room_all()
