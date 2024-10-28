from tkinter import *
import math

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
marks = ""

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg="#f7f5dd")


def reset():
    global marks
    global reps
    window.after_cancel(timer)
    lab.config(text="Timer")
    can.itemconfig(text, text="00:00")
    marks = ""
    reps = 0


def c(t):
    c_m = math.floor(t/60)
    c_s = math.floor(t % 60)
    if c_s < 10:
        c_s = f"0{c_s}"
    can.itemconfig(text, text=f"{c_m}:{c_s}")
    if t >= 1:
        global timer
        timer = window.after(1000, c, t-1)
    else:
        ch()
        global marks
        ws = math.floor(reps/2)
        for _ in range(ws):
            marks += "✔️"
        but2.config(text=marks)


def ch():
    wm = WORK_MIN*60
    sb = SHORT_BREAK_MIN*60
    lb = LONG_BREAK_MIN*60
    global reps
    reps += 1

    if reps % 8 == 0:
        lab.config(text="Long Break", fg="#e7305b")
        c(lb)
    elif reps % 2 == 0:
        lab.config(text="Short Break", fg="#e7305b")
        c(sb)
    else:
        lab.config(text="Work", fg="#e7305b")
        c(wm)


can = Canvas(width=200, height=224, bg="#f7f5dd", highlightthickness=0)
i = PhotoImage(file="tomato.png")
can.create_image(100, 112, image=i)
text = can.create_text(103, 130, text="00:00", fill="white", font=("Courier", 35, "bold"))
can.grid(row=2, column=2)

lab = Label(text="Timer", fg="#9bdeac", bg="#f7f5dd", font=("#9bdeac", 20, 'bold'))
lab.grid(row=1, column=2)

but = Button(text="Start", command=ch)
but.grid(row=3, column=1)

but1 = Button(text="Reset", command=reset)
but1.grid(row=3, column=4)

but2 = Label(fg="#9bdeac", bg="#f7f5dd", font=("#9bdeac", 20))
but2.grid(row=4, column=2)

window.mainloop()