import hashlib

# Stored password (example)
stored_password = "hello123"

# Convert to hash
stored_hash = hashlib.sha256(stored_password.encode()).hexdigest()

# User input
password = input("Enter password to verify: ")

# Hash user input
input_hash = hashlib.sha256(password.encode()).hexdigest()

# Compare
if input_hash == stored_hash:
    print("[+] Password Matched")
else:
    print("[-] Wrong Password")