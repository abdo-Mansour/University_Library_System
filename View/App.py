from customtkinter import CTk, CTkButton

class App(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x150")

        self.button = CTkButton(self, text="my button", command=self.button_callbck)
        self.button.pack(padx=20, pady=20)

    def button_callbck(self):
        print("button clicked")

app = App()
app.mainloop()