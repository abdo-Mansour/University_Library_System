import tkinter as tk
from tkinter import ttk

class AddBook(ttk.Frame):
    def __init__(self, parent, app, controller):
        ttk.Frame.__init__(self, parent)
        self.style = ttk.Style(self)
        self.controller = controller
        self.app = app
        
        # Widgets
        label_title = ttk.Label(self, text="Add Book", font=("Helvetica", 20, 'bold'))
        label_title.pack(pady=10)

        frame_id_title = ttk.Frame(self)
        frame_id_title.pack(pady=10)

        self.entry_book_title = ttk.Entry(frame_id_title)
        self.entry_book_title.pack(side="left", padx=10)
        self.entry_book_title.insert(0, "Title")

        self.entry_author = ttk.Entry(frame_id_title)
        self.entry_author.pack(side="left", padx=10)
        self.entry_author.insert(0, "Author")

        self.entry_publisher = ttk.Entry(frame_id_title)
        self.entry_publisher.pack(side="left", padx=10)
        self.entry_publisher.insert(0, "Publisher")

        frame_details = ttk.Frame(self)
        frame_details.pack(pady=10)

        self.entry_location_id = ttk.Entry(frame_details)
        self.entry_location_id.pack(side="left", padx=10)
        self.entry_location_id.insert(0, "Location ID")

        self.entry_book_copies = ttk.Entry(frame_details)
        self.entry_book_copies.pack(side="left", padx=10)
        self.entry_book_copies.insert(0, "Book Copies")

        self.entry_min_age = ttk.Entry(frame_details)
        self.entry_min_age.pack(side="left", padx=10)
        self.entry_min_age.insert(0, "Min Age to Read")

        frame_isbn_page_year = ttk.Frame(self)
        frame_isbn_page_year.pack(pady=10)

        self.entry_page_count = ttk.Entry(frame_isbn_page_year)
        self.entry_page_count.pack(side="left", padx=10)
        self.entry_page_count.insert(0, "Page Count")

        self.entry_publication_year = ttk.Entry(frame_isbn_page_year)
        self.entry_publication_year.pack(side="left", padx=10)
        self.entry_publication_year.insert(0, "Publication Year")

        self.entry_isbn = ttk.Entry(frame_isbn_page_year)
        self.entry_isbn.pack(side="left", padx=10)
        self.entry_isbn.insert(0, "ISBN")

        frame_language = ttk.Frame(self)
        frame_language.pack(pady=10)

        label_language = ttk.Label(frame_language, text="Language:")
        label_language.pack(side="left", padx=10)

        self.language_var = tk.StringVar()
        self.language_var.set("")  # Default language selection

        language_options = ["", "English", "French", "Arabic", "German", "Russian"]
        self.language_dropdown = ttk.OptionMenu(frame_language, self.language_var, *language_options)
        self.language_dropdown.pack(side="left", padx=10)

        frame_description = ttk.Frame(self)
        frame_description.pack(pady=10)

        self.text_description = tk.Text(frame_description, width=40, height=5)
        self.text_description.pack(side="left", padx=10)
        self.text_description.insert("1.0", "Description")  # Placeholder text

        button_frame = ttk.Frame(self)
        button_frame.pack(pady=10)

        button_add_book = ttk.Button(button_frame, text="Add Book", command=self.add_book)
        button_add_book.pack(side="left", padx=10)

        button_back = ttk.Button(button_frame, text="Back", command=self.go_back)
        button_back.pack(side="left", padx=10)

    def add_book(self):
        # Get the input values from the entry fields
        author = self.entry_author.get()
        publisher = self.entry_publisher.get()
        book_title = self.entry_book_title.get()
        isbn = self.entry_isbn.get()
        page_count = self.entry_page_count.get()
        language = self.language_var.get()
        publication_year = self.entry_publication_year.get()
        description = self.text_description.get("1.0", tk.END)
        location_id = self.entry_location_id.get()
        book_copies = self.entry_book_copies.get()
        min_age = self.entry_min_age.get()

        # Perform necessary actions to add the book
        # ...
        # You can use the self.controller or self.app to interact with the rest of the application
        pass

    def go_back(self):
        # Perform necessary actions to go back
        # ...
        # You can use the self.controller or self.app to interact with the rest of the application
        pass
