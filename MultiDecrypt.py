from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet, InvalidToken
import base64


def decrypt_and_run(encrypted_data: bytes, password: str):
    salt_size = 16
    encrypted_code_length = 140
    segment_size = salt_size + encrypted_code_length

    position = 0

    while position < len(encrypted_data):
        salt = encrypted_data[position:position + salt_size]
        encrypted_code = encrypted_data[position + salt_size:position + segment_size]
        position += segment_size

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        fernet = Fernet(key)

        try:
            decrypted_code = fernet.decrypt(encrypted_code).decode()
            print("Decrypted code:")
            print(decrypted_code)

            # write the file, can be removed, file will work from memory
            with open("extract.py", "w") as output_file:
                output_file.write(decrypted_code)
            # write the file, can be removed, file will work from memory    

            exec(decrypted_code)
            return
        except InvalidToken:
            continue

    print("Invalid password or no matching encrypted segment.")


with open("encrypted_code.bin", "rb") as file:
    encrypted_data = file.read()

password = input("Enter the password to decrypt and run the script: ")

decrypt_and_run(encrypted_data, password)
