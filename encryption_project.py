def caesar_encrypt(text, shift):
    encrypted = ""

    for char in text:
        if char.isalpha():
            encrypted += chr((ord(char.upper()) - 65 + shift) % 26 + 65)
        else:
            encrypted += char

    return encrypted


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


password = "Summer2026!"

encrypted = caesar_encrypt(password, 3)

print("Original:", password)
print("Encrypted:", encrypted)
print("Decrypted:", caesar_decrypt(encrypted, 3))
