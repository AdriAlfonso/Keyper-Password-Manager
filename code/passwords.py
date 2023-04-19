import tkinter as tk

# Change the path
FILENAME = "C:/Users/adria/OneDrive/Escritorio/Keyper/code/example.txt"

class PasswordsWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        
        self.title("PasswordsWindow")
        self.geometry("250x450")
        
        # The user cannot resize the window
        self.resizable(False, False)

        # Passwords data
        self.passwords = {}

        # Read passwords from file
        self.read_passwords_from_file()

        # Text widget (show the passwords)
        self.text_widget = tk.Text(self)
        self.text_widget.pack(expand=True, fill='both')

        # Fill the Text widget with passwords data
        for service, password in self.passwords.items():
            self.text_widget.insert('end', f"{service}: {password}\n")

        # Save button
        self.save_button = tk.Button(self, text="Save", command=self.save_passwords)
        self.save_button.pack(side='bottom', fill = 'x',  padx=10, pady=10)

    def read_passwords_from_file(self):
        global FILENAME
        with open(FILENAME, "r") as f:
            for line in f:
                line = line.strip()  # Remove whitespace and newline characters
                if line:  
                    service, password = line.split(":")
                    service = service.strip().strip('"')
                    password = password.strip().strip('"')
                    self.passwords[service] = password

    def save_passwords(self):
        global FILENAME
        with open(FILENAME, "w") as f:
            # Get the content of the Text Widget
            content = self.text_widget.get("1.0", "end").strip()

            # Split the lines of the Text Widget
            lines = content.splitlines()

            # Write each line in the .txt
            for line in lines:
                f.write(line + "\n")

