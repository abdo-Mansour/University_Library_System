import tkinter as tk
from tkinter import ttk


class UpdateBookDetails(ttk.Frame):
    def __init__(self, parent, app, controller):
        ttk.Frame.__init__(self, parent)
        self.style = ttk.Style(self)
        self.controller = controller
        self.app = app
        print("UpdateBookDetails.__init__")

        # Widgets
        self.show_info_label = ttk.Label(
            self, text='Update Book Details', font=("Helvetica", 18, 'bold'))
        self.show_info_label.grid(
            row=0, column=0, columnspan=2, pady=10, sticky=tk.W)

        self.isbn_entry = ttk.Entry(self, width=30)
        self.isbn_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)
        ttk.Label(self, text="ISBN", font=("Helvetica", 14, 'bold')).grid(
            row=1, column=0, padx=10, pady=5, sticky=tk.W)

        self.book_info_entries = {}
        self.create_book_info_table()

        ttk.Button(self, text="Search", command=self.search_book).grid(
            row=2, column=0, columnspan=2, pady=10)
        ttk.Button(self, text="Save Changes", command=self.save_changes).grid(
            row=3, column=0, columnspan=2, pady=20)

    def create_book_info_table(self):
        book_info_labels = {
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
                row=row, column=0, padx=10, pady=5, sticky=tk.W)
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
            # Display an error message or handle the case when the book is not found
            pass

    def save_changes(self):
        updated_details = [
            self.book_info_entries["Title"].get(),
            self.book_info_entries["PageCount"].get(),
            self.isbn_entry.get(),
            self.book_info_entries["Language"].get(),
            self.book_info_entries["Description"].get(),
            self.book_info_entries["Publisher"].get(),
            self.book_info_entries["MinAgeToRead"].get(),
            self.book_info_entries["PublicationYear"].get()
        ]
        self.controller.updateBookDetails(updated_details)
