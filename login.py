from tkinter import *
from main import menu
import customtkinter

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("dark")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")


def change_appearance_mode(new_appearance_mode):
    customtkinter.set_appearance_mode(new_appearance_mode)

# root=login page
# root1=menu
# rootp=patient form


# variables
root = None
userbox = None
passbox = None
topframe = None
bottomframe = None
frame3 = None
login = None
flag = 0
# command for login button


def GET():
    global userbox, passbox, error, flag
    flag = 0
    S1 = userbox.get()  # extract input from , userbox = tkinter.Entry(topframe)
    S2 = passbox.get()
    if(S1 == 'admin' and S2 == '2020'):
        menu()
    elif(S1 == 'krishna' and S2 == '2020'):
        menu()
    elif(S1 == 'laeek' and S2 == '2020'):
        root.destroy()
        menu()
        root.destroy()
    elif(S1 == 'vishesh' and S2 == '2020'):
        menu()
    else:
        error = customtkinter.CTkLabel(
            topframe, text="Wrong Id / Password \n TRY AGAIN",text_font="Verdana 12")
        error.pack()

# LOGIN PAGE WINDOW


def showframe(frame):
    frame.tkraise()


def entryfunc():
    global userbox, passbox, login, topframe, w2frame, image_1, root
    root = customtkinter.CTk()
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    root.geometry("400x400")
    topframe = customtkinter.CTkFrame(root)
    topframe.pack(padx=60, pady=60)

    # frame1;
    heading = customtkinter.CTkLabel(
        topframe, text="WELCOME TO LVK HOSPITAL ", relief='sunken')
    heading.place()
    userbox = customtkinter.CTkEntry(topframe, text_font="Verdana 12",placeholder_text="Name")
    userbox.pack(pady=12, padx=50)
    passbox = customtkinter.CTkEntry(
        topframe, show="*", text_font="Verdana 12",placeholder_text="password")
    passbox.pack(padx=50)
    login = customtkinter.CTkButton(topframe, text="LOGIN",text_font="Verdana 12", command=GET)
    login.pack(pady=12,padx=50)
    # logo;
    # root.iconbitmap(
    #     "C:/Users/User/Downloads/hospital_icon.ico")  # hospital logo!

    # mode change button;
    label_mode = customtkinter.CTkLabel(root, text="Appearance Mode:",text_font="Verdana 12")
    label_mode.pack()

    optionmenu_1 = customtkinter.CTkOptionMenu(
        root, values=["Light", "Dark", "System"],text_font="Verdana 12", command=change_appearance_mode)
    optionmenu_1.pack(pady=10)
    root.title("LOGIN PAGE")
    #img1 = ImageTk.PhotoImage(Image.open('wallpaper1.jfif'))
    #labelx = customtkinter.CTkLabel(image=img1).grid()
    root.mainloop()  # keeps the window open (terminates on clicking X)


entryfunc()
