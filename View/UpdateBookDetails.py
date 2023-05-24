import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from Controller.Controller import Controller


class UpdateBookDetails(ttk.Frame):
    def __init__(self, parent, app, controller: Controller):
        ttk.Frame.__init__(self, parent)
        self.style = ttk.Style(self)
        self.controller = controller
        self.app = app

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
            row=1, column=0, padx=(230,0), pady=5, sticky=tk.W)
        self.isbn_entry = ttk.Entry(self, width=30)
        self.isbn_entry.grid(row=1, column=1, padx=(0,210), pady=5, sticky=tk.E)

        self.book_info_entries = {}
        self.create_book_info_table()

        search_button = ttk.Button(self, text="Search", command=self.search_book)
        search_button.grid(row=2, column=0, columnspan=2, pady=10)

        save_button = ttk.Button(self, text="Save Changes", command=self.save_changes)
        save_button.grid(row=16, column=0, padx=(260,5), pady=20, sticky=tk.W)

        button_back = ttk.Button(self, text="Back", command=lambda: self.app.show_frame("AdminMenu"))
        button_back.grid(row=16, column=1, padx=5, pady=20, sticky=tk.W)

    def create_book_info_table(self):
        book_info_labels = {
            "BookID": "Book Id",
            "Title": "Title",
            "PageCount": "Page Count",
            "ISBN": "ISBN",
            "Language": "Language",
            "Description": "Description",
            "Publisher": "Publisher",
            "MinAgeToRead": "Minimum Age",
            "PublicationYear": "Publication Year"
        }

        row = 4
        for key, label_text in book_info_labels.items():
            ttk.Label(self, text=label_text, font=("Helvetica", 14, 'bold')).grid(
                row=row, column=0, padx=(230,5), pady=5, sticky=tk.W)
            entry = ttk.Entry(self, width=30)
            entry.grid(row=row, column=1, padx=(20,210), pady=5, sticky=tk.E)
            self.book_info_entries[key] = entry
            row += 1

    def search_book(self):
        isbn = self.isbn_entry.get()
        book_info_list = self.controller.getBooksBy("ISBN", isbn)
                
        if book_info_list:
            bookID = book_info_list[0]["BookID"]
            ISBN = book_info_list[0]["ISBN"]
            if book_info_list:
                # Assuming there's only one book with the given ISBN
                book_info = book_info_list[0]
                for key, entry in self.book_info_entries.items():
                    if key == "BookID":
                        entry.insert(0, bookID)
                        entry.config(state="disabled")
                    elif key == "ISBN":
                        entry.insert(0, ISBN)
                        entry.config(state="disabled")
                    else:
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
            self.book_info_entries["Description"].get("1.0", tk.END).strip(),
            self.book_info_entries["Publisher"].get(),
            self.book_info_entries["MinAgeToRead"].get(),
            self.book_info_entries["PublicationYear"].get()
        ]

        if(self.controller.updateBookDetails(updated_details)):
            self.app.frames["Browse"].refreshList()
            self.app.frames["Report"].refresh_report()
            
            showinfo("Success", "Book details updated successfully")
        else:
            showinfo("Error", "Failed to update book details")
