# 🔐 Password Cracking & Hashing Algorithms

![Language](https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Type](https://img.shields.io/badge/Type-Security%20Research-orange?style=for-the-badge)
![MITRE](https://img.shields.io/badge/MITRE-T1110%20Brute%20Force-red?style=for-the-badge)
![Internship](https://img.shields.io/badge/Internship-Codec%20Technologies-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)

> **Security awareness research project** — implemented MD5, SHA-1, SHA-256 hashing algorithms in Python, simulated dictionary and brute-force cracking attacks against weak passwords, and produced a comparative security report on algorithm strength. Built as part of Cyber Security Internship at Codec Technologies India.

---

## ⚠️ Educational Disclaimer

> This project is built **strictly for educational and security awareness purposes**. All techniques demonstrated are performed in an isolated lab environment on self-generated test data. Understanding how attacks work is essential for building better defenses.

---

## 🎯 Objective

Passwords are the #1 attack vector in cybersecurity. This project demonstrates:
- How hashing algorithms protect passwords at rest
- Why weak passwords fail against modern cracking tools
- Which hashing algorithms are secure vs. broken
- How SOC analysts identify credential-based attacks

---

## 📁 Project Files

| File | Purpose |
|---|---|
| `hashing.py` | Implements MD5, SHA-1, SHA-256, SHA-512 hashing |
| `bruteforce.py` | Simulates brute-force attack against hashed passwords |
| `crack.py` | Dictionary attack using wordlist against target hash |
| `verify.py` | Verifies plaintext password against stored hash |
| `wordlist.txt` | Sample wordlist for dictionary attack simulation |

---

## 🔬 Implementation Details

### 1. Password Hashing (`hashing.py`)

Implemented all major hashing algorithms using Python's `hashlib`:

```python
import hashlib

password = "password123"

# MD5 (broken - do not use in production)
md5_hash = hashlib.md5(password.encode()).hexdigest()

# SHA-1 (weak - deprecated)
sha1_hash = hashlib.sha1(password.encode()).hexdigest()

# SHA-256 (secure - recommended)
sha256_hash = hashlib.sha256(password.encode()).hexdigest()

# SHA-512 (most secure in this comparison)
sha512_hash = hashlib.sha512(password.encode()).hexdigest()
```

**Output example:**
```
Input:   password123
MD5:     482c811da5d5b4bc6d497ffa98491e38
SHA-1:   cbfdac6008f9cab4083784cbd1874f76618d2a97
SHA-256: ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f
SHA-512: [longer hash...]
```

---

### 2. Dictionary Attack (`crack.py`)

Simulates how attackers use common password lists to crack hashes:

```python
import hashlib

def crack_hash(target_hash, wordlist_file):
    with open(wordlist_file, 'r') as f:
        for word in f:
            word = word.strip()
            attempt = hashlib.md5(word.encode()).hexdigest()
            if attempt == target_hash:
                print(f"[+] Password FOUND: {word}")
                return word
    print("[-] Password not found in wordlist")
```

---

### 3. Brute Force Attack (`bruteforce.py`)

Demonstrates how short passwords are vulnerable to exhaustive search:

```python
import hashlib
import itertools
import string

def brute_force(target_hash, max_length=4):
    chars = string.ascii_lowercase + string.digits
    for length in range(1, max_length + 1):
        for combo in itertools.product(chars, repeat=length):
            attempt = ''.join(combo)
            if hashlib.md5(attempt.encode()).hexdigest() == target_hash:
                print(f"[+] Cracked: {attempt}")
                return attempt
```

---

## 📊 Algorithm Comparison Results

| Algorithm | Hash Length | Speed | Status | Crack Time (weak pwd) |
|---|---|---|---|---|
| MD5 | 128-bit | Very Fast | ❌ Broken | < 1 second |
| SHA-1 | 160-bit | Fast | ❌ Deprecated | Seconds |
| SHA-256 | 256-bit | Moderate | ✅ Secure | Years (strong pwd) |
| SHA-512 | 512-bit | Slower | ✅ Most Secure | Decades (strong pwd) |

---

## 🔍 Key Security Findings

| Finding | Risk | Recommendation |
|---|---|---|
| MD5 passwords cracked in < 1 sec | 🔴 Critical | Never use MD5 for passwords |
| Dictionary attack succeeded on "password123" | 🔴 Critical | Enforce strong password policy |
| 4-char passwords cracked by brute force instantly | 🔴 Critical | Minimum 12+ character passwords |
| SHA-256 with salt resisted all attacks | ✅ Secure | Use bcrypt/SHA-256+salt in production |

---

## 🛡️ MITRE ATT&CK Mapping

| Tactic | Technique | ID | Demonstrated |
|---|---|---|---|
| Credential Access | Brute Force: Password Cracking | T1110.002 | `bruteforce.py` |
| Credential Access | Brute Force: Password Spraying | T1110.003 | `crack.py` with wordlist |

---

## 💡 Skills Demonstrated

- ✅ Python scripting for security tools
- ✅ Cryptographic hashing (MD5, SHA family)
- ✅ Dictionary & brute-force attack simulation
- ✅ Algorithm strength comparative analysis
- ✅ Security report writing
- ✅ MITRE ATT&CK T1110 mapping

---

## 🔗 Related Projects

| Project | Description |
|---|---|
| [Splunk SOC Investigation](https://github.com/vivek-sh45/splunk-soc-incident-investigation) | Detecting brute-force attacks in SIEM |
| [SOC Alert Detection Lab](https://github.com/vivek-sh45/soc-alert-detection-lab) | System-level alert triage |
| [Threat Hunting Lab](https://github.com/vivek-sh45/threat-hunting-lab) | C2 & malware traffic detection |

---

## 👤 Author

**Vivek Sharma** — Cybersecurity Analyst (Fresher) | Codec Technologies Internship

[![LinkedIn](https://img.shields.io/badge/LinkedIn-vivek--sharma--cybersec-0077B5?style=flat&logo=linkedin)](https://linkedin.com/in/vivek-sharma-cybersec)
[![GitHub](https://img.shields.io/badge/GitHub-vivek--sh45-181717?style=flat&logo=github)](https://github.com/vivek-sh45)
[![Email](https://img.shields.io/badge/Email-thecybervivek@gmail.com-D14836?style=flat&logo=gmail)](mailto:thecybervivek@gmail.com)
