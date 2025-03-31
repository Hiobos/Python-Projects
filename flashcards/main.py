from tkinter import *
import random

window = Tk()
FONT_LANGUAGE = ('Ariel', 30, 'italic')
FONT_WORD = ('Ariel', 60, 'bold')
BG_COLOR = '#B1DDC6'

window.config(bg=BG_COLOR)
canvas = Canvas(width=800, height=526, bg=BG_COLOR, highlightthickness=0)

#-----------FUNCTIONS---------------
def new_word():
    with open('data/french_words.csv', 'r') as data:
        dict = [i.strip('\n') for i in data]
        dict = [i.split(',') for i in dict]
        #print(dict[0][0]) to daje samo 'French'
        canvas.itemconfig(language, text=dict[0][0])

#------------IMAGES-----------------
flashcard_front = PhotoImage(file='images/card_front.png', width=800, height=526)
flashcard_back = PhotoImage(file='images/card_back.png')
right_image = PhotoImage(file='images/right.png')
wrong_image = PhotoImage(file='images/wrong.png')

#------------BUTTONS-----------------
front_flash = Button(image=flashcard_front)
back_flash = Button(image=flashcard_back)
right = Button(image=right_image, highlightthickness=0, command=new_word)
wrong = Button(image=wrong_image, highlightthickness=0)




#---------------UI-------------------
canvas.create_image(400, 263, image=flashcard_front)
language = canvas.create_text(400, 120, fill='black', text='Title', font=FONT_LANGUAGE)
word = canvas.create_text(400, 250, fill='black', text='word', font=FONT_WORD)
canvas.grid(row=0, column=0, columnspan=2, padx=20, pady=20)
wrong.grid(row=1, column=0)
right.grid(row=1, column=1)


window.mainloop()