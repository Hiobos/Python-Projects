from tkinter import *


def button_clicked():
    x = int(input1.get())
    y = round(x * 1.60934)
    result['text'] = str(y)



window = Tk()
window.config(padx=30, pady=30)
#changing font globally
window.option_add("*font", "lucida 20 bold italic")

input1 = Entry()
input1.grid(row=0, column=1)

label1 = Label(text="Miles")
label1.grid(row=0, column=2)

label2 = Label(text="is equal to")
label2.grid(row=1, column=0)

result = Label(text='0')
result.grid(row=1, column=1)

label3 = Label(text="Km")
label3.grid(row=1, column=2)

button1 = Button(text="calculate", command=button_clicked)
button1.grid(row=2, column=1)





window.mainloop()