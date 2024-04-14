# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 19:57:56 2024

@author: Thasneem
"""

from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os
from tkinter import messagebox

root = Tk()
root.minsize(600, 600)
root.maxsize(1700, 1200)

open_img = ImageTk.PhotoImage(Image.open("open.png"))
save_img = ImageTk.PhotoImage(Image.open("save.png"))
run_img = ImageTk.PhotoImage(Image.open("run.png"))

label_file_name = Label(root, text = "File Name :", bg = "white")
label_file_name.place(relx = 0.40, rely = 0.05, anchor = CENTER)

input_file_name = Entry(root)
input_file_name.place(relx = 0.57, rely = 0.05, anchor = CENTER)

my_text = Text(root, height = 33, width = 74, bg = "gray", fg = "white")
my_text.place(relx = 0.5, rely = 0.55, anchor = CENTER)

open_btn = Button(root, image = open_img, text = "Open File")
open_btn.place(relx = 0.05, rely = 0.05, anchor = CENTER)

save_btn = Button(root, image = save_img, text = "Save File")
save_btn.place(relx = 0.12, rely = 0.05, anchor = CENTER)

run_btn = Button(root, image = run_img, text = "Run File")
run_btn.place(relx = 0.22, rely = 0.05, anchor = CENTER)

root.mainloop()