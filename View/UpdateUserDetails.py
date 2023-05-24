import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from Controller.Controller import Controller

class UpdateUserDetails(ttk.Frame):
    def __init__(self, parent, app, controller: Controller):
        ttk.Frame.__init__(self, parent)
        self.style = ttk.Style(self)
        self.controller = controller
        self.app = app

        # show User info
        self.show_info_label = ttk.Label(
            self, text='Update User Details', font=("Helvetica", 18, 'bold'), anchor="center")
        self.show_info_label.grid(
            row=0, column=0, columnspan=2,padx=(280), pady=10, sticky='we')

        self.user_info_entries = {}

        if(self.controller.Person != None):
            self.create_user_info_table()
            self.ShowUserInfo()

        ttk.Button(self, text="Save Changes", command=self.save_changes).grid(
            row=15, column=0, padx=(220,5), pady=20, sticky=tk.W)

        ttk.Button(self, text="Back", command=self.back).grid(
            row=15, column=1, padx=5, pady=20, sticky=tk.W)

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

        user_details = self.controller.getUserDetails()
        user_id = user_details['id']
        user_isAdmin = user_details['isAdmin']
        row = 1
        for key, label_text in user_info_labels.items():
            ttk.Label(self, text=label_text, font=("Helvetica", 14, 'bold')).grid(
                row=row, column=0, padx=(210,10), pady=5, sticky=tk.W)
            entry = ttk.Entry(self, width=30)

            if key == "ID":
                entry.insert(0, user_id)
                entry.config(state="disabled")
            if key == "isAdmin":
                value = "Yes" if user_isAdmin == 1 else "No"
                entry.insert(0, value)
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
                sex_text = "Male" if sex_value == 0 else "Female"
                entry.insert(0, sex_text)
            
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
                    updated_details.append(0)
                else:
                    updated_details.append(1)
            elif key == "isAdmin":
                if entry.get() == "Yes":
                    updated_details.append(1)
                else:
                    updated_details.append(0)
            else:
                updated_details.append(entry.get())

        # Call the controller function to save the updated details
        if(self.controller.updateUserDetails(updated_details)):
            self.app.frames["Report"].refresh_report()
            showinfo("Success", "User details updated successfully")
        else:
            showinfo("Error", "Failed to update user details")

    def back(self):
        if self.controller.isAdmin:
            command = self.app.show_frame("AdminMenu")
        else:
            command = self.app.show_frame("StudentMenu")
