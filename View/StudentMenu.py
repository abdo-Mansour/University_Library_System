from tkinter import ttk
from tkinter.ttk import Label


class StudentMenu(ttk.Frame):
    def __init__(self, parent, app, controller):
        ttk.Frame.__init__(self, parent)
        self.style = ttk.Style(self)
        self.controller = controller
        self.app = app

        message = Label(self, text="Hello, Student! How may I server you ?")
        message.pack(pady=(200, 0))

        button_frame = ttk.Frame(self)
        button_frame.pack(pady=(0, 0))  # Adjust the top padding value to center the buttons

        browse_books_button = ttk.Button(button_frame, text="Browse Books", command=self.browse)
        browse_books_button.pack(pady=10)

        update_user_data_button = ttk.Button(button_frame, text="Update User Data", command=self.update_user_details)
        update_user_data_button.pack(pady=10)

        show_books_button = ttk.Button(button_frame, text="Show Books Based On Criteria", command=self.search_book)
        show_books_button.pack(pady=10)

        add_book_button = ttk.Button(self, text="Log Out", command=self.log_out)
        add_book_button.pack(pady=10)

    def browse(self):
        self.app.frames["Browse"].refreshList()
        command = self.app.show_frame("Browse")

    def update_user_details(self):
        command = self.app.show_frame("UpdateUserDetails")

    def search_book(self):
        command = self.app.show_frame("SearchBook")
    
    def log_out(self):
        self.controller.Person = None
        self.app.show_frame("Login")
