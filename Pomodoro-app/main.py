from functools import partial
from tkinter import *
import time

colors = {'PINK': "#e2979c", 'RED': "#e7305b", 'GREEN': "#9bdeac", 'YELLOW': "#f7f5dd"}
FONT_NAME = "Courier"
WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN = 25 * 60, 5 * 60, 20 * 60
timer_running = None
reps = 0
run = True
#---------------functions
def text_update(timer):
    canvas.itemconfig(canvas_text, text=timer)

def countdown(t):
    if run:
        global timer_running
        if t>= 0:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer)
            text_update(timer)
            timer_running = window.after(1000, countdown, t-1)
        else:
            start_timer()
            if reps % 2 == 0:
                checks_label['text'] += '✓'

def start_timer():
    global run
    global reps
    reps += 1
    run = True

    if reps == 8:
        timer_label['text'] = "BREAK"
        countdown(LONG_BREAK_MIN)
    elif reps % 2 == 0:
        timer_label['text'] = "BREAK"
        countdown(SHORT_BREAK_MIN)
    else:
        timer_label['text'] = "WORK"
        countdown(WORK_MIN)

def stop_app():
    global run
    global reps
    run = False
    reps = 0
    timer_label['text'] = "TIMER"
    canvas.itemconfig(canvas_text, text='00:00')


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
checks_label = Label(fg=colors['GREEN'], bg=colors['YELLOW'], font=("Times New Roma", 20, 'bold'))

#start button
button_start = Button(text="Start", command=start_timer)
button_stop = Button(text="Stop", command=stop_app)

#UI Placement
timer_label.grid(row=0, column=1)
canvas.grid(row=1, column=1)
button_start.grid(row=2, column=0)
button_stop.grid(row=2, column=2)
checks_label.grid(row=3, column=1)

window.mainloop()