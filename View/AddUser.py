import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from Controller.Controller import Controller

class AddUser(ttk.Frame):
    def __init__(self, parent, app, controller: Controller):
        ttk.Frame.__init__(self, parent)
        self.style = ttk.Style(self)
        self.Controller = controller
        self.app = app

        # Widgets
        label_title = ttk.Label(self, text="Add User", font=("Helvetica", 20, 'bold'))
        label_title.pack(pady=10)

        frame_name = ttk.Frame(self)
        frame_name.pack(pady=10)

        self.entry_first_name = ttk.Entry(frame_name)
        self.entry_first_name.pack(side="left", padx=10)
        self.entry_first_name.insert(0, "First Name")

        self.entry_last_name = ttk.Entry(frame_name)
        self.entry_last_name.pack(side="left", padx=10)
        self.entry_last_name.insert(0, "Last Name")

        frame_email_password = ttk.Frame(self)
        frame_email_password.pack(pady=10)

        self.entry_email = ttk.Entry(frame_email_password, width=35)
        self.entry_email.pack(side="left", padx=10)
        self.entry_email.insert(0, "Email")

        self.entry_password = ttk.Entry(frame_email_password)
        self.entry_password.pack(side="left", padx=10)
        self.entry_password.insert(0, "Password")

        frame_phone_dob_gender = ttk.Frame(self)
        frame_phone_dob_gender.pack(pady=10)

        self.entry_phone = ttk.Entry(frame_phone_dob_gender)
        self.entry_phone.pack(side="left", padx=10)
        self.entry_phone.insert(0, "Phone Number")

        self.entry_dob = ttk.Entry(frame_phone_dob_gender)
        self.entry_dob.pack(side="left", padx=10)
        self.entry_dob.insert(0, "Date of Birth")

        label_gender = ttk.Label(frame_phone_dob_gender, text="Gender")
        label_gender.pack(side="left", padx=10)

        self.gender_var = tk.StringVar()
        self.gender_var.set("")  # Default gender selection

        gender_options = ["", "Male", "Female"]
        self.gender_dropdown = ttk.OptionMenu(frame_phone_dob_gender, self.gender_var, *gender_options)
        self.gender_dropdown.pack(side="left", padx=10)

        frame_admin = ttk.Frame(self)
        frame_admin.pack(pady=10)

        self.admin_var = tk.IntVar()
        self.admin_checkbox = ttk.Checkbutton(frame_admin, text="Admin", variable=self.admin_var)
        self.admin_checkbox.pack()

        button_frame = ttk.Frame(self)
        button_frame.pack(pady=10)
        
        button_add_user = ttk.Button(button_frame, text="Add User", command=self.add_user)
        button_add_user.pack(side="left", padx=10)

        button_back = ttk.Button(button_frame, text="Back", command=lambda: self.app.show_frame("AdminMenu"))
        button_back.pack(side="left", padx=10)


    def add_user(self):
        # Get the input values
        first_name = self.entry_first_name.get()
        last_name = self.entry_last_name.get()
        email = self.entry_email.get()
        password = self.entry_password.get()
        phone_number = self.entry_phone.get()
        dob = self.entry_dob.get()
        gender = self.gender_var.get()
        admin = self.admin_var.get()

        # Check if any of the values are empty or equal to their placeholder values
        if (not first_name or first_name == "First Name" or
            not last_name or last_name == "Last Name" or
            not email or email == "Email" or
            not password or password == "Password" or
            not phone_number or phone_number == "Phone Number" or
            not dob or dob == "Date of Birth" or
            not gender or gender == ""
        ):
            showinfo("Invalid Input", "Please fill all fields with correct values")
            return
        
        gender = 0 if gender == 'Male' else 1;

        data = [first_name, last_name, phone_number, dob, gender, admin, email, password]
        
        if self.Controller.addUser(data):
            showinfo("Success", "User added successfully")
            self.go_back()
        else:
            showinfo("Error", "Something went wrong")
