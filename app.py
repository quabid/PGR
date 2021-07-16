import tkinter as tk
import re
import os
from tkinter import ttk
from tkinter.constants import BOTTOM, CENTER, LEFT, RIGHT
from custom_modules import custom, error, success, warning

# Clear console


def cls(): return os.system('clear')


# Regex integers
number_pattern = re.compile('^[0-9]+$')

# Content manager
content = tk.Tk()
content.title("Converter")

# setting the windows size
content.geometry("400x74")

tf_entry_number_var = tk.StringVar()
entry_results_var = tk.StringVar()
lbl_converter_results = tk.Label(font=('calibre', 10, 'bold'))
lbl_converter_results.grid(column=1, columnspan=4, row=1, ipadx=5, padx=5)

# Main frame
frame = tk.Frame(content, borderwidth=1,
                 relief="ridge")
frame.grid(column=1, columnspan=12, row=1, padx=10, pady=10)

# User controls frame
controls_frame = tk.Frame(frame)
controls_frame.grid(columnspan=12, row=3, column=1, padx=10, pady=10)

# Labels
lbl_entry_number = tk.Label(
    controls_frame, bg="White", fg="Black", text="Enter Number", font=('calibre', 10, 'bold'))
lbl_entry_number.grid(column=1, row=1, ipadx=5)

# Text fields
tf_entry_number = tk.Entry(
    controls_frame, textvariable=tf_entry_number_var, width=15)
tf_entry_number.grid(column=2, row=1, columnspan=2, padx=5)
tf_entry_number_var.set("")


def btn_click_handler():
    text_input = tf_entry_number_var.get()

    try:
        if len(text_input) == 0:
            message = error("Must enter a valid integer")
            print("\n\t{}\n".format(message))
        elif (type(int(text_input)) != int) or not (number_pattern.search(text_input)):
            message = error("input error".capitalize())
            cause = custom("{} is not a valid integer".format(ve), 200, 77, 75)
            print("\n{}\n\tCause:\t{}\n", message, cause)
        else:
            print(text_input)
    except ValueError as ve:
        message = error("input error".title())
        cause = custom("{} is not a valid integer\n".format(ve), 200, 77, 75)
        print("\n{}\n\tCause:\t{}".format(message, cause))


# Buttons
btn_convert = tk.Button(
    controls_frame, text="convert".title(), width=10, command=btn_click_handler)
btn_convert.grid(column=4, ipadx=5)


def create_gui():
    # Layout controls
    frame.grid(column=0, row=6, columnspan=3)
    lbl_entry_number.grid(column=1, row=1, columnspan=2)
    tf_entry_number.grid(column=4, columnspan=2, row=1)
    btn_convert.grid(column=7, columnspan=1, row=1)

    content.columnconfigure(1, weight=3)
    frame.columnconfigure(2, weight=2)

    content.mainloop()


cls()
create_gui()
