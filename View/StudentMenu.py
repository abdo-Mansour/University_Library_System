import tkinter as tk

from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.ttk import Label


class StudentMenu(ttk.Frame):
    def __init__(self, parent, app, controller):
        ttk.Frame.__init__(self, parent)
        self.style = ttk.Style(self)
        self.controller = controller
        self.app = app

        message = Label(self, text="Hello, Student! How may I server you ?")
        message.pack(pady=(200, 0))

        button_frame = ttk.Frame(self)
        button_frame.pack(pady=(0, 0))  # Adjust the top padding value to center the buttons

        browse_books_button = ttk.Button(button_frame, text="Browse Books", command=self.app.show_frame("Browse"))
        browse_books_button.pack(pady=10)

        update_user_data_button = ttk.Button(button_frame, text="Update User Data", command=self.app.show_frame("UpdateUserDetails"))
        update_user_data_button.pack(pady=10)

        show_books_button = ttk.Button(button_frame, text="Show Books Based On Criteria", command=self.app.show_frame("SearchBook"))
        show_books_button.pack(pady=10)