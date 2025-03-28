from tkinter import *
import tkinter as tk
import random

from click import command

from save_to_file import Save

FONT = ('Arial', 14)

save = Save()

#functions---------------------------------------------------------------------
#popup
def popup_bonus():
    win = tk.Toplevel()
    win.wm_title("Window")

    l = tk.Label(win, text="Are you sure that provided information is right?")
    l.grid(row=0, column=0)

    def save_and_close():
        save.to_file(website_input.get(), emailuser_input.get(), password_input.get())
        win.destroy()  # Zamknięcie okna popup

    b = tk.Button(win, text="Okay", command=save_and_close)
    b.grid(row=1, column=0)


#main window
window = Tk()
window.config(padx=30, pady=30, bg='white')
window.minsize(width=600, height=400)
canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
lock_img = PhotoImage(file='lock.png')
lock_img = lock_img.subsample(3, 3)
canvas.create_image(140, 90, image=lock_img)


#---website / emailuser / password labels
website_label = Label(text='Website: ', font=FONT, bg='white')
emailuser_label = Label(text='Email/Username: ', font=FONT, bg='white')
password_label = Label(text='Password: ', font=FONT, bg='white')
generate_button = Button(text='Generate', bg='white')
add_button = Button(text='Add', bg='white', command=popup_bonus)

#--Inputs
website_input = Entry()
emailuser_input = Entry()
password_input = Entry()

#-----UI-----------------------------------------
canvas.grid(row=0, column=1)

website_label.grid(row=1, column=0)
website_input.grid(row=1, column=1, columnspan=2, sticky='nsew', padx=5, pady=5)

emailuser_label.grid(row=2, column=0)
emailuser_input.grid(row=2, column=1, columnspan=2, sticky='nsew', padx=5, pady=5)

password_label.grid(row=3, column=0)
password_input.grid(row=3, column=1, sticky='nsew', padx=5, pady=5)

generate_button.grid(row=3, column=2, sticky='nsew', padx=5, pady=5)
add_button.grid(row=4, column=1, columnspan=2, sticky='nsew', padx=5, pady=5)


window.mainloop()