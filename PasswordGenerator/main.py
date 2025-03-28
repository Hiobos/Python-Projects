from tkinter import *
import random

FONT = ('Arial', 14)

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
add_button = Button(text='Add', bg='white')

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