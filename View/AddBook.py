
import tkinter as tk
from tkinter import ttk


class AddBook(ttk.Frame):
    def __init__(self, parent, app , controller):
        ttk.Frame.__init__(self, parent)
        self.style = ttk.Style(self)
        self.controller = controller
        self.app = app
        

        #widgets
        
  
       