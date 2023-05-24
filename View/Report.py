import tkinter
import tkinter as tk

from tkinter import ttk, CENTER, NW, W, LEFT, END
from tkinter.messagebox import showinfo
from tkinter.ttk import Label


class Report(ttk.Frame):
    def __init__(self, parent, app, controller):
        ttk.Frame.__init__(self, parent)
        self.genre_table_header_label = None
        self.nstudents_label = None
        self.nbooks_label = None
        self.report = None
        self.style = ttk.Style(self)
        self.controller = controller
        self.app = app

        # self.report = self.controller.generateStatisticsReport()

        self.message = Label(self, text="Statistics", font=24)
        self.message.place(x=self.app.WIDTH / 2, y=12, anchor=CENTER)

        self.nbooks_label = Label(self, text=f"Total Number Of Books: ", font=18)
        self.nbooks_label.place(x=5, y=50, anchor="w")

        self.nstudents_label = Label(self, text=f"Total Number Of Students: ", font=18)
        self.nstudents_label.place(x=5, y=100, anchor="w")

        self.genre_table_header_label = Label(self,
                                              text=f"Genre: Number Of books of that genre",
                                              font=18)
        self.genre_table_header_label.place(x=5, y=150, anchor="w")

        self.number_of_spaces_in_tables = 40

        self.genreList = tk.Listbox(self, width=self.number_of_spaces_in_tables + 20, font=18, height=6)

        # for i in self.report["nBooksForEveryGenre"]:
        #     first_part = str(i[0]) + ": "
        #     line_content = first_part + str(i[1])
        #     self.genreList.insert(tk.END, line_content)

        self.genreList.place(x=5, y=240, anchor="w")

        language_table_header_label = Label(self,
                                            text=f"Language: Number Of books of that Language",
                                            font=18)
        language_table_header_label.place(x=5, y=370, anchor="w")

        self.language_list = tk.Listbox(self, width=self.number_of_spaces_in_tables + 20, font=18, height=6)

        # for i in self.report["nBooksForEveryLang"]:
        #     first_part = str(i[0]) + ": "
        #     line_content = first_part + str(i[1])
        #     genreList.insert(tk.END, line_content)

        self.language_list.place(x=5, y=470, anchor="w")

        button_back = ttk.Button(self, text="Back", command=self.back)
        button_back.place(x=5, y=550, anchor="w")

    def back(self):
        if self.controller.isAdmin:
            command = self.app.show_frame("AdminMenu")
        else:
            command = self.app.show_frame("StudentMenu")

    def refresh_report(self):
        self.report = self.controller.generateStatisticsReport()
        self.nbooks_label.config(text=f"Total Number Of Books: {self.report['nBooks']}")
        self.nstudents_label.config(text=f"Total Number Of Students: {self.report['nStudents']}", font=18)

        self.genreList.delete(0, END)
        self.language_list.delete(0, END)

        for i in self.report["nBooksForEveryGenre"]:
            first_part = str(i[0]) + ": "
            line_content = first_part + str(i[1])
            self.genreList.insert(tk.END, line_content)

        for i in self.report["nBooksForEveryLang"]:
            first_part = str(i[0]) + ": "
            line_content = first_part + str(i[1])
            self.genreList.insert(tk.END, line_content)
