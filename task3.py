import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        # Initialize variables
        self.password_length = tk.IntVar(value=12)
        self.use_lowercase = tk.BooleanVar(value=True)
        self.use_uppercase = tk.BooleanVar(value=True)
        self.use_digits = tk.BooleanVar(value=True)
        self.use_special_chars = tk.BooleanVar(value=True)
        self.generated_password = tk.StringVar(value="")
        self.password_strength = tk.StringVar(value="Weak")
        self.password_history = []

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Password Length
        label_length = tk.Label(self.root, text="Password Length:")
        label_length.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        entry_length = tk.Entry(self.root, textvariable=self.password_length)
        entry_length.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        # Character Sets
        checkbox_lowercase = tk.Checkbutton(self.root, text="Lowercase Letters", variable=self.use_lowercase)
        checkbox_lowercase.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        checkbox_uppercase = tk.Checkbutton(self.root, text="Uppercase Letters", variable=self.use_uppercase)
        checkbox_uppercase.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        checkbox_digits = tk.Checkbutton(self.root, text="Digits", variable=self.use_digits)
        checkbox_digits.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        checkbox_special_chars = tk.Checkbutton(self.root, text="Special Characters", variable=self.use_special_chars)
        checkbox_special_chars.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        # Generate Password Button
        button_generate = tk.Button(self.root, text="Generate Password", command=self.generate_password)
        button_generate.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # Generated Password Display
        label_result = tk.Label(self.root, text="Generated Password:")
        label_result.grid(row=6, column=0, padx=10, pady=5, sticky="w")
        entry_result = tk.Entry(self.root, textvariable=self.generated_password, state="readonly")
        entry_result.grid(row=6, column=1, padx=10, pady=5, sticky="w")

        # Password Strength Indicator
        label_strength = tk.Label(self.root, text="Password Strength:")
        label_strength.grid(row=7, column=0, padx=10, pady=5, sticky="w")
        label_strength_value = tk.Label(self.root, textvariable=self.password_strength)
        label_strength_value.grid(row=7, column=1, padx=10, pady=5, sticky="w")

    def generate_password(self):
        password_length = self.password_length.get()

        if password_length <= 0:
            messagebox.showerror("Error", "Please enter a valid password length.")
            return

        character_sets = ""
        if self.use_lowercase.get():
            character_sets += string.ascii_lowercase
        if self.use_uppercase.get():
            character_sets += string.ascii_uppercase
        if self.use_digits.get():
            character_sets += string.digits
        if self.use_special_chars.get():
            character_sets += string.punctuation

        if not character_sets:
            messagebox.showerror("Error", "Please select at least one character set.")
            return

        generated_password = ''.join(random.choice(character_sets) for _ in range(password_length))
        self.generated_password.set(generated_password)
        self.password_history.append(generated_password)
        self.update_password_strength()
        self.update_password_history()

    def update_password_strength(self):
        password_length = len(self.generated_password.get())
        if password_length <= 8:
            self.password_strength.set("Weak")
        elif 8 < password_length <= 12:
            self.password_strength.set("Moderate")
        else:
            self.password_strength.set("Strong")

    def update_password_history(self):
        pass

# Create main application window
root = tk.Tk()
app = PasswordGeneratorApp(root)
root.mainloop()
