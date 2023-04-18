import tkinter as tk

class PasswordsWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        
        self.title("PasswordsWindow")
        self.geometry("200x150")