import tkinter as tk

class PasswordsWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        
        self.title("PasswordsWindow")
        self.geometry("250x450")
        
        # The user cannot resize the window
        self.resizable(False, False)

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

        # Save button
        self.save_button = tk.Button(self, text="Save")
        self.save_button.pack(side='bottom', fill = 'x',  padx=10, pady=10)
