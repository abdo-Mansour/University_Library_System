
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
        from View.AdminMenu import AdminMenu
        from View.AddUser import AddUser
        from View.Browse import Browse
        from View.Report import Report
        from View.SearchBook import SearchBook
        from View.UpdateBookDetails import UpdateBookDetails
        from View.UpdateUserDetails import UpdateUserDetails
        from View.DeleteBook import DeleteBook
        from View.DeleteUser import DeleteUser
        from View.BookLocation import BookLocation
        # from View.BorrowBook import BorrowBook
        from View.StudentMenu import StudentMenu
        # from View.AdminMenu import AdminMenu

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
        self.container = ttk.Frame(self)
        # set width and height
        self.container.config(width=1000, height=580)
        self.container.pack(side="top", fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.frameClasses = {"Login": Login, "AddBook": AddBook, "AdminMenu": AdminMenu, "AddUser": AddUser, "Browse": Browse, "Report": Report, "SearchBook": SearchBook, "UpdateBookDetails": UpdateBookDetails, "UpdateUserDetails": UpdateUserDetails, "DeleteBook": DeleteBook, "DeleteUser": DeleteUser, "BookLocation": BookLocation, "StudentMenu": StudentMenu}
        # for F in (Login):

        page_name = F.__name__
        frame = F(parent=self.container, app=self, controller=self.controller)
        self.frames[page_name] = frame
        
        # put all of the pages in the same location;
        # the one on the top of the stacking order
        # will be the one that is visible.
        frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("Login")
    # to display the current frame passed as
    # parameter

    def create_if_doesnt_exist(self, name_of_frame):
        if(name_of_frame not in self.frames):
            frame = self.frameClasses[name_of_frame](parent= self.container, app=self, controller=self.controller)
            self.frames[name_of_frame] = frame 
        
    
    def destroy_frame(self, name_of_frame):
        self.frames[name_of_frame].grid_forget()
    

    def show_frame(self, cont):
        print("I am trying to show frame " + cont)
        frame = self.frames[cont]
        frame.tkraise()


# first window frame startpage
