from tkinter import *
import tkinter as tk
from pwgenerate import Generate
from save_to_file import Save

FONT = ('Arial', 14)
save = Save()
g_password = Generate()

#functions---------------------------------------------------------------------
#popup
def ok_popup():
    website = website_input.get()
    email = emailuser_input.get()
    password = password_input.get()

    if len(website) > 3 and len(email) > 5 and len(password) > 7:
        win = tk.Toplevel()
        win.wm_title("Window")

        l = tk.Label(win, text=f"Are those information correct?\n"
                               f"website: {website}\n"
                               f"email: {email}\n"
                               f"password: {password}")
        l.grid(row=0, column=0)

        def save_and_close():
            save.to_file(website, email, password)
            win.destroy()  # Zamknięcie okna popup
            website_input.delete(0, tk.END)
            emailuser_input.delete(0, tk.END)
            password_input.delete(0, tk.END)
            website_input.focus()

        def wrong_info():
            win.destroy()

        b = tk.Button(win, text="Yes", command=save_and_close)
        b.grid(row=1, column=0)
        b = tk.Button(win, text="No", command=wrong_info)
        b.grid(row=2, column=0)


def generate():
    generated_password = g_password.password()
    password_text.set(generated_password)

def search():
    result = save.search(website_input.get())
    win = tk.Toplevel()
    win.wm_title("Window")

    l = tk.Label(win, text=f"{result}")
    l.grid(row=0, column=0)

    def close():
        win.destroy()

    b = tk.Button(win, text="Close", command=close)
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
generate_button = Button(text='Generate', bg='white', command=generate)
add_button = Button(text='Add', bg='white', command=ok_popup, activebackground='blue')
search_button = Button(text='Search', command=search)


#--Inputs
website_input = Entry(bg='lightgray')
emailuser_input = Entry(bg='lightgray')
password_text = tk.StringVar()
password_input = Entry(bg='lightgray', textvariable=password_text)


#-----UI-----------------------------------------
canvas.grid(row=0, column=1)

website_label.grid(row=1, column=0)
website_input.grid(row=1, column=1, sticky='nsew', padx=5, pady=5)
website_input.focus()

emailuser_label.grid(row=2, column=0)
emailuser_input.grid(row=2, column=1, columnspan=2, sticky='nsew', padx=5, pady=5)

password_label.grid(row=3, column=0)
password_input.grid(row=3, column=1, sticky='nsew', padx=5, pady=5)

generate_button.grid(row=3, column=2, sticky='nsew', padx=5, pady=5)
add_button.grid(row=4, column=1, columnspan=2, sticky='nsew', padx=5, pady=5)
search_button.grid(row=1, column=2, sticky='nsew', padx=5, pady=5)



window.mainloop()