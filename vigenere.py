def vigenere_encrypt(text, key):
    result = []
    key = key.lower()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')

            if char.isupper():
                new_char = chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                new_char = chr((ord(char) - 97 + shift) % 26 + 97)

            result.append(new_char)
            key_index += 1
        else:
            result.append(char)

    return ''.join(result)


text = input("Enter message: ")
key = input("Enter key: ")

encrypted = vigenere_encrypt(text, key)
print("Encrypted message:", encrypted)
