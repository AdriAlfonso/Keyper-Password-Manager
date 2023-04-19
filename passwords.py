import tkinter as tk

class PasswordsWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        
        self.title("PasswordsWindow")
        self.geometry("300x200")

        # Passwords data
        self.passwords = {
            "Instagram": "abc123",
            "Facebook": "123avf",
            "Twitter": "qwerty",
            "Gmail": "password123"
        }

        # Widget Text (show the passwords)
        self.text_widget = tk.Text(self)
        self.text_widget.pack(expand=True, fill='both')

        # Fill the widget text with passwords data
        for service, password in self.passwords.items():
            self.text_widget.insert('end', f"{service}: {password}\n")
