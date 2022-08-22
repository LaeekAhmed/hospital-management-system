# Importing required modules

import tkinter as tk
import tkinter.scrolledtext as st
import customtkinter

# Creating tkinter window
win = customtkinter.CTk()
win.title("ScrolledText Widget")

# Title Label
customtkinter.CTkLabel(win,
                       text="ScrolledText Widget Example",
                       text_font=("Times New Roman", 15),
                       fg_color='green',).grid(column=0,
                                               row=0)

# Creating scrolled text area
# widget with Read only by
# disabling the state
t1 = customtkinter.CTkScrollbar(win, width=30,
                                height=8,)
t1.grid(column=10)
t1.set(1, 5)
text_area = st.ScrolledText(win,
                            width=30,
                            height=8,
                            bg='gray',
                            fg="white",
                            font=("Times New Roman",
                                  15))

text_area.grid(column=0, pady=10, padx=10)

# Inserting Text which is read only
text_area.insert(tk.INSERT,
                 """\
This is a scrolledtext widget to make tkinter text read only.
Hi
Geeks !!!
Geeks !!!
Geeks !!!
Geeks !!!
Geeks !!!
Geeks !!!
Geeks !!!
""")

# Making the text read only
text_area.configure(state='disabled')
win.mainloop()
