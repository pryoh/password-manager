from cryptography.fernet import Fernet

class PasswordManager:
    
    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}
        
    def create_key(self, path):
        try:
            self.key = Fernet.generate_key()
            with open(path, 'wb') as f:
                f.write(self.key)
            print("Key created successfully.")
        except Exception as e:
            print(f"Error creating key: {e}")

    def load_key(self, path):
        try:
            with open(path, 'rb') as f:
                self.key = f.read()
            print("Key loaded successfully.")
        except Exception as e:
            print(f"Error loading key: {e}")

    def encrypt_password(self, password):
        try:
            return Fernet(self.key).encrypt(password.encode()).decode()
        except Exception as e:
            print(f"Error encrypting password: {e}")
            return None

    def decrypt_password(self, encrypted):
        try:
            return Fernet(self.key).decrypt(encrypted.encode()).decode()
        except Exception as e:
            print(f"Error decrypting password: {e}")
            return None

    def create_password_file(self, path, initial_values=None):
        try:
            self.password_file = path

            if initial_values is not None:
                with open(path, 'a') as f:
                    for key, value in initial_values.items():
                        encrypted = self.encrypt_password(value)
                        if encrypted is not None:
                            f.write(f"{key}:{encrypted}\n")

            print("Password file created successfully.")
        except Exception as e:
            print(f"Error creating password file: {e}")

    def load_password(self, path):
        try:
            with open(path, 'r') as f:
                for line in f:
                    site, encrypted = line.strip().split(":")
                    decrypted_password = self.decrypt_password(encrypted)
                    if decrypted_password is not None:
                        self.password_dict[site] = decrypted_password
                        print(f"Loaded password for site {site}")
            print("Passwords loaded successfully.")
        except Exception as e:
            print(f"Error loading passwords: {e}")

    def add_password(self, site, password):
        encrypted = self.encrypt_password(password)
        if encrypted is not None:
            self.password_dict[site] = password
            if self.key is not None:
                try:
                    with open(self.password_file, 'a') as f:
                        f.write(f"{site}:{encrypted}\n")
                    print("Password added successfully.")
                except Exception as e:
                    print(f"Error adding password to file: {e}")
            else:
                print("Error: Key not set. Please create or load a key.")

    def get_password(self, site):
        if self.key is not None:
            return self.password_dict.get(site, "Site not found")
        else:
            print("Error: Key not set. Please create or load a key.")
            return None

def main():
    password = {
        "email": "1234567",
        "facebook": "myfbpassword",
        "youtube": "helloworld123"
    }

    pm = PasswordManager()

    print("""What do you want to do?
    (1) Create a new key
    (2) Load an existing key
    (3) Create new password file
    (4) Load existing password file
    (5) Add a new password
    (6) Get a password
    (q) Quit
    """)

    done = False
    while not done:
        choice = input("Enter your choice:  ")
        try:
            if choice == "1":
                path = input("Enter path: ")
                pm.create_key(path)
            elif choice == "2":
                path = input("Enter path: ")
                pm.load_key(path)
            elif choice == "3":
                path = input("Enter path: ")
                pm.create_password_file(path, password)
            elif choice == "4":
                path = input("Enter path: ")
                pm.load_password(path)
            elif choice == "5":
                site = input("Enter the site: ")
                password = input("Enter the password: ")
                pm.add_password(site, password)
            elif choice == "6":
                site = input("What site do you want: ")
                print(f"Password for {site} is {pm.get_password(site)}")
            elif choice == "q":
                done = True
                print("Bye")
            else:
                print("Invalid choice")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
