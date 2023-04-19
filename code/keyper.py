import tkinter as tk
from tkinter import messagebox
from passwords import PasswordsWindow

class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Set a title and geometry
        self.title("Keyper")
        self.geometry("250x100")
        
        # The user cannot resize the window
        self.resizable(False, False)

        # Creates the password field
        password_label = tk.Label(self, text="Introduce your password:")
        password_label.pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        # Creates the login button
        login_button = tk.Button(self, text="Login", command=self.check_password)
        login_button.pack()

        # The user can login directly with the <Return> button 
        self.bind("<Return>", self.check_password)
    
    def open_passwords_window(self):
        # Creates a new instance of PasswordsWindow and withdraws the Login window
        self.withdraw()
        passwords_window = PasswordsWindow(self)
    
    def check_password(self, event=None):
        password = "mypassword" 
        if password == self.password_entry.get():
            self.open_passwords_window()
        else:
            messagebox.showerror("Access Denied", "Incorrect Password. Try again.")
            self.password_entry.delete(0, tk.END)  # Delete the content of 'password_entry'

# Creates the first instance of Login
loginWindow = Login()
loginWindow.mainloop()