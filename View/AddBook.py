
import tkinter as tk
from tkinter import ttk


class AddBook(ttk.Frame):
    def __init__(self, parent, controller):
        print("AddBook.__init__")
        ttk.Frame.__init__(self, parent)
        self.style = ttk.Style(self)
        self.controller = controller
        

        #widgets
        
  
       