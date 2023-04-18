import tkinter as tk
from tkinter import messagebox

def check_password(event=None):
    password = "mypassword" 
    if password == password_entry.get():
        # Future commits
        messagebox.showinfo("Login Succesful",  "Welcome to Keyper!")
        pass
    else:
        messagebox.showerror("Access Denied", "Incorrect Password. Try again.")
        password_entry.delete(0, tk.END)  # Delete the content of 'password_entry'

# Creates the TKinter window
root = tk.Tk()
root.title("Keyper") 
root.geometry("250x100")

# Creates the password field
password_label = tk.Label(root, text="Introduce your password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Creates the login button
login_button = tk.Button(root, text="Login", command=check_password)
login_button.pack()

# The user can login directly with the <Return> button 
root.bind("<Return>", check_password)

# Executes the TKinter window
root.mainloop()
