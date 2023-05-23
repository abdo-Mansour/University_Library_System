

import tkinter as tk
from tkinter import ttk, CENTER
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

        message = Label(self, text="All Books", font=24)
        message.place(x=self.app.WIDTH / 2, y=12, anchor=CENTER)

        book_list = tk.Listbox(self, width=60, font=18, height=21)
        books = controller.getAllBooks()
        index = 1;
        for i in books:
            line_content = f"{index}) {i['Title']}, ISBN: {i['ISBN']}"
            index += 1
            book_list.insert(tk.END, line_content)

        book_list.place(x=5, y=300, anchor="w")

        button_back = ttk.Button(self, text="Back", command=self.back)
        button_back.place(x=5, y=550, anchor="w")

    def back(self):
        if self.controller.isAdmin:
            command = self.app.show_frame("AdminMenu")
        else:
            command = self.app.show_frame("StudentMenu")



    # def getBooksQuery(self):
    #     result = self.controller.getAllBooks()
    #     print(result)
    #     self.bookList = result
    #     # self.displayBookListView()


