
import tkinter as tk
from tkinter import ttk


class AddUser(ttk.Frame):
    def __init__(self, parent, controller):
        print("AddUser.__init__")
        ttk.Frame.__init__(self, parent)
        self.style = ttk.Style(self)
        self.controller = controller
        

        #widgets
        
  
       