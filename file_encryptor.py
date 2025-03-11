from cryptography.fernet import Fernet
import os

def generate_key(passphrase):
    return Fernet.generate_key()  # Simplified for demo; use passphrase in prod

def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as f:
        data = f.read()
    encrypted = fernet.encrypt(data)
    with open(file_path + ".enc", "wb") as f:
        f.write(encrypted)

def decrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as f:
        data = f.read()
    decrypted = fernet.decrypt(data)
    with open(file_path.replace(".enc", ".dec"), "wb") as f:
        f.write(decrypted)

if __name__ == "__main__":
    key = generate_key("test")  # Replace with user input in practice
    encrypt_file("sample_file.txt", key)
    decrypt_file("sample_file.txt.enc", key)