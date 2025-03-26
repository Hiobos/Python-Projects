from tkinter import *
import time

colors = {'PINK': "#e2979c", 'RED': "#e7305b", 'GREEN': "#9bdeac", 'YELLOW': "#f7f5dd"}
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

#---------------functions
def countdown(t):
    t -= 1
    while t != -1:
        secs = 59
        while secs >= 0:
            timer = '{:02d}:{:02d}'.format(t, secs)
            canvas.create_text(100, 135, text=timer, font=(FONT_NAME, 32, 'bold'), fill='white')
            time.sleep(1)
            print(timer)
            secs -= 1
        t -= 1



window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=colors['YELLOW'])


#Canvas, image of tomato
canvas = Canvas(width=200, height=224, bg=colors['YELLOW'], highlightthickness=0)
tmt_image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tmt_image)
canvas.create_text(100, 135, text="00:00", font=(FONT_NAME, 32, 'bold'), fill='white')

#Timer Label
timer_label = Label(text="Timer", font=("Times New Roma", 40, 'bold'), bg=colors['YELLOW'], fg=colors['GREEN'])

#start button
button_start = Button(text="Start", command= lambda: countdown(5))
button_stop = Button(text="Stop")

#UI Placement
timer_label.grid(row=0, column=1)
canvas.grid(row=1, column=1)
button_start.grid(row=2, column=0)
button_stop.grid(row=2, column=2)

window.mainloop()