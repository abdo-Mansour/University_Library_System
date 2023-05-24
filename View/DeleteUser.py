from tkinter import ttk
from tkinter.messagebox import showinfo
from Controller.Controller import Controller

class DeleteUser(ttk.Frame):
    def __init__(self, parent, app, controller: Controller):
        ttk.Frame.__init__(self, parent)
        self.style = ttk.Style(self)
        self.controller = controller
        self.app = app

        # Widgets
        label_title = ttk.Label(self, text="Delete User", font=("Helvetica", 20, 'bold'))
        label_title.pack(pady=10)

        frame_email = ttk.Frame(self)
        frame_email.pack(pady=10)

        self.entry_email = ttk.Entry(frame_email, width= 40)
        self.entry_email.pack(side="left", padx=10)
        self.entry_email.insert(0, "Email")

        button_frame = ttk.Frame(self)
        button_frame.pack(pady=10)

        button_delete_user = ttk.Button(button_frame, text="Delete User", command=self.delete_user)
        button_delete_user.pack(side="left", padx=10)

        button_back = ttk.Button(button_frame, text="Back", command=lambda: self.app.show_frame("AdminMenu"))
        button_back.pack(side="left", padx=10)

    def delete_user(self):
        email = self.entry_email.get()

        if(not email or email == "Email"):
            showinfo("Invalid Input", "Please fill the field with correct email")
        else:
            if(self.controller.deleteUser(email)):
                showinfo("Success", "User deleted successfully")
            else:
                showinfo("Error", "User not found")

