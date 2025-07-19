# Cyber-Security
Caesar Cipher Application
A simple Python program that allows users to encrypt and decrypt text using the Caesar Cipher algorithm.

📝 Description
This application implements the classic Caesar Cipher, a substitution cipher where each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. It's a basic cryptographic method often used to introduce the concept of encryption.

The program runs in your terminal, providing an interactive menu for encryption, decryption, and exiting the application. It handles uppercase and lowercase English letters, as well as numbers. Other characters (like spaces, punctuation) remain unchanged.

✨ Features
Encryption: Encrypts a given text message using a user-defined shift value.

Decryption: Decrypts an encrypted text message back to its original form using the same shift value.

Interactive Menu: Easy-to-use command-line interface.

Handles Letters & Numbers: Supports encryption/decryption of English alphabet letters (both uppercase and lowercase) and numbers (0-9).

Special Characters Handling: Preserves spaces and special characters.

🚀 Prerequisites
Before you can run this program, you need to have:

Python 3.x installed on your system.

You can download Python from the official website: python.org

💻 How to Run
Save the Code:
Save the provided Python code into a file named caesar_cipher.py (or any other .py extension) on your computer. Ensure it's saved as plain text (not Rich Text Format or any other formatted document).

Open Your Terminal/Command Prompt:

On Windows: Search for cmd or PowerShell in the Start Menu and open it.

On macOS/Linux: Open the Terminal application (usually found in Applications/Utilities on Mac).

Navigate to the Directory:
Use the cd command to change your current directory to where you saved caesar_cipher.py.
For example, if you saved it in your Documents folder:

Bash

cd C:\Users\YourUsername\Documents  # On Windows
cd ~/Documents                      # On macOS/Linux
(Replace YourUsername with your actual username).

Run the Program:
Execute the Python script using the python or python3 command:

Bash

python caesar_cipher.py   # Try this first
# OR
python3 caesar_cipher.py  # If 'python' doesn't work or refers to an older version
🎮 Usage
Once the program is running, you will see an interactive menu:

--- Caesar Cipher Application ---

Choose an operation:
1. Encrypt
2. Decrypt
3. Exit

Enter your choice (number):
To Encrypt:

Enter 1 and press Enter.

You'll be prompted to "Enter your message:". Type your text and press Enter.

Then, "Enter the shift value (integer):". Type a number (e.g., 3) and press Enter.

The encrypted message will be displayed.

To Decrypt:

Enter 2 and press Enter.

You'll be prompted to "Enter your message:". Type the encrypted text and press Enter.

Then, "Enter the shift value (integer):". Type the same shift value that was used for encryption and press Enter.

The decrypted (original) message will be displayed.

To Exit:

Enter 3 and press Enter. The application will close.

📚 About Caesar Cipher
The Caesar cipher is one of the simplest and most widely known encryption techniques. It's a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.
