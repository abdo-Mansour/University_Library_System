from tkinter import ttk


class BookLocation(ttk.Frame):
    def __init__(self, parent, controller, app):
        ttk.Frame.__init__(self, parent)
        self.style = ttk.Style(self)
        self.controller = controller
        self.app = app
        self.locationLabel = ttk.Label()
        # widgets
        self.ISBNInput = ttk.Entry(self, width=50)
        self.bookCopyIDInput = ttk.Entry(self, width=50)
        self.window = self.app
# ------------------------------------------------------------------------------------
        Title = ttk.Label(self, text='Book location', font=(
            "Helvetica", 17, 'bold'))
        Title.place(relx=0.5, y=10, anchor='center')
# ------------------------------------------------------------------------------------
        ISBNLableX = 50
        ISBNLableY = 130

        ISBNLabel = ttk.Label(self, text='ISBN:', font=(
            "Helvetica", 14, 'bold'))
        ISBNLabel.place(x=ISBNLableX, y=ISBNLableY, anchor='w')
# ------------------------------------------------------------------------------------
        ISBNInputX = ISBNLableX + 140
        ISBNInputY = ISBNLableY - 9

        self.ISBNInput.place(x=ISBNInputX, y=ISBNInputY)
# ------------------------------------------------------------------------------------

        bookCopyIDLableX = ISBNLableX
        bookCopyIDLableY = ISBNLableY + 50

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
        searchButtonX = ISBNInputX + 350
        searchButtonY = (ISBNInputY + bookCopyIDLableY)/2 - 10
        self.searchButton.place(x=searchButtonX, y=searchButtonY)

# ------------------------------------------------------------------------------------

        self.returnToMainmenu = ttk.Button(
            self, text="Return to Menu", command=self.mainmenu)
        self.returnToMainmenu.place(x=600, y=500)
# ------------------------------------------------------------------------------------

    def searchExecute(self):
        self.locationLabel.destroy()
        dic = self.controller.getLocation(
            str(self.ISBNInput.get()), int(self.bookCopyIDInput.get()))
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
