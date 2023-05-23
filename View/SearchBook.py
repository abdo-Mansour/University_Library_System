
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
        self.optionDictionary = {}
        # widgets
        entry = ttk.Entry(self, width=50)
        window = self.app

        Title = ttk.Label(self, text='Search Books', font=(
            "Helvetica", 17, 'bold'))
        Title.place(relx=0.5, y=10, anchor='center')

        searchBoxX = 175
        searchBoxY = 50

        entry.place(x=searchBoxX, y=searchBoxY)

        # Create the "Search" button
        searchButton = ttk.Button(
            self, text="Search")
        searchButtonX = searchBoxX + 155
        searchButtonY = searchBoxY + 40
        searchButton.place(x=searchButtonX, y=searchButtonY)
        # Create a style object
        style = ttk.Style(window)

        # Set the font and background color of the OptionMenu
        style.configure("TCombobox", font=("Arial", 12))
        style.configure("TCombobox", fieldbackground="white")

        # Set the highlight color of the OptionMenu
        style.map("TCombobox", fieldbackground=[("readonly", "white")])

        # Create a list of options
        options = ['Choose filter', 'Title', 'Page count', 'ISBN', 'Language',
                   'Description', 'Publisher', 'Minimum age', 'Publication year']
        queries = ['Title', 'PageCount', 'ISBN', 'Language',
                   'Description', 'Publisher', 'MinimumAgeToRead', 'PublicationYear']

        for option, query in zip(options, queries):
            self.optionDictionary[option] = query

        # Create the variable to hold the selected option
        var = tk.StringVar(window)
        # Set the initial option
        var.set(options[0])
        # Create the OptionMenu with the customized style
        optionMenu = ttk.OptionMenu(window, var, *options)
        optionMenuX = searchBoxX + 320
        optionMenuY = searchBoxY - 4
        optionMenu.place(x=optionMenuX, y=optionMenuY)

        self.bookList = tk.Canvas(window, width=700,
                                  height=400)

        self.bookList.place(x=50, y=150)
        y = 0
        for i in range(1, 100):
            label = Label(self.bookList, text="File number " +
                          str(i), font=("Courier", 10))
            self.bookList.create_window(0, y, window=label)
            y += 10

        scrollbar = tk.Scrollbar(
            self.bookList, orient='vertical', command=self.bookList.yview)
        scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')
        self.bookList.config(yscrollcommand=scrollbar.set,
                             scrollregion=(0, 0, 0, y))
