import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from Controller.Controller import Controller


class AddBook(ttk.Frame):
    def __init__(self, parent, app, controller: Controller):
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

        frame_location = ttk.Frame(frame_details)
        frame_location.pack(side="left", padx=10)

        self.entry_book_copies = ttk.Entry(frame_details)
        self.entry_book_copies.pack(side="left", padx=10)
        self.entry_book_copies.insert(0, "Book Copies")

        self.entry_min_age = ttk.Entry(frame_details)
        self.entry_min_age.pack(side="left", padx=10)
        self.entry_min_age.insert(0, "Min Age to Read")

        frame_language_genre = ttk.Frame(frame_details)
        frame_language_genre.pack(side="left", padx=10)

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

        label_language = ttk.Label(frame_language_genre, text="Language")
        label_language.pack(side="left", padx=10)

        self.language_var = tk.StringVar()
        self.language_var.set("")  # Default language selection

        language_options = ["", "English", "French", "Arabic", "German", "Russian"]
        self.language_dropdown = ttk.OptionMenu(frame_language_genre, self.language_var, *language_options)
        self.language_dropdown.pack(side="left", pady=5)

        frame_description = ttk.Frame(self)
        frame_description.pack(pady=10)

        self.text_description = tk.Text(frame_description, width=40, height=5)
        self.text_description.pack(side="top", padx=10, pady=5)
        self.text_description.insert("1.0", "Description")  # Placeholder text

        frame_location = ttk.Frame(self)
        frame_location.pack(pady=10)

        label_location = ttk.Label(frame_location, text="Location")
        label_location.pack(side="top", padx=10)

        frame_floor_shelf_genre = ttk.Frame(frame_location)
        frame_floor_shelf_genre.pack(pady=5)

        frame_floor_shelf = ttk.Frame(frame_floor_shelf_genre)
        frame_floor_shelf.pack(side="left")

        label_floor = ttk.Label(frame_floor_shelf, text="Floor no.")
        label_floor.pack(side="left")

        self.floor_var = tk.StringVar()
        self.floor_var.set("")  # Default floor selection

        floor_options = ["", "1", "2", "3"]
        self.floor_dropdown = ttk.OptionMenu(frame_floor_shelf, self.floor_var, *floor_options)
        self.floor_dropdown.pack(side="left", padx=5)

        label_shelf = ttk.Label(frame_floor_shelf, text="Shelf no.")
        label_shelf.pack(side="left", padx=10)

        self.shelf_var = tk.StringVar()
        self.shelf_var.set("")  # Default shelf selection

        shelf_options = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        self.shelf_dropdown = ttk.OptionMenu(frame_floor_shelf, self.shelf_var, *shelf_options)
        self.shelf_dropdown.pack(side="left", padx=5)

        label_genre = ttk.Label(frame_floor_shelf_genre, text="Genre")
        label_genre.pack(side="left", padx=10)

        genre_options = ["", "Mystery", "Romance", "Thriller", "Sci-Fi", "Fantasy", "Adventure", "Historical Fiction",
                         "Biography", "Horror",
                         "Comedy", "Drama", "Action", "Crime", "Western", "Young Adult", "Children's", "Poetry",
                         "Self-help", "Cooking"]

        self.genre_var = tk.StringVar()
        self.genre_var.set("")  # Default genre selection

        self.genre_dropdown = ttk.OptionMenu(frame_floor_shelf_genre, self.genre_var, *genre_options)
        self.genre_dropdown.pack(side="left", padx=5)

        button_frame = ttk.Frame(self)
        button_frame.pack(pady=10)

        button_back = ttk.Button(button_frame, text="Back", command=lambda: self.app.show_frame("AdminMenu"))
        button_back.pack(side="left", padx=10)

        button_add_book = ttk.Button(button_frame, text="Add Book", command=self.add_book)
        button_add_book.pack(side="left", padx=10)



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
        book_copies = self.entry_book_copies.get()
        min_age = self.entry_min_age.get()
        genre = self.genre_var.get()

        # Check if any of the inputs are empty or None
        if (
                not author or author == "Author" or
                not publisher or publisher == "Publisher" or
                not book_title or book_title == "Title" or
                not isbn or isbn == "ISBN" or
                not page_count or page_count == "Page Count" or
                not language or language == "" or
                not publication_year or publication_year == "Publication Year" or
                not description or description.strip() == "Description" or
                not book_copies or book_copies == "Book Copies" or
                not min_age or min_age == "Min Age to Read" or
                not genre or genre == "" or
                not self.floor_var.get() or not self.shelf_var.get()
        ):
            showinfo("Invalid Input", "Please fill all fields with correct values")
            return

        data = [book_title, isbn, page_count, language, description, publisher, min_age, publication_year]

        if self.controller.addBook(data):
            showinfo("Success", "Book added successfully")
            self.go_back()
        else:
            showinfo("Error", "Something went wrong")
        pass

    def go_back(self):
        # Perform necessary actions to go back
        # ...
        # You can use the self.controller or self.app to interact with the rest of the application
        pass
