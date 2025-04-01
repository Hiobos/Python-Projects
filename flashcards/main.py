from tkinter import *
import random
import pandas as pd

window = Tk()
FONT_LANGUAGE = ('Ariel', 30, 'italic')
FONT_WORD = ('Ariel', 60, 'bold')
BG_COLOR = '#B1DDC6'

#initial setup
window.config(bg=BG_COLOR)
canvas = Canvas(width=800, height=526, bg=BG_COLOR, highlightthickness=0)

#-----------FUNCTIONS---------------
def new_word():
    data_df = pd.read_csv('data/french_words.csv')

    #picking random word
    random_pick = random.randrange(1, len(data_df))
    foreign_word = data_df['French'][random_pick]
    english_word = data_df['English'][random_pick]

    #updating canvas with english words
    update_to_english(english_word)
    window.after(3000, lambda: update_to_foreign(foreign_word))


#updating canvas with foreign words after 3 seconds
def update_to_foreign(foreign_word):
    canvas.itemconfig(flashcard, image=flashcard_back)
    canvas.itemconfig(word, text=foreign_word, fill='white')
    canvas.itemconfig(language, text='French', fill='white')

def update_to_english(english_word):
    canvas.itemconfig(flashcard, image=flashcard_front)
    canvas.itemconfig(word, text=english_word, fill='black')
    canvas.itemconfig(language, text='English', fill='black')


#------------IMAGES-----------------
flashcard_front = PhotoImage(file='images/card_front.png', width=800, height=526)
flashcard_back = PhotoImage(file='images/card_back.png')
right_image = PhotoImage(file='images/right.png')
wrong_image = PhotoImage(file='images/wrong.png')

#------------BUTTONS-----------------
front_flash = Button(image=flashcard_front)
back_flash = Button(image=flashcard_back)
right = Button(image=right_image, highlightthickness=0, command=new_word)
wrong = Button(image=wrong_image, highlightthickness=0, command=new_word)

#---------------UI-------------------
flashcard = canvas.create_image(400, 263, image=flashcard_front)
language = canvas.create_text(400, 120, fill='black', text='Title', font=FONT_LANGUAGE)
word = canvas.create_text(400, 250, fill='black', text='word', font=FONT_WORD)
canvas.grid(row=0, column=0, columnspan=2, padx=20, pady=20)
wrong.grid(row=1, column=0)
right.grid(row=1, column=1)

#start
new_word()

window.mainloop()