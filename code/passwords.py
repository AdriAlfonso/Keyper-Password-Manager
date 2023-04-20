import sqlite3
import tkinter as tk

class PasswordsWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)

        # Set a title and geometry
        self.title("PasswordsWindow")
        self.geometry("250x450")

        # The user cannot resize the window
        self.resizable(False, False)

        # Connect to the database
        self.conn = sqlite3.connect('passwords.db')

        # Create the table if it doesn't exist
        self.create_table()

        # Passwords data
        self.passwords = {}

        # Read passwords from the 'passwords.db'
        self.read_passwords_from_db()

        # Text widget (show the passwords)
        self.text_widget = tk.Text(self)
        self.text_widget.pack(expand=True, fill='both')

        # Fill the Text widget with passwords data
        for service, password in self.passwords.items():
            self.text_widget.insert('end', f"{service}: {password}\n")

        # Save button
        self.save_button = tk.Button(self, text="Save", command=self.save_passwords)
        self.save_button.pack(side='bottom', fill='x', padx=10, pady=10)

    def create_table(self):
        c = self.conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS passwords (
                service TEXT PRIMARY KEY,
                password TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def read_passwords_from_db(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM passwords")
        rows = c.fetchall()
        for row in rows:
            service, password = row
            self.passwords[service] = password

    def save_passwords(self):
        c = self.conn.cursor()

        # Delete all existing passwords
        c.execute("DELETE FROM passwords")

        # Insert the new passwords
        content = self.text_widget.get("1.0", "end").strip()
        lines = content.splitlines()
        for line in lines:
            service, password = line.split(":")
            service = service.strip()
            password = password.strip()
            c.execute("INSERT INTO passwords (service, password) VALUES (?, ?)", (service, password))
        self.conn.commit()
