import tkinter
import tkinter as tk

from tkinter import ttk, CENTER, NW, W, LEFT
from tkinter.messagebox import showinfo
from tkinter.ttk import Label


class Report(ttk.Frame):
    def __init__(self, parent, app, controller):
        ttk.Frame.__init__(self, parent)
        self.style = ttk.Style(self)
        self.controller = controller
        self.app = app

        report = self.controller.generateStatisticsReport()

        # self.grid_columnconfigure(0, weight=1)
        # self.grid_columnconfigure(1, weight=1)

        message = Label(self, text="Statistics", font=24)
        message.place(x=self.app.WIDTH / 2, y=12, anchor=CENTER)

        nbooks_label = Label(self, text=f"Total Number Of Books: {report['nBooks']}", font=18)
        nbooks_label.place(x=5, y=50, anchor="w")

        nstudents_label = Label(self, text=f"Total Number Of Students: {report['nStudents']}", font=18)
        nstudents_label.place(x=5, y=100, anchor="w")

        genre_table_header_label = Label(self,
                                         text=f"Genre: Number Of books of that genre",
                                         font=18)
        genre_table_header_label.place(x=5, y=150, anchor="w")

        number_of_spaces_in_tables = 40

        genreList = tk.Listbox(self.app, width=number_of_spaces_in_tables + 20, font=18, height=6)
        for i in report["nBooksForEveryGenre"]:
            first_part = str(i[0]) + ": "
            line_content = first_part + str(i[1])
            genreList.insert(tk.END, line_content)
        genreList.place(x=5, y=240, anchor="w")



        language_table_header_label = Label(self,
                                            text=f"Langue: Number Of books of that Languge",
                                            font=18)
        language_table_header_label.place(x=5, y=370, anchor="w")

        genreList = tk.Listbox(self.app, width=number_of_spaces_in_tables + 20, font=18, height=6)
        for i in report["nBooksForEveryLang"]:
            first_part = str(i[0]) + ": "
            line_content = first_part + str(i[1])
            genreList.insert(tk.END, line_content)
        genreList.place(x=5, y=470, anchor="w")


