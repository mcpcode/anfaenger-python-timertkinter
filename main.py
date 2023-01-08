

import tkinter as tk
import math
#--- Variables --- #
FONT = "Courier"
timer_minutes = 4
total_seconds = timer_minutes * 60
timer_active = False
timer_paused = False
remaining_seconds = None
remaining_minutes = None
seconds_of_minute = None
#--- End Variables --- #


def my_timer(total_seconds):
    global seconds_of_minute
    global remaining_minutes
    if timer_active:
        seconds_of_minute = total_seconds % 60
        if seconds_of_minute < 10:
            seconds_of_minute = f'0{seconds_of_minute}'
        remaining_minutes = math.floor(total_seconds / 60)
        if remaining_minutes < 10:
            remaining_minutes = f'0{remaining_minutes}'
        canvas.itemconfig(timer_text, text=f'{remaining_minutes}:{seconds_of_minute}')
        window.after(1000, my_timer, total_seconds -1)
    else:
        return

def start_timer():
    global timer_active
    if not timer_active:
        timer_active = True
        my_timer(total_seconds)
    else:
        return

def reset_timer():
    global timer_active
    timer_active = False
    canvas.itemconfig(timer_text, text="00:00")

def pause_timer():
    global timer_active
    global timer_paused
    if not timer_paused:
        timer_paused = True
        timer_active = False
        pause_button.configure(text="Timer ist pausiert")
        canvas.config(bg="red")
        global remaining_seconds
        remaining_seconds = remaining_minutes * 60 + seconds_of_minute

    else:
        # Timer ist pausiert
        pause_button.configure(text="Pause")
        timer_paused = False
        timer_active = True
        my_timer(remaining_seconds)


# --- GUI ---- #

window = tk.Tk()
window.config(padx=10, pady=10)
window.title("Timer")
canvas = tk.Canvas(width=200, height=200, bg="#181031")
timer_text = canvas.create_text(100,100,text="00:00", fill="white", font=(FONT, 40))
canvas.grid(column=1, row=0)

start_button = tk.Button(text="Start", bg="#181031", fg="#ffffff", command=start_timer)
start_button.grid(column=0, row=1)

reset_button = tk.Button(text="Stop/Reset", bg="#181031", fg="#ffffff", command=reset_timer)
reset_button.grid(column=1, row=1)

pause_button = tk.Button(text="Pause", bg="#181031", fg="#ffffff", command=pause_timer)
pause_button.grid(column=2, row=1)

window.mainloop()

