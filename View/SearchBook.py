
import tkinter as tk
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter.ttk import Label


class SearchBook(ttk.Frame):

    def __init__(self, parent, controller, app):
        ttk.Frame.__init__(self, parent)
        self.style = ttk.Style(self)
        self.controller = controller
        self.app = app
        # widgets
        entry = tk.Entry(self, width=50)
        window = self.app
        entry.pack(side=tk.LEFT)

        # Create the "Search" button
        search_button = tk.Button(
            self, text="Search")
        search_button.grid(row=0, column=0, padx=10, pady=1)
        # Create a style object
        style = ttk.Style(window)

        # Set the font and background color of the OptionMenu
        style.configure("TCombobox", font=("Arial", 12))
        style.configure("TCombobox", fieldbackground="white")

        # Set the highlight color of the OptionMenu
        style.map("TCombobox", fieldbackground=[("readonly", "white")])

        # Create a list of options
        options = ['None', 'Title', 'PageCount', 'ISBN', 'Language',
                   'Description', 'Publisher', 'MinimumAgeToRead', 'PublicationYear']

        # Create the variable to hold the selected option
        var = tk.StringVar(window)

        # Set the initial option
        var.set(options[0])

        # Create the OptionMenu with the customized style
        option_menu = ttk.OptionMenu(window, var, *options)
        option_menu.pack(pady=10)
