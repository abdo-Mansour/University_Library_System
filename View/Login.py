from tkinter import ttk
from tkinter.messagebox import showinfo


class Login(ttk.Frame):
    def __init__(self, parent, app, controller):
        ttk.Frame.__init__(self, parent)
        self.style = ttk.Style(self)
        self.controller = controller
        self.app = app
        # styles

        # widgets
        welcomeLabel = ttk.Label(self, text='Welcome to the FCAI Library System', font=("Helvetica", 17, 'bold'))
        welcomeLabel.pack(pady= 10, padx=190)

        self.label = ttk.Label(self, text='Login', font=("Helvetica", 18, 'bold'))
        self.label.pack(pady=50, padx=190)

        emailLabel = ttk.Label(self, text='Email:', font=("Helvetica", 15))
        emailLabel.pack(pady=1, padx=230 , anchor="w")
        self.user_entry = ttk.Entry(self, width=30, text="Email", font=("Helvetica", 15))
        self.user_entry.pack(pady=12, padx=10)

        passwordLabel = ttk.Label(self, text='Password:', font=("Helvetica", 15))
        passwordLabel.pack(pady=1, padx=230 , anchor="w")
        self.user_pass = ttk.Entry(self, width=30, text="Password", show="*", font=("Helvetica", 15))
        self.user_pass.pack(pady=12, padx=10)

        button = ttk.Button(self, width=30, text='Login', command=self.login)
        button.pack(pady=50, padx=10)

        self.checkbox = ttk.Checkbutton(self, text='Login as Admin')
        self.checkbox.state()
        self.checkbox.pack(pady=22, padx=10)
    
    def login(self):
        email = self.user_entry.get()
        password = self.user_pass.get()
        isAdmin = self.checkbox.instate(['selected'])

        if(self.controller.login(email,password,isAdmin)):
            # showinfo("Login Successful","Welcome to the Library System")
            # self.app.show_frame("")
            self.app.frames["UpdateUserDetails"].create_user_info_table()
            self.app.frames["UpdateUserDetails"].ShowUserInfo()
            self.app.frames["Browse"].refreshList()
            self.app.frames["Report"].refresh_report()
            if isAdmin:
                self.app.show_frame("AdminMenu")
            else:
                self.app.show_frame("StudentMenu")
        else:
            showinfo("Login Failed","Invalid Email or Password")


       