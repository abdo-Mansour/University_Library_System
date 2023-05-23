

import tkinter as tk
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter.ttk import Label


class Browse(ttk.Frame):

    def __init__(self, parent, controller, app):
        ttk.Frame.__init__(self, parent)
        self.style = ttk.Style(self)
        self.controller = controller
        self.app = app
        self.bookList = []
        self.prevYCoordForBookListView = 0
        self.bookViewLables = []
        # widgets

        self.window = self.app

        Title = ttk.Label(self, text='Browse Books', font=(
            "Helvetica", 17, 'bold'))
        Title.place(relx=0.5, y=10, anchor='center')

        searchBoxX = 175
        searchBoxY = 50


       
        # Create a style object
        style = ttk.Style(self.window)

        # Set the font and background color of the OptionMenu
        style.configure("TCombobox", font=("Arial", 12))
        style.configure("TCombobox", fieldbackground="white")

        # Set the highlight color of the OptionMenu
        style.map("TCombobox", fieldbackground=[("readonly", "white")])



        self.bookListView = tk.Canvas(self.window, width=700,
                                      height=500)

        self.bookListView.place(x=50, y=150)
        self.getBooksQuery()
        # self.displayBookListView()

    def displayBookListView(self):
        for l in self.bookViewLables:
            l.destroy()
        y = 50

        for i in range(len(self.bookList)):
            label = Label(self.bookListView, text=str(i + 1) + ")\nBook title: " +
                          self.bookList[i].Title + '\n' + "ISBN: " + str(self.bookList[i].ISBN) + '\n', font=("Courier", 15))
            self.bookViewLables.append(label)
            self.bookListView.create_window(0, y, window=label, anchor='w')
            y += 100

        scrollbar = tk.Scrollbar(
            self.bookListView, orient='vertical', command=self.bookListView.yview)
        scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')
        self.bookListView.config(yscrollcommand=scrollbar.set,
                                 scrollregion=(0, 0, 0, y))

    def getBooksQuery(self):
        result = self.controller.getAllBooks()
        print(result)
        self.bookList = result
        # self.displayBookListView()
        
  
       