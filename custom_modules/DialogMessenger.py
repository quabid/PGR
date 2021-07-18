import tkinter
from tkinter import messagebox as tkMessageBox


def error(title="title", message="message"):
    tkMessageBox.showinfo(title, message)


def warning(title="title", message="message"):
    tkMessageBox.showwarning(title, message)


def success(title="title", message="message"):
    tkMessageBox.showinfo(title, message)


MESSAGE_SWITCH = {
    "error": error,
    "warning": warning,
    "success": success
}