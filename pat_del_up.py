from logging import root
import tkinter
import sqlite3
from turtle import width
import customtkinter
import tkinter.messagebox
import tkinter.scrolledtext as st

conn = sqlite3.connect("MDBA.db")
# variables
rootU = None
rootD = None
rootS = None
head = None
inp_s = None
searchB = None
disp_frame = None
# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("Dark")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")


def change_appearance_mode(new_appearance_mode):
    customtkinter.set_appearance_mode(new_appearance_mode)

# display/search button


def Search_button():
    global inp_s, entry, errorS, t, i, q, dis1, dis2, dis3, dis4, dis5, dis6, dis7, dis8, dis9, dis10
    global l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, close, text_area
    clear_screen()
    c1 = conn.cursor()  # cursor used to interact with db (do operations like create,modify etc)
    inp_s = entry.get()
    p = list(c1.execute('select * from PATIENT where PATIENT_ID=?', (inp_s,)))
    if (len(p) == 0):
        errorS = customtkinter.CTkLabel(
            disp_frame, text_font="Verdana 12", text="Patient record not found", corner_radius=8,fg_color="red")
        errorS.pack(pady=10)
        errorS.after(2000, errorS.pack_forget)
    else:
        t = c1.execute(
            'SELECT * FROM PATIENT NATURAL JOIN CONTACT_NO where PATIENT_ID=?', (inp_s,))
        text_area = st.ScrolledText(disp_frame,
                                    width=60,
                                    height=10,
                                    bg='black',
                                    fg="white",
                                    font=("Verdana",
                                          12))
        text_area.pack(padx=10,pady=15)
        names = list(map(lambda x: x[0], t.description))
        L1=[]
        k=0
        for j in t: 
            L1=j
        for i in names:
                text_area.insert(tkinter.INSERT,str(i)+" : "+str(L1[k])+'\n')
                k+=1
        # Making the text read only
        text_area.configure(state='disabled')
        conn.commit()


def eXO():
    rootS.destroy()

# search window


def showframe(frame):
    frame.tkraise()


def P_display():
    global rootS, head, inp_s, entry, searchB, disp_frame
    rootS = customtkinter.CTk()
    rootS.title("SEARCH WINDOW")
    rootS.geometry("580x600")
    rootS.rowconfigure(0, weight=1)
    rootS.columnconfigure(0, weight=1)
    disp_frame = customtkinter.CTkFrame(rootS)
    # D_display()
    P_UPDATE()
    for frame in (disp_frame, rootU):
        frame.grid(row=0, column=0, padx=30, pady=30, sticky='nsew')
    showframe(disp_frame)
    head = customtkinter.CTkLabel(
        disp_frame, text_font="Verdana 12", text="Enter patient id to search:")
    entry = customtkinter.CTkEntry(disp_frame, text_font="Verdana 12")
    searchB = customtkinter.CTkButton(
        disp_frame, text_font="Verdana 12", text='Search', command=Search_button)

    head.pack()
    entry.pack(pady=10)
    searchB.pack()
    # other options;
    opt = customtkinter.CTkLabel(
        disp_frame, text_font="Verdana 12", text="Other Options : ").pack(pady=7)
    DELETE = customtkinter.CTkButton(
        disp_frame, text_font="Verdana 12", text="  DELETE  ",  command=Delete_button).pack(pady=5)
    UPD = customtkinter.CTkButton(
        disp_frame, text_font="Verdana 12", text="UPDATE",  command=lambda: showframe(rootU)).pack()
    # Modes: "System" (standard), "Dark", "Light"
    customtkinter.set_appearance_mode("Dark")
    # Themes: "blue" (standard), "green", "dark-blue"
    customtkinter.set_default_color_theme("blue")
    rootS.mainloop()


inp_d = None
entry1 = None
errorD = None
disd1 = None

# DELTE BUTTONcleatext_


def clear_screen():
    if 'text_area' in globals():
        text_area.pack_forget()
    # l1.pack_forget()
    # dis1.place_forget()
    # l2.pack_forget()
    # dis2.place_forget()
    # l3.pack_forget()
    # dis3.place_forget()
    # l4.pack_forget()
    # dis4.place_forget()
    # l5.pack_forget()
    # dis5.place_forget()
    # l6.pack_forget()
    # dis6.place_forget()
    # l7.pack_forget()
    # dis7.place_forget()
    # l8.pack_forget()
    # dis8.place_forget()
    # l9.pack_forget()
    # dis9.place_forget()
    # l10.pack_forget()
    # dis10.place_forget()
    # close.place_forget()


def Delete_button():
    global inp_d, entry1, errorD, disd1
    clear_screen()
    c1 = conn.cursor()
    inp_d = entry.get()
    p = list(conn.execute("select * from PATIENT where PATIENT_ID=?", (inp_d,)))
    if (len(p) == 0):
        errorD = customtkinter.CTkLabel(
            disp_frame, text_font="Verdana 12", text="Patient record not found", corner_radius=8,fg_color="red")
        errorD.pack(pady=10)
        errorD.after(2000, errorD.pack_forget)
    else:
        conn.execute('DELETE FROM PATIENT where PATIENT_ID=?', (inp_d,))
        conn.execute('DELETE FROM CONTACT_NO where PATIENT_ID=?', (inp_d,))
        disd1 = customtkinter.CTkLabel(
            disp_frame, text_font="Verdana 12", text="Patient record deleted", corner_radius=8,fg_color="green")
        disd1.pack(pady=10)
        disd1.after(2000, disd1.pack_forget)
        conn.commit()


# # DELETE SCREEN
# def D_display():
#     global rootD, headD, inp_d, entry1, DeleteB
#     rootD = customtkinter.CTkFrame(rootS)
#     headD = customtkinter.CTkLabel(
#         rootD, text_font="Verdana 12", text="ENTER PATIENT ID TO DELETE")
#     entry1 = customtkinter.CTkEntry(rootD, text_font="Verdana 12")
#     DeleteB = customtkinter.CTkButton(
#         rootD, text_font="Verdana 12", text="DELETE", command=Delete_button)
#     headD.pack()
#     entry1.pack(pady=10)
#     DeleteB.pack()
#     back1 = customtkinter.CTkButton(
#         rootD, text_font="Verdana 12", text="  back  ",  command=lambda: showframe(disp_frame)).pack(pady=10)

    # Modes: "System" (standard), "Dark", "Light"
    customtkinter.set_appearance_mode("Dark")
    # Themes: "blue" (standard), "green", "dark-blue"
    customtkinter.set_default_color_theme("blue")

# variables for update


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


def up1():
    global u1, u2, u3, u4, u5, u6, u7, u8, u9, u10, ue1, conn
    clear_screen()
    conn.cursor()
    u1 = pat_ID.get()
    u2 = pat_name.get()
    u3 = pat_sex.get()
    u4 = pat_dob.get()
    u5 = pat_BG.get()
    u6 = pat_contact.get()
    u7 = pat_contactalt.get()
    u8 = pat_email.get()
    u9 = pat_CT.get()
    u10 = pat_address.get()
    conn = sqlite3.connect("MDBA.db")
    p = list(conn.execute("Select * from PATIENT where PATIENT_ID=?", (u1,)))
    if len(p) != 0:
        conn.execute('UPDATE PATIENT SET NAME=?,SEX=?,DOB=?,BLOOD_GROUP=?,ADDRESS=?,CONSULT_TEAM=?,EMAIL=? where PATIENT_ID=?',
                     (u2, u3, u4, u5, u10, u9, u8, u1,))
        conn.execute(
            'UPDATE CONTACT_NO set CONTACTNO=?,ALT_CONTACT=? WHERE PATIENT_ID=?', (u6, u7, u1,))
        label_mode = customtkinter.CTkLabel(
            rootU, text_font="Verdana 12", text="DETAILS INSERTED INTO DATABASE", corner_radius=8,fg_color="green")
        label_mode.pack(pady=10)
        label_mode.after(2000, label_mode.pack_forget)
        conn.commit()

    else:
        label_mode = customtkinter.CTkLabel(
            rootU, text_font="Verdana 12", text="Patient not registered", corner_radius=8,fg_color="red")
        label_mode.pack(pady=10)
        label_mode.after(2000, label_mode.pack_forget)


labelu = None
bu1 = None


def EXITT():
    rootU.destroy()

##-----PATIENT UPDATE SCREEN -----##


def P_UPDATE():
    global pat_address, pat_BG, pat_contact, pat_contactalt, pat_CT, pat_dob, pat_email, pat_ID, pat_name, pat_sex
    global rootU, regform, id, name, dob, sex, email, ct, addr, c1, c2, bg, SUBMIT, menubar, filemenu, p1f, p2f, HEAD
    rootU = customtkinter.CTkFrame(rootS)
    HEAD = customtkinter.CTkLabel(
        rootU, text_font="Verdana 12", text="ENTER NEW DETAILS TO UPDATE :").pack()
    pat_ID = customtkinter.CTkEntry(
        rootU, text_font="Verdana 12", placeholder_text="patient ID")
    pat_name = customtkinter.CTkEntry(
        rootU, text_font="Verdana 12", placeholder_text="patient Name")
    pat_sex = customtkinter.CTkEntry(
        rootU, text_font="Verdana 12", placeholder_text="gender")
    pat_dob = customtkinter.CTkEntry(
        rootU, text_font="Verdana 12", placeholder_text="DOB:(YYYY-MM-DD)")
    pat_BG = customtkinter.CTkEntry(
        rootU, text_font="Verdana 12", placeholder_text="Blood group")
    pat_contact = customtkinter.CTkEntry(
        rootU, text_font="Verdana 12", placeholder_text="Contact no.")
    pat_contactalt = customtkinter.CTkEntry(
        rootU, text_font="Verdana 12", placeholder_text="Alt contact no.")
    pat_email = customtkinter.CTkEntry(
        rootU, text_font="Verdana 12", placeholder_text="email ID")
    pat_CT = customtkinter.CTkEntry(
        rootU, text_font="Verdana 12", placeholder_text="consulting Doc/team")
    pat_address = customtkinter.CTkEntry(
        rootU, text_font="Verdana 12", placeholder_text="Address")
    SUBMIT = customtkinter.CTkButton(
        rootU, text_font="Verdana 12", text="  Submit  ", command=up1,)

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
    SUBMIT.pack(pady=10)
    back2 = customtkinter.CTkButton(
        rootU, text_font="Verdana 12", text="  back  ",  command=lambda: showframe(disp_frame)).pack()

    # Modes: "System" (standard), "Dark", "Light"
    customtkinter.set_appearance_mode("dark")
    # Themes: "blue" (standard), "green", "dark-blue"
    customtkinter.set_default_color_theme("blue")


#P_display()
