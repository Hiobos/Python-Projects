from functools import partial
from tkinter import *
import time

colors = {'PINK': "#e2979c", 'RED': "#e7305b", 'GREEN': "#9bdeac", 'YELLOW': "#f7f5dd"}
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer_running = None

#---------------functions
def text_update(timer):
    canvas.itemconfig(canvas_text, text=timer)

def countdown(t, status):
    timer_label['text'] = status
    global timer_running
    if t>= 0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer)
        text_update(timer)
        timer_running = window.after(1000, countdown, t-1)

def game_logic():
    countdown(25, "WORK")
    # countdown(5, "BREAK")
    # countdown(25, "WORK")
    # countdown(5, "BREAK")
    # countdown(25, "WORK")
    # countdown(5, "BREAK")
    # countdown(25, "WORK")
    # countdown(15, "BREAK") #longbreak



window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=colors['YELLOW'])


#Canvas, image of tomato
canvas = Canvas(width=200, height=224, bg=colors['YELLOW'], highlightthickness=0)
tmt_image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tmt_image)
canvas_text = canvas.create_text(100, 135, text="00:00", font=(FONT_NAME, 32, 'bold'), fill='white')

#Timer Label
timer_label = Label(text="Timer", font=("Times New Roma", 40, 'bold'), bg=colors['YELLOW'], fg=colors['GREEN'])

#checks label
checks_label = Label(text='✓', fg=colors['GREEN'], bg=colors['YELLOW'], font=("Times New Roma", 20, 'bold'))

#start button
button_start = Button(text="Start", command=game_logic)
button_stop = Button(text="Stop")

#UI Placement
timer_label.grid(row=0, column=1)
canvas.grid(row=1, column=1)
button_start.grid(row=2, column=0)
button_stop.grid(row=2, column=2)
checks_label.grid(row=3, column=1)

window.mainloop()