# Import the necessary modules
import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess

def chk_monitor():
    # if ddccontrol is not installed
    # sudo apt-get install ddccontrol
    cmd = "ddccontrol -p"

def set_value(event):
    val = scale.get()
    update_brightness(val)

def update_brightness(val):
    cmd = f"ddccontrol dev:/dev/i2c-6 -r 0x10 -w {val}"
    try:
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to set brightness.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
window = tk.Tk()
window.title("Brightness Control")

# Configure the window style
window.geometry("400x240")
window.config(bg="#F0F0F0")

# Create a label
label = tk.Label(
    window,
    text="Adjust Brightness",
    font=("Arial", 20),
    fg="#333333",
    bg="#F0F0F0"
)
label.pack(pady=20)

# Create a scale (slider) widget
scale = ttk.Scale(
    window,
    from_=0,
    to=100,
    orient=tk.HORIZONTAL,
    length=300,
)
scale.pack(padx=50, pady=20)

# Bind the set_value function to the Button-1 event of the scale widget
scale.bind("<Button-1>", set_value)

# Create a label for displaying credits
credits_label = tk.Label(
    window,
    text="Developed by: Akash Yadav, akashyadav23@gmail.com",
    font=("Arial", 8),
    fg="#666666",
    bg="#F0F0F0"
)
credits_label.pack(side=tk.BOTTOM, pady=5)

# Start the main event loop
window.mainloop()
