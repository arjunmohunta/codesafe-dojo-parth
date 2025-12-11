# Secure Text Utility Challenge

In this challenge, you will complete a partially implemented text-processing tool and secure it against command injection attacks. The goal is to learn basic software engineering practices, implement small transformations, and fix a real security vulnerability — all while preserving the original intended behavior.

---

## 📌 Scenario

Codesafe has received a prototype text utility built to help developers process user-supplied text (reverse words, check palindromes, convert lists, etc.).  
However:

### ⚠️ The prototype contains a **command injection vulnerability**  
A malicious user could inject shell commands and potentially read sensitive files (like `/flag`).  
Your task is to complete the missing program logic **and** secure the system.

---

## What You Must Do

You are given a starter Python file: `modify_me.py`  
You must complete the following tasks:

### **Task 1 — Implement the missing text-processing functions**
You must write correct implementations for:
- `reverse_string`
- `is_palindrome`
- `to_upper_list`
- `to_lower_list`

### **Task 2 — Block malicious input**
You must complete the `is_malicious(text)` function so that it detects and rejects shell-injection attempts.

### **Task 3 — Fix the security vulnerability**
The current `process_text()` function improperly invokes a shell command.  
You must rewrite it so it:

- Does **not** use `os.system`
- Does **not** use `shell=True`
- Does **not** allow shell execution at all  
- Always correctly returns:  
