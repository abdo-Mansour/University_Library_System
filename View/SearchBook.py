
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
        self.bookList = []
        self.prevYCoordForBookListView = 0
        self.bookViewLables = []
        # widgets
        self.entry = ttk.Entry(self, width=50)
        self.window = self

        Title = ttk.Label(self, text='Search Books', font=(
            "Helvetica", 17, 'bold'))
        Title.place(relx=0.5, y=10, anchor='center')

        searchBoxX = 175
        searchBoxY = 50

        self.entry.place(x=searchBoxX, y=searchBoxY)

        # Create the "Search" button
        self.searchButton = ttk.Button(
            self, text="Search", command=self.getBooksQuery)
        searchButtonX = searchBoxX + 155
        searchButtonY = searchBoxY + 40
        self.searchButton.place(x=searchButtonX, y=searchButtonY)
        # Create a style object
        style = ttk.Style(self.window)

        # Set the font and background color of the OptionMenu
        style.configure("TCombobox", font=("Arial", 12))
        style.configure("TCombobox", fieldbackground="white")

        # Set the highlight color of the OptionMenu
        style.map("TCombobox", fieldbackground=[("readonly", "white")])

        # Create a list of options
        options = ['Choose filter', 'Title', 'Page count', 'ISBN', 'Language',
                   'Description', 'Publisher', 'Minimum age', 'Publication year']
        queries = ['None', 'Title', 'PageCount', 'ISBN', 'Language',
                   'Description', 'Publisher', 'MinimumAgeToRead', 'PublicationYear']

        for option, query in zip(options, queries):
            self.optionDictionary[option] = query

        # Create the variable to hold the selected option
        self.filter = tk.StringVar(self.window)
        # Set the initial option
        self.filter.set(options[0])
        # Create the OptionMenu with the customized style
        self.optionMenu = ttk.OptionMenu(self.window, self.filter, *options)
        optionMenuX = searchBoxX + 320
        optionMenuY = searchBoxY - 4
        self.optionMenu.place(x=optionMenuX, y=optionMenuY)

        self.bookListView = tk.Canvas(self.window, width=700,
                                      height=400)

        self.bookListView.place(x=50, y=150)
        self.displayBookListView()
# ----------------------------------------------------------------------------------------------
        self.returnButton = ttk.Button(
            self, text="Return to Menu", command=self.returningToMainMenu)
        self.returnButton.place(x=600, y=10)

# -----------------------------------------------------------------------------------------------
    def displayBookListView(self):
        for l in self.bookViewLables:
            l.destroy()
        y = 50

        for i in range(len(self.bookList)):
            label = ttk.Label(self.bookListView, text=str(i + 1) + ")\nBook title: " +
                          self.bookList[i]['Title'] + '\n' + "ISBN: " + str(self.bookList[i]['ISBN']) + '\n', font=("Courier", 15))
            self.bookViewLables.append(label)
            self.bookListView.create_window(0, y, window=label, anchor='w')
            y += 100
        
        scrollbar = ttk.Scrollbar(
            self.bookListView, orient='vertical', command=self.bookListView.yview)
        scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')
        self.bookListView.config(yscrollcommand=scrollbar.set,
                                 scrollregion=(0, 0, 0, y))

    def getBooksQuery(self):
        query = self.entry.get()
        result = self.controller.getBooksBy(
            self.optionDictionary[self.filter.get()], query)
        if (result == False):

            showinfo("Query error", "Please choose a filter")
        else:
            self.bookList = result
            self.displayBookListView()

    def returningToMainMenu(self):
        if self.controller.isAdmin:
            self.app.show_frame("AdminMenu")
        else:
            self.app.show_frame("StudentMenu")
        # button_back = ttk.Button(
        #     self, text="Back", command=self.app.show_frame("AdminMenu"))
        # button_back.place(x=600, y=400)
