from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

# Define the key and IV (must be 16 bytes)
key = b'1234567890123456'
iv = b'1234567890123456'

def encrypt_data(data):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_bytes = cipher.encrypt(pad(data.encode(), AES.block_size))  # Pad and encrypt
    return base64.b64encode(encrypted_bytes).decode()  # Convert to Base64 string

def decrypt_data(encrypted_data):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_bytes = unpad(cipher.decrypt(base64.b64decode(encrypted_data)), AES.block_size)  # Decrypt and unpad
    return decrypted_bytes.decode()

# Example usage:
original_text = ""
decrypted_text = decrypt_data(original_text)

print("🔓 Decrypted:", decrypted_text)
