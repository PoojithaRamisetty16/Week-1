from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)
original_message = "Hello, LearnCorp"
print(f"Original Message: {original_message}")
encrypted_message = cipher.encrypt(original_message.encode())
print(f"Encrypted Message: {encrypted_message}")
decrypted_message = cipher.decrypt(encrypted_message).decode()
print(f"Decrypted Message: {decrypted_message}")
if original_message == decrypted_message:
    print("Decryption successful: Messages match!")
else:
    print("Decryption failed: Messages do not match.")
