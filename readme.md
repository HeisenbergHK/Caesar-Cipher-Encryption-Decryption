# Caesar Cipher Encryption/Decryption

This project implements the classic **Caesar Cipher** encryption and decryption method in Python. The Caesar Cipher is a type of substitution cipher where each letter in the plaintext is "shifted" by a certain number of positions down the alphabet.

## Features
- **Encryption**: Encrypt a message by shifting each letter by a user-specified number of positions.
- **Decryption**: Decrypt a message by reversing the shift applied during encryption.
- **Brute-Force Decryption**: Try all possible shifts (0-25) and output all possible decrypted messages. This helps in breaking the cipher if the shift is unknown.

## Usage

The program offers a simple menu to choose between encryption, decryption, and brute-force decryption:
1. Encrypt
2. Decrypt
3. Brute-force Decryption

### Encryption

1. Select option `1) Encrypt`.
2. Enter a shift value (positive integer).
3. Enter the message you want to encrypt.
4. The program will output the encrypted message.

### Decryption

1. Select option `2) Decrypt`.
2. Enter the same shift value used for encryption.
3. Enter the encrypted message.
4. The program will output the original message (decrypted).

### Brute-Force Decryption

1. Select option `3) Brute-force Decryption`.
2. Enter the encrypted message.
3. The program will try all possible shift values (0-25) and output the decrypted messages for each.

## Example

**Encryption Example:**

1. Select option `1`.
2. Enter shift value: `3`.
3. Enter the message: `Hello World!`.
4. Encrypted message: `Khoor Zruog!`.

**Decryption Example:**

1. Select option `2`.
2. Enter shift value: `3`
3. Enter encrypted message: `Khoor Zruog!`
4. Decrypted message: `Hello World!`

**Brute-Force Example:**

1. Select option `3`.
2. Enter encrypted message: `Khoor Zruog!`

Caesar decryption with shift value 0:
`Khoor Zruog!`

Caesar decryption with shift value 1:
`Jgnnq Yqtwnf!`

Caesar decryption with shift value 2:
`Ifmmp Xpsme!`

…

## Error Handling

- The program ensures that the user enters a valid menu option (1, 2, or 3). If an invalid option is entered, an error message is shown.
- It validates that the shift value is a non-negative integer.
- The program gracefully handles `ValueError` exceptions when the user provides invalid input.

## Running the Program

Simply run the script:

```bash
python caesar_cipher.py
```

The program will then display the menu and guide you through the encryption, decryption, or brute-force decryption process.

## How it Works

* Encryption: Each letter in the message is shifted by the given number of positions. The shift wraps around the alphabet (so a shift of 3 turns ‘Z’ into ‘C’).

* Decryption: The process is reversed by shifting in the opposite direction (i.e., subtracting the shift value).

* Brute-force: Attempts all possible shifts to decrypt a message without knowing the original shift value.
