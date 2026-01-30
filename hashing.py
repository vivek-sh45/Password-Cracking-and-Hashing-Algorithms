import hashlib

password = input("Enter password: ")

md5 = hashlib.md5(password.encode()).hexdigest()
sha1 = hashlib.sha1(password.encode()).hexdigest()
sha256 = hashlib.sha256(password.encode()).hexdigest()

print("\nMD5 Hash   :", md5)
print("SHA1 Hash  :", sha1)
print("SHA256 Hash:", sha256)