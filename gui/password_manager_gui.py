import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
from cryptography_helper import PasswordManager
from cryptography.fernet import Fernet

class PasswordManagerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Password Manager")

        self.password_manager = PasswordManager()

        self.label = tk.Label(master, text="Welcome to Password Manager!")
        self.label.pack()

        self.button_create_key = tk.Button(master, text="Create New Key", command=self.create_key)
        self.button_create_key.pack()

        self.button_load_key = tk.Button(master, text="Load Key", command=self.load_key)
        self.button_load_key.pack()

        self.button_create_password_file = tk.Button(master, text="Create Password File", command=self.create_password_file)
        self.button_create_password_file.pack()

        self.button_load_password_file = tk.Button(master, text="Load Password File", command=self.load_password_file)
        self.button_load_password_file.pack()

        self.button_add_password = tk.Button(master, text="Add Password", command=self.add_password)
        self.button_add_password.pack()

        self.button_get_password = tk.Button(master, text="Get Password", command=self.get_password)
        self.button_get_password.pack()

        self.button_quit = tk.Button(master, text="Quit", command=master.quit)
        self.button_quit.pack()

    def create_key(self):
        self.password_manager.create_key()
        messagebox.showinfo("Info", "Key created successfully!")

    def load_key(self):
        key_path = filedialog.askopenfilename(filetypes=[("Key Files", "*.key")])
        if key_path:
            self.password_manager.load_key(key_path)
            messagebox.showinfo("Info", "Key loaded successfully!")

    def create_password_file(self):
        path = filedialog.asksaveasfilename(defaultextension=".pass", filetypes=[("Password Files", "*.pass")])
        if path:
            self.password_manager.create_password_file(path)
            messagebox.showinfo("Info", f"Password file created at {path}")

    def load_password_file(self):
        path = filedialog.askopenfilename(filetypes=[("Password Files", "*.pass")])
        if path:
            self.password_manager.load_password_file(path)
            messagebox.showinfo("Info", f"Password file loaded successfully!")

    def add_password(self):
        site = simpledialog.askstring("Add Password", "Enter the site:")
        if site:
            password = simpledialog.askstring("Add Password", "Enter the password:")
            if password:
                self.password_manager.add_password(site, password)
                messagebox.showinfo("Info", f"Password for {site} added successfully!")

    def get_password(self):
        site = simpledialog.askstring("Get Password", "Enter the site:")
        if site:
            password = self.password_manager.get_password(site)
            if password:
                messagebox.showinfo("Info", f"Password for {site} is {password}")
            else:
                messagebox.showwarning("Warning", f"No password found for {site}")

# ... (rest of the code remains unchanged) ...
