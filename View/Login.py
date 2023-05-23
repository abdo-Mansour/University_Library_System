
import tkinter as tk

from tkinter import ttk
from tkinter.messagebox import showinfo


class Login(ttk.Frame):
    def __init__(self, parent, app , controller):
        ttk.Frame.__init__(self, parent)
        self.style = ttk.Style(self)
        self.controller = controller
        self.app = app
        print("Login.__init__")
        #styles

        #widgets
        
        self.label = ttk.Label(self,text='Enter Your Email and Password',font=("Helvetica",20,'bold'))
        self.label.grid(row=0, column=0, pady=50, padx=190 , sticky= "nswe")
        
        self.user_entry= ttk.Entry(self,width=30,text="Email",font=("Helvetica",15))
        self.user_entry.grid(row=1, column=0, pady=12, padx=10)
        
        self.user_pass= ttk.Entry(self,width=30,text="Password",show="*",font=("Helvetica",15))
        self.user_pass.grid(row=2, column=0, pady=12, padx=10)
        
        
        button = ttk.Button(self,width=30,text='Login',command=self.login)
        button.grid(row=3, column=0,rowspan=2, pady=50, padx=10, sticky= "ns")
        
        self.checkbox = ttk.Checkbutton(self,text='Login as Admin')
        self.checkbox.state()
        self.checkbox.grid(row=5, column=0, pady=22, padx=10)
    
    def login(self):
        email = self.user_entry.get()
        password = self.user_pass.get()
        isAdmin = self.checkbox.instate(['selected'])
        #print(isAdmin)
        if(self.controller.login(email,password,isAdmin)):
            showinfo("Login Successful","Welcome to the Library System")
            # self.app.show_frame("")
        else:
            showinfo("Login Failed","Invalid Email or Password")


       