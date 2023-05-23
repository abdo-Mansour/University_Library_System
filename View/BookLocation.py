
import tkinter as tk
from tkinter import ttk


class BookLocation(ttk.Frame):
    def __init__(self, parent, controller, app):
        ttk.Frame.__init__(self, parent)
        self.style = ttk.Style(self)
        self.controller = controller
        self.app = app

        # widgets
        self.bookTitleInput = ttk.Entry(self, width=50)
        self.ISBNInput = ttk.Entry(self, width=50)
        self.window = self.app
# ------------------------------------------------------------------------------------
        Title = ttk.Label(self, text='Book location', font=(
            "Helvetica", 17, 'bold'))
        Title.place(relx=0.5, y=10, anchor='center')
# ------------------------------------------------------------------------------------
        bookTitleLableX = 50
        bookTitleLableY = 130

        bookTitleLabel = ttk.Label(self, text='Title:', font=(
            "Helvetica", 14, 'bold'))
        bookTitleLabel.place(x=bookTitleLableX, y=bookTitleLableY, anchor='w')
# ------------------------------------------------------------------------------------
        bookTitleInputX = bookTitleLableX + 80
        bookTitleInputY = bookTitleLableY - 9

        self.bookTitleInput.place(x=bookTitleInputX, y=bookTitleInputY)
# ------------------------------------------------------------------------------------

        ISBNLableX = bookTitleLableX
        ISBNLableY = bookTitleLableY + 50

        ISBN = ttk.Label(self, text='ISBN:', font=(
            "Helvetica", 14, 'bold'))
        ISBN.place(x=ISBNLableX, y=ISBNLableY, anchor='w')
# ------------------------------------------------------------------------------------
        ISBNInputX = ISBNLableX + 80
        ISBNInputY = ISBNLableY - 9

        self.ISBNInput.place(x=ISBNInputX, y=ISBNInputY)
# ------------------------------------------------------------------------------------

        # Create the "Search" button
        self.searchButton = ttk.Button(
            self, text="Search")
        searchButtonX = bookTitleInputX + 350
        searchButtonY = (bookTitleInputY + ISBNLableY)/2 - 10
        self.searchButton.place(x=searchButtonX, y=searchButtonY)
