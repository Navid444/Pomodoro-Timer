from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    Title_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        Title_label.config(
            text="Break", bg=YELLOW, fg=RED, font=(FONT_NAME, 40, "bold")
        )
    elif reps % 2 == 0:
        count_down(short_break_sec)
        Title_label.config(
            text="Break", bg=YELLOW, fg=PINK, font=(FONT_NAME, 40, "bold")
        )
    else:
        count_down(work_sec)
        Title_label.config(
            text="Work", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold")
        )


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_minute = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{int(count_sec)}"

    if count_minute < 10:
        count_minute = f"0{int(count_minute)}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps / 2)):
            mark += "✔"
            check_mark.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pamodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white"
)
canvas.grid(column=1, row=1)


start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)


reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)


check_mark = Label(bg=YELLOW, fg=GREEN)
check_mark.grid(column=1, row=3)


Title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
Title_label.grid(column=1, row=0)


window.mainloop()