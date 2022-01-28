from concurrent.futures.process import _WorkItem
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
TITLE = "Pomodoro"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20

# ---------------------------- VARIABLES ------------------------------- #

reps = 0
timer = None
marks = ""

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    global marks
    
    marks = ""
    reps = 0
    
    window.after_cancel(timer)
    
    title_label.config(text=f"{TITLE}\nTimer", fg=RED)
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text = f"{marks}")
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long\nBreak", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Short\nBreak", fg=RED)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer
    global marks
    
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        # Use dynamic typing to change the seconds to a string when less than 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:   
        start_timer()
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✅"
            check_marks.config(text=f"{marks}")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title(TITLE)
window.config(padx=20, pady=10, bg=YELLOW)

title_label = Label(text=f"{TITLE}\nTimer", fg=RED, bg=YELLOW, font=(FONT_NAME, 40, "bold"), padx=20, pady=20)
title_label.grid(row=0, column=1, sticky="N")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0, bd=0)

background = PhotoImage(file="./tomato.png")
canvas.create_image(100,112,image=background)

timer_text = canvas.create_text(100,132, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

start_button = Button(text="Start", command=start_timer, bg=YELLOW, highlightbackground=YELLOW)
start_button.grid(row=2, column=0, sticky="SE")

reset_button = Button(text="Reset", command=reset_timer, bg=YELLOW, highlightbackground=YELLOW)
reset_button.grid(row=2, column=2, sticky="SW")

check_marks = Label(bg=YELLOW, font=(FONT_NAME, 14, "bold"))
check_marks.grid(row=2, column=1, sticky="S")

canvas.grid(row=1, column=1)

window.mainloop()