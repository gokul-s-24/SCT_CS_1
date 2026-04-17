def encrypt(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  
    
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


print("=== Caesar Cipher Program ===")

message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()

if choice == 'e':
    encrypted = encrypt(message, shift)
    print("Encrypted Message:", encrypted)

elif choice == 'd':
    decrypted = decrypt(message, shift)
    print("Decrypted Message:", decrypted)

else:
    print("Invalid choice!")