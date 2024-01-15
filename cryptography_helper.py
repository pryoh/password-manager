from cryptography.fernet import Fernet

class PasswordManager:
    def __init__(self):
        self.key = None
        self.password_dict = {}

    def create_key(self):
        self.key = Fernet.generate_key()

    def load_key(self, path):
        with open(path, 'rb') as f:
            self.key = f.read()

    def create_password_file(self, path):
        with open(path, 'w') as f:
            f.write("")

    def load_password_file(self, path):
        with open(path, 'r') as f:
            for line in f:
                site, encrypted = line.split(":")
                self.password_dict[site] = encrypted.strip()

    def add_password(self, site, password):
        if self.key:
            encrypted = Fernet(self.key).encrypt(password.encode()).decode()
            self.password_dict[site] = encrypted
        else:
            print("Error: Key not set. Please create or load a key.")

    def get_password(self, site):
        if site in self.password_dict:
            return Fernet(self.key).decrypt(self.password_dict[site].encode()).decode()
        else:
            return None
