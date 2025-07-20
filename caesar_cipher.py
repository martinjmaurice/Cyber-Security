# File: caesar_cipher.py

# This function is the core of the program; it encrypts or decrypts the text.
def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypts or decrypts text using the Caesar cipher algorithm.

    Parameters:
    text (str): The text to be encrypted or decrypted.
    shift (int): The shift value (an integer).
    mode (str): The operation mode: 'encrypt' for encryption, 'decrypt' for decryption.
                The default value is 'encrypt'.

    Returns:
    str: The resulting text after encryption or decryption.
    """
    result_text = "" # Variable to store the resulting text (encrypted or decrypted)

    # If the mode is 'decrypt', reverse the shift value.
    # This is because decryption is the inverse of encryption.
    if mode == 'decrypt':
        shift = -shift

    # Iterate through each character in the input text
    for char_code in text:
        # 1. Handle lowercase English letters (a-z)
        if 'a' <= char_code <= 'z':
            base_ascii = ord('a') # ASCII value of 'a' (97)
            # Convert the character to a number (0-25), add the shift, apply modulo 26
            # (to ensure the number stays within the alphabetical range), then convert it back to a character.
            result_text += chr((ord(char_code) - base_ascii + shift) % 26 + base_ascii)
        # 2. Handle uppercase English letters (A-Z)
        elif 'A' <= char_code <= 'Z':
            base_ascii = ord('A') # ASCII value of 'A' (65)
            # The same logic used for lowercase letters, but using the ASCII value of 'A'.
            result_text += chr((ord(char_code) - base_ascii + shift) % 26 + base_ascii)
        # 3. Handle digits (0-9)
        elif '0' <= char_code <= '9':
            base_ascii = ord('0') # ASCII value of '0' (48)
            # The same logic, but the range for digits is 10 (0-9).
            result_text += chr((ord(char_code) - base_ascii + shift) % 10 + base_ascii)
        # 4. Handle any other characters (spaces, punctuation, etc.)
        else:
            # Any character that is not an English letter (lowercase or uppercase) or a digit,
            # is kept as is.
            result_text += char_code
    return result_text # Return the resulting text

# This function is the main entry point of the program, interacting with the user.
def main():
    """
    The main function to run the interactive Caesar cipher application.
    It handles user inputs and displays the results.
    """
    print("--- Caesar Cipher Application ---") 

    while True: # Infinite loop to keep the application running until the user chooses to exit
        print("\nChoose an operation:") 
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        user_choice = input("Enter your choice (number): ") 

        # If the user chose 1 (encrypt) or 2 (decrypt)
        if user_choice == '1' or user_choice == '2':
            input_message = input("Enter your message: ") 
            try:
                shift_value = int(input("Enter the shift value (integer): ")) 
            except ValueError:
                # If the user enters something that is not an integer for the shift, display an error message and return to the start of the loop.
                print("Invalid shift value. Please enter an integer.") 
                continue # Go back to the beginning of the while loop

            # Execute the encryption operation if the choice is '1'
            if user_choice == '1':
                encrypted_message = caesar_cipher(input_message, shift_value, 'encrypt')
                print(f"Encrypted message: {encrypted_message}") 
            # Execute the decryption operation if the choice is '2'
            else: # user_choice == '2'
                decrypted_message = caesar_cipher(input_message, shift_value, 'decrypt')
                print(f"Decrypted message: {decrypted_message}")
        # If the user chose 3 (exit)
        elif user_choice == '3':
            print("Thank you for using the application. Goodbye!") 
            break # Break the infinite loop, thus ending the program.
        # If the user enters an invalid choice (not 1, 2, or 3)
        else:
            print("Invalid choice. Please try again.") 

# This condition ensures that the 'main()' function is called only when the file is run directly,
# and not when this file is imported as a module in another Python file.
if __name__ == "__main__":
    main()
