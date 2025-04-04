import tkinter
from tkinter import *
from utils import Kanye
kanye = Kanye()

class Graphics:
    def __init__(self):
        window = Tk()
        window.minsize(400, 500)
        quote = tkinter.StringVar(window, kanye.get_quote())

        quote_label = Label(textvariable=quote)
        quote_label.grid(row=0, column=0)

        def start(quote):
            quote = tkinter.StringVar(window, kanye.get_quote())
            quote_label.config(textvariable=quote)

        btn1 = Button(text='new quote', command=lambda: start(quote))
        btn1.grid(row=1, column=0)

        window.mainloop()





