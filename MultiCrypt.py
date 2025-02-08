from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import base64
import os


def encrypt_code(passwords: dict, code: str) -> bytes:
    encrypted_data = b""
    for identifier, password in passwords.items():
        code_with_comment = f'#i was decrypted with {identifier}\n' + code

        salt = os.urandom(16)

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        fernet = Fernet(key)

        encrypted_code = fernet.encrypt(code_with_comment.encode())

        encrypted_data += salt + encrypted_code

    return encrypted_data


file_path = input("Enter the path of the file you want to encrypt: ")

try:
    with open(file_path, "r", encoding="utf-8") as f:
        file_content = f.read()
except FileNotFoundError:
    print("The specified file was not found.")
    exit(1)
except UnicodeDecodeError:
    print("The file contains characters that cannot be decoded with UTF-8.")
    exit(1)

passwords = {
    'A': '12345A',
    'B': '12345B',
    'C': '12345C'
}

encrypted_data = encrypt_code(passwords, file_content)

with open("encrypted_code.bin", "wb") as file:
    file.write(encrypted_data)

print("Encryption complete. Encrypted data saved as 'encrypted_code.bin'.")
