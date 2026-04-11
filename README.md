# Password Cracking and Hashing Algorithms

## Project Overview

This project explores how password hashing works and how weak passwords can be cracked using different attack techniques. The objective is to understand the security risks associated with poor password policies and demonstrate how attackers attempt to recover plaintext passwords from hashed values.

The lab demonstrates password hashing concepts and password cracking techniques commonly studied in cybersecurity.

---

## Lab Environment

Operating System: Kali Linux  
Hardware Configuration:

CPU: 4-core processor  
RAM: 8 GB  

Environment used for performing password hashing analysis and cracking simulations.

---

## Tools Used

- Kali Linux
- John the Ripper
- Hashcat
- Linux terminal utilities

---

## Password Hashing

Password hashing is a security technique used to convert plaintext passwords into encrypted hash values using cryptographic algorithms.

Common hashing algorithms include:

- MD5
- SHA-1
- SHA-256
- SHA-512

Hashing protects passwords by storing them in an irreversible format so attackers cannot easily retrieve the original password.

Example:

```
password123 → 482c811da5d5b4bc6d497ffa98491e38
```

---

## Password Cracking Techniques

Several techniques can be used to recover passwords from hashes.

### Dictionary Attack

This attack uses a predefined list of common passwords and compares their hashes with the target hash.

```
john --wordlist=passwordlist.txt hashes.txt
```

---

### Brute Force Attack

A brute force attack attempts every possible combination of characters until the correct password is found.

```
hashcat -a 3 -m 0 hash.txt ?a?a?a?a?a?a
```

---

### Hybrid Attack

A hybrid attack combines dictionary words with numbers or symbols.

Example:

```
password → password123
```

---

## Password Cracking Process

1. Generated password hashes using hashing algorithms.
2. Stored hashes in a hash file.
3. Used password cracking tools to attempt recovering plaintext passwords.
4. Tested dictionary and brute-force attack techniques.
5. Observed the time taken to crack weak passwords.

---

## Security Risks Observed

The experiment demonstrated several password security weaknesses:

- Weak passwords can be cracked quickly.
- Dictionary attacks are effective against common passwords.
- Short passwords are vulnerable to brute-force attacks.

---

## Results

The analysis showed that poorly chosen passwords can be cracked within seconds or minutes using modern password cracking tools.

This demonstrates the importance of:

- Strong password policies
- Long passwords
- Multi-factor authentication
- Secure hashing algorithms

---

## Skills Demonstrated

- Password Security Analysis
- Hashing Algorithms
- Password Cracking Techniques
- Cybersecurity Threat Analysis
- Linux Security Tools

---

## Learning Outcome

This project provided practical understanding of how password security works and how attackers exploit weak passwords. It highlights the importance of secure authentication practices in modern cybersecurity systems.
