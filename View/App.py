
from ttkthemes import ThemedStyle
from tkinter import ttk
import tkinter as tk
LARGEFONT = ("Verdana", 35)


class App(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, controller, *args, **kwargs):
        # import all the views
        from View.Login import Login
        from View.AddBook import AddBook
        from View.AddUser import AddUser
        from View.Browse import Browse
        from View.SearchBook import SearchBook
        from View.UpdateBookDetails import UpdateBookDetails
        from View.UpdateUserDetails import UpdateUserDetails
        from View.DeleteBook import DeleteBook
        from View.DeleteUser import DeleteUser
        from View.BookLocation import BookLocation
        from View.BorrowBook import BorrowBook

        print("I AM RUNNING")

        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Library System")
        self.WIDTH = 800
        self.HEIGHT = 580
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.resizable(False, False)

        self.style = ThemedStyle(self)
        self.style.set_theme("ubuntu")
        self.controller = controller

        # creating a container
        container = ttk.Frame(self)
        # set width and height
        container.config(width=1000, height=580)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (AddBook,):
            page_name = F.__name__
            frame = F(parent=container, app=self, controller=self.controller)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("AddBook")
    # to display the current frame passed as
    # parameter

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# first window frame startpage
