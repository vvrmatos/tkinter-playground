#!/usr/bin/env python

from tkinter import *


root = Tk()
root.title("Hello Tkinter")


# Non selectable text
label = Label(root, text="Hello, Tkinter!", font=("Georgia", 16))
label.pack(padx=20, pady=20)


# Selectable text
text_widget = Text(
    root, height=2, width=30, bg=root.cget("bg"), bd=0, font=("Georgia", 16)
)
text_widget.pack(padx=40, pady=40)
text_widget.insert(END, "Hello, Tkinter!")
text_widget.config(state=DISABLED)


root.mainloop()
