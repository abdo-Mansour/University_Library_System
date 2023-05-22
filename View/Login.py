from customtkinter import CTkFrame,  CTkButton, CTkLabel
import customtkinter as ctk
import tkinter.messagebox as tkmb
class Login(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.pack()


        self.label = ctk.CTkLabel(parent,text="Welcome To FCAI Library System",font=("Arial",30,"bold"))
  
        self.label.pack(pady=0)
        
        
        self.frame = ctk.CTkFrame(master=parent)
        self.frame.pack(pady=20,padx=40,fill='both')
        
        self.label = ctk.CTkLabel(master=self.frame,text='Please Enter Your Email and Password',font=("Arial",20,'bold'))
        self.label.pack(pady=40,padx=10)
        
        
        user_entry= ctk.CTkEntry(master=self.frame,width=300 , height= 40 ,placeholder_text="Email",font=("Arial",20))
        user_entry.pack(pady=12,padx=10)
        
        user_pass= ctk.CTkEntry(master=self.frame,width=300 , height= 40 ,placeholder_text="Password",font=("Arial",20),show="*")
        user_pass.pack(pady=12,padx=10)
        
        
        button = ctk.CTkButton(master=self.frame,text='Login',font=("Arial",20,"bold"),command=login)
        button.pack(pady=22,padx=10)
        
        checkbox = ctk.CTkCheckBox(master=self.frame,text='Login as Admin',font=("Arial",20))
        checkbox.pack(pady=22,padx=10)

    def button_callbck(self):
        self.controller.show_frame("Home")
    
    def on_show(self):
        print("Login frame is shown")
        
# # Selecting GUI theme - dark, light , system (for system default)
# ctk.set_appearance_mode("dark")
  
# # Selecting color theme - blue, green, dark-blue
# ctk.set_default_color_theme("dark-blue")
  
# app = ctk.CTk()
# app.geometry("1000x580")
# app.title("Library System")
  
  

