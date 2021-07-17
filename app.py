import tkinter as tk
import re
import os
from tkinter import Spinbox, ttk
from tkinter.constants import BOTTOM, CENTER, LEFT, RIGHT
from custom_modules import custom, error, success, warning
from custom_modules.WindowEventHandler import handle

# Clear console


def cls(): return os.system('clear')


# Regex integers
integer_pattern = re.compile('^[0-9]+$')
float_pattern = re.compile('^[0-9]+(\.[0-9]+){1}$')


# Number converters
def to_hex(arg):
    if float_pattern.search(arg):
        return float.hex(float(arg))
    else:
        num = int(arg.strip())
        return hex(num).lstrip("0x").rstrip("L")


def to_octal(arg):
    num = 0
    if float_pattern.search(arg):
        message = warning("Warning: {} is a floating point number\n\tConverting {} to an integer, so the precision will be lost\n".format(
            arg, arg))
        print("\t{}\n".format(message))
        try:
            num = int(arg)
            return oct(num)
        except ValueError as e:
            message = custom(
                "Error casting {} to an integer".format(arg), 210, 180, 180)
            raise ValueError("Error casting {} to an integer".format(arg),
                             "Cause: {} is a floating point number".format(
                                 arg),
                             "Unable to cast {} to an integer".format(arg))

    else:
        num = int(arg)
        return oct(num).lstrip("0o").rstrip("L")


def to_binary(arg):
    num = 0
    if float_pattern.search(arg):
        message = warning("Warning: {} is a floating point number\n\tConverting {} to an integer, so the precision will be lost\n".format(
            arg, arg))
        print("\t{}\n".format(message))
        try:
            num = int(arg)
            return "{0:b}".format(num)
        except ValueError as e:
            message = custom(
                "Error casting {} to an integer".format(arg), 210, 180, 180)
            raise ValueError("Error casting {} to an integer".format(arg),
                             "Cause: {} is a floating point number".format(
                                 arg),
                             "Unable to cast {} to an integer".format(arg))

    else:
        num = int(arg)
        return "{0:b}".format(num)


# Spinbox
combobox_list = ("Hexadecimal", "Octal", "Binary")
combobox_switch = {
    "Hexadecimal": lambda arg: to_hex(arg),
    "Octal": lambda arg: to_octal(arg),
    "Binary": lambda arg: to_binary(arg)
}

""" The root window & it's openin and closing handlers
    configures a default size
"""
cls()
content = tk.Tk()
content.title("Converter")
content.geometry("500x124")
content.geometry("+500+174")
content.minsize(500, 124)
content.attributes("-alpha", 0.5)
handle(content)


# Top label
label_var = tk.StringVar()
label = tk.Label(content, textvariable=label_var, font=('calibre', 10, 'bold'))
label.grid(pady=1, ipadx=5, ipady=5, column=1, columnspan=12, row=1)

# User input component
tf_entry_number_var = tk.StringVar()
entry_results_var = tk.StringVar()

""" The main content pane
"""
frame = tk.Frame(content, borderwidth=1,
                 relief="ridge")
frame.grid(column=1, columnspan=12, row=2, padx=10, pady=10)

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
            print("\tConverting {} to {}".format(
                success(text_input), selected_item))

            function = combobox_switch[selected_item]
            results = function(text_input)

            if results:
                label_var.set(results)
                print("\tOrignal: {}\t{}: {}\n".format(
                    text_input, selected_item, results))

    except ValueError as ve:
        """  message = error("input error".title())
         cause = custom("\t{} is not a valid integer\n".format(ve), 200, 77, 75)
         print("\n\t{}\n\tCause:\t{}".format(message, cause)) """
        print("{}".format(ve))


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


configure_and_create_gui()
