import hashlib
from cryptography.fernet import Fernet

# Define a class named PasswordManager
class PasswordManager:
    # Constructor: Initialize the PasswordManager 
    # with a master password
    def __init__(self, master_password):
        self.master_password = master_password
        self.passwords = {}
        self.key = self.generate_key()

    # Generate an encryption key based on the master password
    def generate_key(self):
        # Use the master password to generate an encryption 
        # key using PBKDF2
        return hashlib.pbkdf2_hmac('sha256', 
                                   self.master_password
                                   .encode('utf-8'), b'salt', 
                                   100000)

    # Encrypt data using Fernet encryption
    def encrypt(self, data):
        cipher_suite = Fernet(self.key)
        encrypted_data = cipher_suite.encrypt(
            data.encode('utf-8'))
        return encrypted_data

    # Decrypt encrypted data using Fernet encryption
    def decrypt(self, encrypted_data):
        cipher_suite = Fernet(self.key)
        decrypted_data = cipher_suite.decrypt(
            encrypted_data).decode('utf-8')
        return decrypted_data

    # Add a password entry to the passwords dictionary
    def add_password(self, website, username, password):
        encrypted_password = self.encrypt(password)
        self.passwords[website] = {
            'username': username, 
            'password': encrypted_password
        }

    # Retrieve a decrypted password based on the website name
    def get_password(self, website):
        if website in self.passwords:
            encrypted_password = \
                self.passwords[website]['password']
            
            decrypted_password = \
                self.decrypt(encrypted_password)
            return decrypted_password
        else:
            return "Password not found."

    # Return a list of website names stored in the 
    # passwords dictionary
    def list_websites(self):
        return self.passwords.keys()

# Example usage
def main():
    # Get the master password from the user
    master_password = input("Enter your master password: ")
    # Create an instance of PasswordManager with the 
    # master password
    password_manager = PasswordManager(master_password)

    while True:
        # Display a menu for various operations
        print("\n1. Add Password")
        print("2. Get Password")
        print("3. List Websites")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            website = input("Website: ")
            username = input("Username: ")
            password = input("Password: ")
            password_manager.add_password(website, 
                                          username, 
                                          password)
            print("Password added.")

        elif choice == '2':
            website = input("Website: ")
            password = password_manager.get_password(website)
            print(f"Password: {password}")

        elif choice == '3':
            websites = password_manager.list_websites()
            print("Websites:", ', '.join(websites))

        elif choice == '4':
            break

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
