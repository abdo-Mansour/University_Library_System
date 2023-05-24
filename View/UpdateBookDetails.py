import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class UpdateBookDetails(ttk.Frame):
    def __init__(self, parent, app, controller):
        ttk.Frame.__init__(self, parent)
        self.style = ttk.Style(self)
        self.controller = controller
        self.app = app
        print("UpdateBookDetails.__init__")

        # Configure grid weights
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Widgets
        self.show_info_label = ttk.Label(
            self, text='Update Book Details', font=("Helvetica", 18, 'bold'))
        self.show_info_label.grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Label(self, text="ISBN", font=("Helvetica", 14, 'bold')).grid(
            row=1, column=0, padx=10, pady=5, sticky=tk.E)
        self.isbn_entry = ttk.Entry(self, width=30)
        self.isbn_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        self.book_info_entries = {}
        self.create_book_info_table()

        search_button = ttk.Button(self, text="Search", command=self.search_book)
        search_button.grid(row=2, column=0, columnspan=2, pady=10)

        save_button = ttk.Button(self, text="Save Changes", command=self.save_changes)
        save_button.grid(row=3, column=0, padx=5, pady=20, sticky=tk.E)

        button_back = ttk.Button(self, text="Back", command=lambda: self.app.show_frame("AdminMenu"))
        button_back.grid(row=3, column=1, padx=5, pady=20, sticky=tk.W)

    def create_book_info_table(self):
        book_info_labels = {
            "BookID": "Book Id",
            "Title": "Title",
            "PageCount": "Page Count",
            "ISBN": "ISBN",
            "Language": "Language",
            "Description": "Description",
            "Publisher": "Publisher",
            "MinAgeToRead": "Minimum Age to Read",
            "PublicationYear": "Publication Year"
        }

        row = 4
        for key, label_text in book_info_labels.items():
            ttk.Label(self, text=label_text, font=("Helvetica", 14, 'bold')).grid(
                row=row, column=0, padx=10, pady=5, sticky=tk.E)
            entry = ttk.Entry(self, width=30)
            entry.grid(row=row, column=1, padx=10, pady=5, sticky=tk.W)
            self.book_info_entries[key] = entry
            row += 1

    def search_book(self):
        isbn = self.isbn_entry.get()
        book_info_list = self.controller.getBooksBy("ISBN", isbn)
        
        print(book_info_list[0])
        
        if book_info_list:
            # Assuming there's only one book with the given ISBN
            book_info = book_info_list[0]
            for key, entry in self.book_info_entries.items():
                entry.delete(0, tk.END)
                entry.insert(tk.END, book_info.get(key, ""))
        else:
            showinfo("Error", "Book not found")

    def save_changes(self):
        updated_details = [
            self.book_info_entries["BookID"].get(),
            self.book_info_entries["Title"].get(),
            self.book_info_entries["PageCount"].get(),
            self.isbn_entry.get(),
            self.book_info_entries["Language"].get(),
            self.book_info_entries["Description"].get(),
            self.book_info_entries["Publisher"].get(),
            self.book_info_entries["MinAgeToRead"].get(),
            self.book_info_entries["PublicationYear"].get()
        ]

        if(self.controller.updateBookDetails(updated_details)):
            showinfo("Success", "Book details updated successfully")
        else:
            showinfo("Error", "Failed to update book details")
