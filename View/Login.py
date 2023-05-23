
import tkinter as tk
from tkinter import ttk


class Login(ttk.Frame):
    def __init__(self, parent, app , controller):
        ttk.Frame.__init__(self, parent)
        self.style = ttk.Style(self)
        self.controller = controller
        self.app = app
        print("Login.__init__")
        #styles

        #widgets
        # self.frame = ttk.Frame(self )
        # # self.frame.grid(row = 0 , column = 0, pady=20,padx=40)
        # # Configure the row and column weights
        # parent.grid_rowconfigure(0, weight=1)
        # parent.grid_columnconfigure(0, weight=1)
        # self.frame.grid(row=0, column=0, pady=20, padx=40 ,sticky= "nswe")
        
        self.label = ttk.Label(self,text='Enter Your Email and Password',font=("Arial",20,'bold'))
        self.label.grid(row=0, column=0, pady=70, padx=275 , sticky= "nswe")
        
        self.user_entry= ttk.Entry(self,width=30,text="Email",font=("Arial",15))
        self.user_entry.grid(row=1, column=0, pady=12, padx=10)
        
        self.user_pass= ttk.Entry(self,width=30,text="Password",show="*",font=("Arial",15))
        self.user_pass.grid(row=2, column=0, pady=12, padx=10)
        
        
        button = ttk.Button(self,width=30,text='Login',command=self.login)
        button.grid(row=3, column=0,rowspan=2, pady=50, padx=10, sticky= "ns")
        
        self.checkbox = ttk.Checkbutton(self,text='Login as Admin')
        self.checkbox.grid(row=5, column=0, pady=22, padx=10)
    
    def login(self):
        pass
       