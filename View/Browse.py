import tkinter as tk
from tkinter import ttk, CENTER, END
from tkinter.ttk import Label


class Browse(ttk.Frame):

    def __init__(self, parent, controller, app):
        ttk.Frame.__init__(self, parent)
        self.style = ttk.Style(self)
        self.controller = controller
        self.app = app
        self.prevYCoordForBookListView = 0
        self.bookViewLables = []
        self.books_list = None
        # widgets

        message = Label(self, text="All Books", font=24)
        message.place(x=self.app.WIDTH / 2, y=12, anchor=CENTER)

        self.book_list_box = tk.Listbox(self, width=71, font=18, height=17)

        # self.books_list = controller.getAllBooks()
        # index = 1
        # for i in self.books_list:
        #     line_content = f"{index}) {i['Title']}, ISBN: {i['ISBN']}"
        #     index += 1
        #     self.book_list_box.insert(tk.END, line_content)

        self.book_list_box.place(x=5, y=300, anchor="w")

        button_back = ttk.Button(self, text="Back", command=self.back)
        button_back.place(x=self.app.WIDTH / 2, y=550, anchor=CENTER)

    def back(self):
        if self.controller.isAdmin:
            command = self.app.show_frame("AdminMenu")
        else:
            command = self.app.show_frame("StudentMenu")

    def refreshList(self):
        self.book_list_box.delete(0, END)
        self.books_list = self.controller.getAllBooks()
        index = 1
        for i in self.books_list:
            line_content = f"{index}) {i['Title']}, ISBN: {i['ISBN']}"
            index += 1
            self.book_list_box.insert(tk.END, line_content)

    # def getBooksQuery(self):
    #     result = self.controller.getAllBooks()
    #     print(result)
    #     self.bookList = result
    #     # self.displayBookListView()


