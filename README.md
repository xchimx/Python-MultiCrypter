<p align="center">
<a href="https://github.com/xchimx/Python-MultiCrypter/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-brightgreen.svg" alt="License"></a>
</p>

## About MultiCrypter

MultiCrypter consists of two Python scripts (`MultiCrypt.py` and `MultiDecrypt.py`) that allow you to encrypt and decrypt a python file using multiple passwords. The decrypt works with any of these passwords and extract, run the file in the memory, marked with the entered password. It uses the following libraries and modules:

- **[cryptography](https://cryptography.io/en/latest/)** for cryptographic primitives:
  - `Fernet` for symmetric encryption/decryption
  - `PBKDF2HMAC` for deriving keys from passwords
- **[base64](https://docs.python.org/3/library/base64.html)** for encoding binary data
- **[os](https://docs.python.org/3/library/os.html)** for generating random salts
- **[hashes](https://cryptography.io/en/latest/hazmat/primitives/cryptographic-hashes/)** from the `cryptography.hazmat.primitives` package
- **[default_backend](https://cryptography.io/en/latest/hazmat/backends/)** to specify the cryptographic backend

## How It Works

1. **Encryption** (`CryptMulti.py`)
   - Prompts you for a file path to the source code you want to encrypt.
   - Uses three different passwords (e.g., `12345A`, `12345B`, `12345C` - you can choose them by yourself) to encrypt the code in segments.
   - Saves the combined encrypted data as `encrypted_code.bin`.

2. **Decryption** (`DecryptMulti.py`)
   - Reads the `encrypted_code.bin` file.
   - Asks for a password.
   - Attempts to decrypt each segment in turn using the provided password:
     - If decryption is successful, it prints and optionally writes the decrypted code to `extract.py`.
     - Executes the decrypted code via `exec()`.
     - If no segment can be decrypted with the given password, it prints an error message.

## Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/xchimx/Python-MultiCrypter
   cd Python-MultiCrypter
   pip install -r requirements.txt
   py ./MultiCrypt.py to crypt the python file (try the HelloWorld.py example in Testfile subdir
   py ./MultiDecrypt.py to decrypt the python file with one of the passwords
   
   
## Contributing

Thank you for considering contributing to URLTest! Pull requests, issue reports, and suggestions are highly appreciated. For major changes, please open an issue first to discuss what you would like to change.

## Code of Conduct

In order to keep a welcoming environment, please adhere to a basic code of conduct when interacting in this repository (polite language, respect for others, etc.).

## Security Vulnerabilities

If you discover a security vulnerability within URLTest, please open a GitHub issue or contact the repository owner directly. We’ll address vulnerabilities promptly.

## License
MultiCrypter is open-sourced software licensed under the MIT license.

