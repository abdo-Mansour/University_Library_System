from customtkinter import CTkFrame,  CTkButton, CTkLabel

class Login(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.pack()

        self.label = CTkLabel(self, text="Login", font=controller.title_font)
        self.label.pack(side="top", fill="x", pady=10)

        self.button = CTkButton(self, text="Back to Home", command=self.button_callbck)
        self.button.pack(padx=20, pady=20)

    def button_callbck(self):
        self.controller.show_frame("Home")
    
    def on_show(self):
        print("Login frame is shown")
        

