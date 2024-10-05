def encrypt_caesar(message, shift):
    encrypted_message = []
    for char in message:
        if char.isupper():
            encrypted_message.append(chr(((ord(char) + shift - 65) % 26) + 65))
        elif char.islower():
            encrypted_message.append(chr(((ord(char) + shift - 97) % 26) + 97))
        else:
            encrypted_message.append(char)
    return "".join(encrypted_message)

def decrypt_caesar(message, shift):
    decrypted_message = []
    for char in message:
        if char.isupper():
            decrypted_message.append(chr(((ord(char) - shift - 65) % 26) + 65))
        elif char.islower():
            decrypted_message.append(chr(((ord(char) - shift - 97) % 26) + 97))
        else:
            decrypted_message.append(char)
    return "".join(decrypted_message)

def brute_force_decrypt_caesar(message):
    decrypted_messages = {}
    for i in range(26):
        temp_decrypted_message = []
        for char in message:
            if char.isupper():
                temp_decrypted_message.append(chr(((ord(char) - i - 65) % 26) + 65))
            elif char.islower():
                temp_decrypted_message.append(chr(((ord(char) - i - 97) % 26) + 97))
            else:
                temp_decrypted_message.append(char)
        decrypted_messages[i] = "".join(temp_decrypted_message)
    return decrypted_messages

def main():
    try:
        print("1) Encrypt")
        print("2) Decrypt")
        print("3) Brute-force Decryption")
        menu_number = int(input("--> "))

        if menu_number not in [1, 2, 3]:
            raise ValueError("Invalid menu option. Please select 1, 2, or 3.")

        if menu_number == 1:
            shift_value = int(input("Enter shift value: "))
            if shift_value < 0:
                raise ValueError("Shift value cannot be negative.")
            message = input("Enter the message: ")
            print("Encrypted message:")
            print(encrypt_caesar(message=message, shift=shift_value))
        
        elif menu_number == 2:
            shift_value = int(input("Enter shift value: "))
            if shift_value < 0:
                raise ValueError("Shift value cannot be negative.")
            message = input("Enter encrypted message: ")
            print("Decrypted message:")
            print(decrypt_caesar(message=message, shift=shift_value))
        
        elif menu_number == 3:
            message = input("Enter encrypted message: ")
            decrypted_messages = brute_force_decrypt_caesar(message=message)
            for key, value in decrypted_messages.items():
                print(f"Caesar decryption with shift value {key}:")
                print(value)
                print()

    except ValueError as e:
        print(f"Error: {e}")
        
if __name__ == "__main__":
    main()