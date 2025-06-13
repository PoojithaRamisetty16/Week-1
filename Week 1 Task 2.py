import bcrypt

original_password = "AllIsWell"
print(f" Original Password: {original_password}")
hashed_password = bcrypt.hashpw(original_password.encode(), bcrypt.gensalt())
print(f" Hashed Password (to store in DB): {hashed_password.decode()}")
login_password = input("\n Enter your password: ")
if bcrypt.checkpw(login_password.encode(), hashed_password):
    print(" Password is correct! Access granted.")
else:
    print(" Password is incorrect! Access denied.")
