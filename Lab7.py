# CSC 122
# Substitution Cipher
# By <Ashanti Carpio>
"""
Inputs, Processes, Outputs (IOP)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Input(s):
Processes:
Output(s):
"""


def main():
    # Prompt user for message to encrypt
    message = input("Enter the message to be encrypted: ")

    # Encrypt the message
    encrypted_message = ""
    for char in message:
        encrypted_message += chr(ord(char) + 3)

    # Print the encrypted message
    print(f"Encrypted message = {encrypted_message}\n")

    # Prompt user for cipher to decrypt
    cipher = input("Enter the cipher to be decrypted: ")

    # Decrypt the cipher
    decrypted_message = ""
    for char in cipher:
        decrypted_message += chr(ord(char) - 3)

    # Print the decrypted message
    print(f"Decrypted message = {decrypted_message}\n")


if __name__ == "__main__":
    main()