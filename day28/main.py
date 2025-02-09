import math
import time
import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# WORK_MIN = 25
WORK_MIN = 0.10
# SHORT_BREAK_MIN = 5
SHORT_BREAK_MIN = 0.10
# LONG_BREAK_MIN = 20
LONG_BREAK_MIN = 0.15
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Long Break", fg=GREEN)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Short Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        timer_label.config(text="Work", fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    canvas.itemconfig(timer_text, text=f"{'%02d' % int(count/60)}:{'%02d' % (count % 60)}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            mark += "✔"
        checkmarks_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

timer_label = tkinter.Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

canvas = tkinter.Canvas(window, width=210, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(105,112, image=tomato_img)
timer_text = canvas.create_text(105, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

start_button = tkinter.Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

checkmarks_label = tkinter.Label(font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
checkmarks_label.grid(column=1, row=3)




















window.mainloop()