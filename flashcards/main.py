from tkinter import *
import random
import time

window = Tk()
FONT_LANGUAGE = ('Ariel', 30, 'italic')
FONT_WORD = ('Ariel', 60, 'bold')
BG_COLOR = '#B1DDC6'

window.config(bg=BG_COLOR)
canvas = Canvas(width=800, height=526, bg=BG_COLOR, highlightthickness=0)

#-----------FUNCTIONS---------------
def new_word():
    with open('data/french_words.csv', 'r') as data:
        dict1 = [i.strip('\n') for i in data]
        dict2 = [i.split(',') for i in dict1]
        #print(dict[0][0]) to daje samo 'French'

        #picking random word
        random_foreign_word = dict2[random.randrange(1, len(dict1))]
        foreign_word = random_foreign_word[0]
        english_word = random_foreign_word[1]

        #updating canvas with english words
        update_to_english(english_word, dict2)
        window.after(3000, lambda: update_to_foreign(foreign_word, dict2))


#updating canvas with foreign words after 3 seconds
def update_to_foreign(foreign_word, dict2):
    canvas.itemconfig(flashcard, image=flashcard_back)
    canvas.itemconfig(word, text=foreign_word)
    canvas.itemconfig(language, text=dict2[0][0])

def update_to_english(english_word, dict2):
    canvas.itemconfig(flashcard, image=flashcard_front)
    canvas.itemconfig(word, text=english_word)
    canvas.itemconfig(language, text=dict2[0][1])


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