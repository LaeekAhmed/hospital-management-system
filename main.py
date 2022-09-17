import tkinter
import sqlite3
import tkinter.messagebox
import customtkinter
from pat_del_up import P_display
#from PATDELSU import D_display
from pat_del_up import P_UPDATE
from room_alloc import room_all
from bill import BILLING
from empl_reg import emp_screen
from apmnt import appo
import tkinter.scrolledtext as st


conn = sqlite3.connect("MDBA.db")  # will be created if doesn't exist.
print("DATABASE CONNECTION SUCCESSFUL\n(from window2.py)")

# variables
root1 = None
rootp = None
topframe = None
pat_ID = None
pat_name = None
pat_dob = None
pat_address = None
pat_sex = None
pat_BG = None
pat_email = None
pat_contact = None
pat_contactalt = None
pat_CT = None

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("dark")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")


def change_appearance_mode(new_appearance_mode):
    customtkinter.set_appearance_mode(new_appearance_mode)

# MENU BUTTONS


def showframe(frame):
    frame.tkraise()


def menu():
    global rootV,root1, button1, button2, button3, button4, button5, m, button6, topframe
    root1 = customtkinter.CTk()
    root1.geometry("580x600")
    root1.rowconfigure(0, weight=1)
    root1.columnconfigure(0, weight=1)
    root1.title("MAIN MENU")
    #root1.configure(bg='pale goldenrod')
    rootV = customtkinter.CTkFrame(root1)
    topframe = customtkinter.CTkFrame(root1)
    PAT()
    viewRecords()
    for frame in (topframe, rootp,rootV):
        frame.grid(row=0, column=0, padx=30, pady=30, sticky='nsew')
    showframe(topframe)
    #topframe.pack(pady=20, padx=20, fill="both", expand=True)

    m = customtkinter.CTkLabel(
        topframe, text="Select an option : ", text_font="Verdana 13")
    button1 = customtkinter.CTkButton(
        topframe, text="1 - Patient Registration", text_font="Verdana 12", command=lambda: showframe(rootp))
    button2 = customtkinter.CTkButton(
        topframe, text="2 - Room Allocation", text_font="Verdana 12", command=room_all)
    button3 = customtkinter.CTkButton(
        topframe, text="3 - Employee Registration", text_font="Verdana 12", command=emp_screen)
    button4 = customtkinter.CTkButton(
        topframe, text="4 - Book Appointment", text_font="Verdana 12", command=appo)
    button5 = customtkinter.CTkButton(
        topframe, text="5 - Patient Billing", text_font="Verdana 12", command=BILLING)
    m.place(x=55, y=5)
    button1.pack(side=tkinter.TOP)
    button1.place(x=80, y=50)
    button2.pack(side=tkinter.TOP)
    button2.place(x=80, y=100)
    button3.pack(side=tkinter.TOP)
    button3.place(x=80, y=150)
    button4.pack(side=tkinter.TOP)
    button4.place(x=80, y=200)
    button5.pack(side=tkinter.TOP)
    button5.place(x=80, y=250)
    # mode chnage button;
    label_mode = customtkinter.CTkLabel(
        topframe, text_font="Verdana 12", text="Appearance Mode:")
    label_mode.place(x=55, y=400)

    optionmenu_1 = customtkinter.CTkOptionMenu(
        topframe, values=["Light", "Dark", "System"], text_font="Verdana 12", command=change_appearance_mode)
    optionmenu_1.place(x=80, y=450)

    root1.mainloop()


p = None
# input patient form


def IN_PAT():  # insert values from patient reg. form into table PATIENT
    global pp1, pp2, pp3, pp4, pp5, pp6, pp7, pp8, pp9, pp10, ce1, conn
    conn = sqlite3.connect("MDBA.db")
    conn.cursor()
    print("id = ", pat_ID.get())
    pp1 = pat_ID.get()
    print("id = ", pat_ID.get())
    pp2 = pat_name.get()
    pp3 = pat_sex.get()
    pp4 = pat_BG.get()
    pp5 = pat_dob.get()
    pp6 = pat_contact.get()
    pp7 = pat_contactalt.get()
    pp8 = pat_address.get()
    pp9 = pat_CT.get()
    pp10 = pat_email.get()
    if(len(str(pp1)) == 0 or len(str(pp9)) == 0):
        label_mode = customtkinter.CTkLabel(
            rootp, text_font="Verdana 12", text="Please fill all the required fields (*)", corner_radius=8,fg_color='red')
        label_mode.pack(pady=10)
        label_mode.after(2000, label_mode.pack_forget)
    elif(list(conn.execute("Select * from patient where patient_id=?", (pp1,))) != []):
        label_mode = customtkinter.CTkLabel(
            rootp, text_font="Verdana 12", text="Patient Already Registered!", corner_radius=8,fg_color='red')
        label_mode.pack(pady=10)
        label_mode.after(2000, label_mode.pack_forget)
    else:
        conn.execute('INSERT INTO PATIENT VALUES(?,?,?,?,?,?,?,?)',
                     (pp1, pp2, pp3, pp4, pp5, pp8, pp9, pp10))
        conn.execute('INSERT INTO CONTACT_NO VALUES (?,?,?)', (pp1, pp6, pp7))
        #customtkinter.CTkLabel(rootp,text="DETAILS INSERTED INTO DATABASE")
        label_mode = customtkinter.CTkLabel(
            rootp, text_font="Verdana 12", text="Details inserted into database", corner_radius=8,fg_color="green")
        label_mode.pack(pady=10)
        label_mode.after(2000, label_mode.pack_forget)
        conn.commit()
    clear_screen1()

def menucom(new_command):
    if(new_command == "View Records"):
        clear_screen1()
        showframe(rootV)
        c1 = conn.cursor()
        c1.execute("select * from contact_no")
        results = c1.fetchall()
        print("records : \n")
        for x in results:
            print(x)
    elif(new_command == "Exit"):
        rootp.quit()
    elif(new_command == "New"):
        PAT()
    elif(new_command == "About"):
        print("Made by Laeek Ahmed")


# PATIENT FORM
back = None
SEARCH = None
DELETE = None
UPDATE = None


def PAT():
    global pat_address, pat_BG, pat_contact, pat_contactalt, pat_CT, pat_dob, pat_email, pat_ID, pat_name, pat_sex
    global rootp, regform, id, name, dob, sex, email, ct, addr, c1, c2, bg, SUBMIT, menubar, filemenu, back, SEARCH, DELETE, UPDATE
    rootp = customtkinter.CTkFrame(root1)
    labely = customtkinter.CTkLabel(
        rootp, text_font="Verdana 12", text="Menu : ").place(x=-20, y=20)
    menubar = customtkinter.CTkOptionMenu(
        rootp, values=["View Records", "About", "Exit"], text_font="Verdana 12", command=menucom)  # value selected will be arg for the func()
    menubar.place(x=20, y=50)
    regform = customtkinter.CTkLabel(
        rootp, text="REGISTRATION FORM:-")
    pat_ID = customtkinter.CTkEntry(
        rootp, text_font="Verdana 12", width=170, placeholder_text="patient ID *")
    pat_name = customtkinter.CTkEntry(
        rootp, text_font="Verdana 12", width=170, placeholder_text="patient Name *")
    pat_sex = customtkinter.CTkEntry(
        rootp, text_font="Verdana 12", placeholder_text="gender")
    pat_dob = customtkinter.CTkEntry(
        rootp, text_font="Verdana 12", width=170, placeholder_text="DOB:(YYYY-MM-DD)")
    pat_BG = customtkinter.CTkEntry(
        rootp, text_font="Verdana 12", width=170, placeholder_text="Blood group")
    pat_contact = customtkinter.CTkEntry(
        rootp, text_font="Verdana 12", width=170, placeholder_text="Contact no.")
    pat_contactalt = customtkinter.CTkEntry(
        rootp, text_font="Verdana 12", width=170, placeholder_text="Alt contact no.")
    pat_email = customtkinter.CTkEntry(
        rootp, text_font="Verdana 12", width=170, placeholder_text="email ID")
    pat_CT = customtkinter.CTkEntry(
        rootp, text_font="Verdana 12", width=200, placeholder_text="consulting Doctor *")
    pat_address = customtkinter.CTkEntry(
        rootp, text_font="Verdana 12", width=170, placeholder_text="Address")
    back = customtkinter.CTkButton(
        rootp, text="<< BACK", text_font="Verdana 12", command=lambda: showframe(topframe))
    next = customtkinter.CTkButton(
        rootp, text="MORE OPTIONS >>  ", text_font="Verdana 12", command=P_display)
    # DELETE = customtkinter.CTkButton(
    #     rootp, text="  DELETE  ", text_font="Verdana 12", command=D_display)
    UPDATE = customtkinter.CTkButton(
        rootp, text="  UPDATE  ", text_font="Verdana 12", command=P_UPDATE)
    SUBMIT = customtkinter.CTkButton(
        rootp, text="  SUBMIT  ", text_font="Verdana 12", command=IN_PAT,)

    pat_ID.pack(pady=(20, 10))  # up & down padding
    pat_name.pack()
    pat_sex.pack(pady=10)
    pat_dob.pack()
    pat_BG.pack(pady=10)
    pat_contact.pack()
    pat_contactalt.pack(pady=10)
    pat_email.pack()
    pat_CT.pack(pady=10)
    pat_address.pack()
    SUBMIT.pack(pady=10, padx=10)
    back.place(x=10, y=300)
    next.pack()

    # mode chnage button;
    label_mode = customtkinter.CTkLabel(
        rootp, text_font="Verdana 12", text="Appearance Mode :")
    label_mode.place(x=10, y=90)
    optionmenu_1 = customtkinter.CTkOptionMenu(
        rootp, values=["Light", "Dark", "System"], text_font="Verdana 12", command=change_appearance_mode)
    optionmenu_1.place(x=20, y=120)

def clear_screen1():
    if 'text_area' in globals():
        text_area.pack_forget()
    backV.pack_forget()
    viewRecords()

def viewRecords():
    global text_area,backV
    vv = list(conn.execute("select * from patient"))
    if (len(vv) == 0):
        print("cp1")
        errorD = customtkinter.CTkLabel(
            rootV, text_font="Verdana 12", text="No Records found", corner_radius=8,fg_color="red")
        errorD.pack(pady=10)
        errorD.after(2000, errorD.pack_forget)
    else:
        c1 = conn.cursor()
        c1.execute("select * from patient")
        text_area = st.ScrolledText(rootV,
                                    width=60,
                                    height=20,
                                    bg='black',
                                    fg="white",
                                    font=("Verdana",
                                          10))

        text_area.pack(padx=10,pady=10)
        # Inserting Text which is read only
        text_area.insert(tkinter.INSERT,"Please open (View Records) page again from menu to refresh"+'\n'+'\n')
        for i in c1:
            # s1 = customtkinter.CTkLabel(
            #     rootAP, text_font="Verdana 12", text="patient id : "+str(i[0]))
            # s2 = customtkinter.CTkLabel(
            #     rootAP, text_font="Verdana 12", text="Appointment no. : ("+i[2])
            text_area.insert(tkinter.INSERT, "  patient id : " +
                             str(i[0])+" , "+" Name : "+i[1]+" , "+" Doctor : "+i[6]+'\n')
        # Making the text read only
        text_area.configure(state='disabled')
    backV = customtkinter.CTkButton(
    rootV, text="<< BACK", text_font="Verdana 12", command=lambda: showframe(rootp))
    backV.pack(pady=10)

# menu()
