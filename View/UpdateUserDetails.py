import tkinter as tk
from tkinter import ttk


class UpdateUserDetails(ttk.Frame):
    def __init__(self, parent, app, controller):
        ttk.Frame.__init__(self, parent)
        self.style = ttk.Style(self)
        self.controller = controller
        self.app = app

        # show User info
        self.show_info_label = ttk.Label(
            self, text='Update User Details', font=("Helvetica", 18, 'bold'), anchor="center")
        self.show_info_label.grid(
            row=0, column=0, columnspan=2, pady=10, sticky='we')

        self.user_info_entries = {}
        self.create_user_info_table()

        ttk.Button(self, text="Save Changes", command=self.save_changes).grid(
            row=15, column=0, padx=5, pady=20, sticky=tk.E)

        ttk.Button(self, text="Back", command=self.back).grid(
            row=15, column=1, padx=5, pady=20, sticky=tk.W)

        self.ShowUserInfo()

    def create_user_info_table(self):
        user_info_labels = {
            "ID": "ID",
            "firstName": "First Name",
            "lastName": "Last Name",
            "number": "Number",
            "dob": "DOB",
            "sex": "Sex",
            "isAdmin": "Is Admin",
            "email": "Email",
            "password": "Password"
        }

        row = 1
        for key, label_text in user_info_labels.items():
            ttk.Label(self, text=label_text, font=("Helvetica", 14, 'bold')).grid(
                row=row, column=0, padx=10, pady=5, sticky=tk.W)
            entry = ttk.Entry(self, width=30)

            if key == "ID":
                self.controller.login(
                    "user3@example.com", "02829fb05c3076ec5a6caebd12477dec", 0)
                user_details = self.controller.getUserDetails()
                user_id = user_details['id']

                entry.insert(0, user_id)
                entry.config(state="disabled")

            entry.grid(row=row, column=1, padx=10, pady=5, sticky=tk.W)
            self.user_info_entries[key] = entry
            row += 1

    def ShowUserInfo(self):
        user_details = self.controller.getUserDetails()

        # Insert the user details into the entry fields
        for key, entry in self.user_info_entries.items():
            entry.delete(0, tk.END)
            if key == "sex":
                sex_value = user_details.get(key, "")
                sex_text = "Male" if sex_value == 1 else "Female"
                entry.insert(0, sex_text)
            elif key == "isAdmin":
                value = "Yes" if user_details.get(key, 0) == 1 else "No"
                entry.insert(0, value)
            elif key == "ID":
                entry.insert(0, user_details.get(key, ""))
            else:
                entry.insert(0, user_details.get(key, ""))

    def save_changes(self):
        updated_details = []

        user_details = self.controller.getUserDetails()
        user_id = user_details['id']

        for key, entry in self.user_info_entries.items():
            if key == "ID":
                updated_details.append(user_id)
            elif key == "sex":
                if entry.get() == "Male":
                    updated_details.append(1)
                else:
                    updated_details.append(0)
            elif key == "isAdmin":
                if entry.get() == "Yes":
                    updated_details.append(1)
                else:
                    updated_details.append(0)
            else:
                updated_details.append(entry.get())

        print("Printing Updated List")
        for value in updated_details:
            print(value)
        # Call the controller function to save the updated details
        self.controller.updateUserDetails(updated_details)

    def back(self):
        if self.controller.isAdmin:
            command = self.app.show_frame("AdminMenu")
        else:
            command = self.app.show_frame("StudentMenu")
