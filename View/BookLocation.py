
import tkinter as tk
from tkinter import ttk


class BookLocation(ttk.Frame):
    def __init__(self, parent, controller, app):
        ttk.Frame.__init__(self, parent)
        self.style = ttk.Style(self)
        self.controller = controller
        self.app = app
        self.locationLabel = ttk.Label()
        # widgets
        self.bookIDInput = ttk.Entry(self, width=50)
        self.bookCopyIDInput = ttk.Entry(self, width=50)
        self.window = self.app
# ------------------------------------------------------------------------------------
        Title = ttk.Label(self, text='Book location', font=(
            "Helvetica", 17, 'bold'))
        Title.place(relx=0.5, y=10, anchor='center')
# ------------------------------------------------------------------------------------
        bookIDLableX = 50
        bookIDLableY = 130

        bookIDLabel = ttk.Label(self, text='Book ID:', font=(
            "Helvetica", 14, 'bold'))
        bookIDLabel.place(x=bookIDLableX, y=bookIDLableY, anchor='w')
# ------------------------------------------------------------------------------------
        bookIDInputX = bookIDLableX + 140
        bookIDInputY = bookIDLableY - 9

        self.bookIDInput.place(x=bookIDInputX, y=bookIDInputY)
# ------------------------------------------------------------------------------------

        bookCopyIDLableX = bookIDLableX
        bookCopyIDLableY = bookIDLableY + 50

        bookCopyID = ttk.Label(self, text='Book copy ID:', font=(
            "Helvetica", 14, 'bold'))
        bookCopyID.place(x=bookCopyIDLableX,
                         y=bookCopyIDLableY, anchor='w')
# ------------------------------------------------------------------------------------
        bookCopyIDInputX = bookCopyIDLableX + 140
        bookCopyIDInputY = bookCopyIDLableY - 9

        self.bookCopyIDInput.place(x=bookCopyIDInputX, y=bookCopyIDInputY)
# ------------------------------------------------------------------------------------

        # Create the "Search" button
        self.searchButton = ttk.Button(
            self, text="Search", command=self.searchExecute)
        searchButtonX = bookIDInputX + 350
        searchButtonY = (bookIDInputY + bookCopyIDLableY)/2 - 10
        self.searchButton.place(x=searchButtonX, y=searchButtonY)

# ------------------------------------------------------------------------------------

        self.returnToMainmenu = ttk.Button(
            self, text="Return to mainmenu", command=self.mainmenu)
        self.returnToMainmenu.place(x=600, y=500)
# ------------------------------------------------------------------------------------

    def searchExecute(self):
        self.locationLabel.destroy()
        dic = self.controller.getLocation(
            int(self.bookIDInput.get()), int(self.bookCopyIDInput.get()))
        if dic == False:
            pass
        else:
            self.locationLabel = ttk.Label(
                self, text="Floor: " + str(dic['floor']) + "\nSection: " + str(dic['section']) + "\nShelf number: " + str(dic['shelfNumber']), font=("Courier", 15))
            self.locationLabel.place(
                x=self.app.WIDTH/2, y=400, anchor='center')
# ------------------------------------------------------------------------------------

    def mainmenu(self):
        if self.controller.isAdmin:
            self.app.show_frame("AdminMenu")
        else:
            self.app.show_frame("StudentMenu")
