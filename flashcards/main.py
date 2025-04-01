from tkinter import *
import random
import pandas as pd

window = Tk()
FONT_LANGUAGE = ('Ariel', 30, 'italic')
FONT_WORD = ('Ariel', 60, 'bold')
BG_COLOR = '#B1DDC6'
wrong_words = []
random_pick = ''
should_remove = False

#initial setup----------------------
window.config(bg=BG_COLOR)
canvas = Canvas(width=800, height=526, bg=BG_COLOR, highlightthickness=0)

#-----------FUNCTIONS---------------
def open_file(): #checks if file with wrong words exists
    global should_remove
    try:
        data_df = pd.read_csv('data/wrong_words.csv')
        if data_df.empty or data_df.shape[1] == 0:
            raise ValueError
        should_remove = True
    except (FileNotFoundError, ValueError, pd.errors.EmptyDataError):
        data_df = pd.read_csv('data/words.csv')
        should_remove = False
    return data_df


def buttons_state(state):#DISABLED/NORMAL
    right.config(state=state)
    wrong.config(state=state)


def new_word(state):
    global random_pick, should_remove
    data_df = open_file()

    buttons_state(DISABLED)

    if data_df.empty:
        print("File is empty, cannot pick random word")
        return

    try:
        if state == 'wrong' and random_pick != '':
            to_add = [data_df.iloc[random_pick]['French'], data_df.iloc[random_pick]['English']]
            if to_add not in wrong_words:
                wrong_words.append(to_add)
        elif state == 'right' and random_pick != '':
            if should_remove:
                to_remove = [data_df.iloc[random_pick]['French'], data_df.iloc[random_pick]['English']]
                if to_remove in wrong_words:
                    wrong_words.remove(to_remove)

                if len(wrong_words) == 0:
                    import os
                    if os.path.exists('data/wrong_words.csv'):
                        os.remove('data/wrong_words.csv')
                    should_remove = False

    except IndexError:
        random_pick = random.randint(0, len(data_df) - 1) if len(data_df) > 0 else None

    #picking random word
    data_df = open_file()
    random_pick = random.randint(0, len(data_df) - 1)
    foreign_word = data_df['French'][random_pick]
    english_word = data_df['English'][random_pick]

    #updating canvas with english words
    update_to_foreign(foreign_word)
    window.after(3000, lambda: [update_to_english(english_word), buttons_state(NORMAL)])

    if len(wrong_words) > 0:
        wrong_df = pd.DataFrame(wrong_words, columns=['French', 'English'])
        wrong_df.to_csv('data/wrong_words.csv', index=False, header=True)


#updating canvas with foreign words after 3 seconds
def update_to_foreign(foreign_word):
    canvas.itemconfig(flashcard, image=flashcard_front)
    canvas.itemconfig(word, text=foreign_word, fill='black')
    canvas.itemconfig(language, text='French', fill='black')


def update_to_english(english_word):
    canvas.itemconfig(flashcard, image=flashcard_back)
    canvas.itemconfig(word, text=english_word, fill='white')
    canvas.itemconfig(language, text='English', fill='white')

#------------IMAGES-----------------
flashcard_front = PhotoImage(file='images/card_front.png', width=800, height=526)
flashcard_back = PhotoImage(file='images/card_back.png')
right_image = PhotoImage(file='images/right.png')
wrong_image = PhotoImage(file='images/wrong.png')

#------------BUTTONS-----------------
front_flash = Button(image=flashcard_front)
back_flash = Button(image=flashcard_back)
right = Button(image=right_image, highlightthickness=0, command=lambda: new_word('right'))
wrong = Button(image=wrong_image, highlightthickness=0, command=lambda: new_word('wrong'))

#---------------UI-------------------
flashcard = canvas.create_image(400, 263, image=flashcard_front)
language = canvas.create_text(400, 120, fill='black', text='Title', font=FONT_LANGUAGE)
word = canvas.create_text(400, 250, fill='black', text='word', font=FONT_WORD)
canvas.grid(row=0, column=0, columnspan=2, padx=20, pady=20)
wrong.grid(row=1, column=0)
right.grid(row=1, column=1)

#start
new_word('none')

window.mainloop()