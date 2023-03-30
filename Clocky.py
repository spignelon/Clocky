import tkinter as tk
from tkinter import font
import time

def update_clock():
    #current_time = time.strftime("%H:%M:%S")
    current_time = time.strftime("%I:%M:%S %p")
    clock.config(text=current_time)
    clock.after(1000, update_clock)

root = tk.Tk()
root.overrideredirect(True)
root.geometry("110x40+0+0")
root.lift()
root.wm_attributes("-topmost", True)
root.config(bg='white')
root.attributes("-alpha", 0.8)

clock = tk.Label(root, font=("calibri", 15, "bold"), bg='white')
clock.pack(fill="both", expand=True)

# Add borders
clock.config(bd=2, relief="solid")

# Position the window at the top-right corner
root.geometry("+%d+%d" % (root.winfo_screenwidth()-110, 0))

update_clock()
root.mainloop()
