import tkinter as tk
import re
import os
from tkinter import Spinbox, ttk
from tkinter.constants import BOTTOM, CENTER, LEFT, RIGHT
from custom_modules import custom, error, success, warning

# Clear console


def cls(): return os.system('clear')


# Regex integers
integer_pattern = re.compile('^[0-9]+$')
float_pattern = re.compile('^[0-9]+(\.[0-9]+){1}$')


# Number converters
def hex(arg, is_float=False):
    return arg


def octal(arg, is_float=False):
    return arg


def binary(arg, is_float=False):
    return arg


# Spinbox
combobox_list = ("Hexadecimal", "Octal", "Binary")
combobox_switch = {
    "Hexadecimal": lambda arg: hex(arg),
    "Octal": lambda arg: octal(arg),
    "Binary": lambda arg: binary(arg)
}

""" The root window
    configure default size
"""
content = tk.Tk()
content.title("Converter")
content.geometry("500x74")
content.geometry("+500+174")
content.minsize(500, 74)
content.attributes("-alpha", 0.5)

# User input component
tf_entry_number_var = tk.StringVar()
entry_results_var = tk.StringVar()

""" The main content pane
"""
frame = tk.Frame(content, borderwidth=1,
                 relief="ridge")
frame.grid(column=1, columnspan=12, row=1, padx=10, pady=10)

# Controls panel
controls_frame = tk.Frame(frame)
controls_frame.grid(columnspan=12, row=3, column=1, padx=10, pady=10)

# Text fields
tf_entry_number = tk.Entry(
    controls_frame, textvariable=tf_entry_number_var, width=15)
tf_entry_number.grid(column=2, row=1, columnspan=2, padx=5)
tf_entry_number_var.set("")

""" Component handlers"""


def btn_click_handler():
    text_input = tf_entry_number_var.get()
    selected_item = combo_box.get()
    is_float = False

    try:
        if len(text_input) == 0:
            message = error("Must enter a valid integer")
            print("\n\t{}\n".format(message))
        elif not (integer_pattern.search(text_input)) and not (float_pattern.search(text_input)):
            print("\t{} is an invalid number\n".format(warning(text_input)))
        else:
            if float_pattern.search(text_input):
                is_float = True
            else:
                is_float = False

            print("\n\tNumber: {}".format(success(text_input)))
            print("\tIs {} a floating point number? {}".format(
                success(text_input), is_float))
            print("\tConverting {} to {}\n".format(success(text_input), selected_item))

    except ValueError as ve:
        message = error("input error".title())
        cause = custom("{} is not a valid integer\n".format(ve), 200, 77, 75)
        print("\n{}\n\tCause:\t{}".format(message, cause))


def combobox_handler():
    selected_item = combo_box.get()
    print("\n\tConvert number to {}\n".format(selected_item))


# Buttons
btn_convert = tk.Button(
    controls_frame, text="convert".title(), width=10, command=btn_click_handler)
btn_convert.grid(column=4, ipadx=5)


# Spinbox
combo_box = tk.Spinbox(controls_frame, values=combobox_list, bg="White",
                       fg="Black", state="readonly", command=combobox_handler, text="Enter Number", font=('calibre', 10, 'bold'))
combo_box.grid(column=1, row=1, ipadx=5)


def configure_and_create_gui():
    # Configure layouts
    frame.grid(column=0, row=6, columnspan=3)
    tf_entry_number.grid(column=4, columnspan=2, row=1)
    btn_convert.grid(column=7, columnspan=1, row=1)
    content.columnconfigure(1, weight=3)
    frame.columnconfigure(2, weight=2)
    content.mainloop()


cls()
configure_and_create_gui()
