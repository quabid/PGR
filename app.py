import tkinter as tk
from tkinter import ttk
from tkinter.constants import BOTTOM, CENTER, LEFT, RIGHT


# Content manager
content = tk.Tk()
content.title("Converter")

# Main frame
frame = tk.Frame(content, borderwidth=1,
                 relief="ridge")
frame.grid(column=1, columnspan=12, row=1, padx=10, pady=10)

# User controls frame
controls_frame = tk.Frame(frame)
controls_frame.grid(columnspan=12, row=1, column=1, padx=10, pady=10)

# Labels
lbl_entry_number = tk.Label(
    controls_frame, bg="White", fg="Black", text="Enter Number")

# Text field
tf_entry_number = tk.Entry(controls_frame, width=15)
tf_entry_number.grid(padx=5)

# Buttons
btn_convert = tk.Button(controls_frame, text="convert".title(), width=10)

# Layout controls
frame.grid(column=0, row=6, columnspan=3)
lbl_entry_number.grid(column=1, row=1, columnspan=2)
tf_entry_number.grid(column=4, columnspan=2, row=1)
btn_convert.grid(column=7, columnspan=1, row=1)

content.columnconfigure(1, weight=3)
frame.columnconfigure(2, weight=2)
content.mainloop()
