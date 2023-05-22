
import tkinter as tk
from tkinter import ttk


class Browse(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.style = ttk.Style(self)
        self.controller = controller
        

        #widgets
        
  
       