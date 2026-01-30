import hashlib

target_password = "1234"

target_hash = hashlib.sha256(target_password.encode()).hexdigest()

print("[+] Target Hash:", target_hash)
print("[+] Starting Brute Force Attack...")

for i in range(10000):
    attempt = str(i).zfill(4)
    attempt_hash = hashlib.sha256(attempt.encode()).hexdigest()

    if attempt_hash == target_hash:
        print("[✔] Password Cracked:", attempt)
        break
    else:
        print("Trying:", attempt)