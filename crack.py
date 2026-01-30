import hashlib

real_password = "vivek123"
target_hash = hashlib.sha256(real_password.encode()).hexdigest()

print("[*] Target Hash:", target_hash)

wordlist = ["1234","12345","password","admin","vivek","vivek123","india123"]

print("\n[*] Starting brute force...\n")

for word in wordlist:
    hashed = hashlib.sha256(word.encode()).hexdigest()
    print("Trying:", word)

    if hashed == target_hash:
        print("\n[+] Password Found:", word)
        break
else:
    print("\n[-] Password not found")