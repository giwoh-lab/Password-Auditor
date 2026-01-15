# Password-Auditor
# 🛡️ Password Auditor Tool

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Security](https://img.shields.io/badge/Security-Tool-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A powerful, terminal-based password strength analyzer written in Python.

This tool evaluates passwords based on **Length**, **Complexity (Regex)**, **Entropy (Shannon Formula)**, and checks against real-world data leaks (**Dictionary Attack**).

---

## ✨ Features

* **🔐 Security Checks:** Detects weak passwords based on length and character types (uppercase, lowercase, digits, symbols).
* **🧮 Entropy Calculation:** Uses the **Shannon Entropy** formula to calculate the information density (bits) of the password.
* **📚 Blacklist Verification:** Instantly checks if the password exists in the `rockyou.txt` database (or any custom dictionary).
* **📊 Detailed Reporting:** Provides a strength rating (**Very Weak** to **Very Strong**) and actionable advice.

---

## 🚀 Installation & Usage

### Prerequisites
* Python 3.x installed.
* (Optional) A dictionary file like `rockyou.txt` placed in the project folder.

### 1. Clone the repository
Open your terminal and run the following commands:

```bash
git clone https://github.com/giwoh-lab/Password-Auditor.git
cd Password-Auditor
````

### 2. Run the Tool
🟢 For Windows Users: Double-click the run_windows.bat file.

🐧 For Linux / macOS Users: Open a terminal and run:

```Bash

chmod +x run_linux.sh
./run_linux.sh
```
### ⚠️ Disclaimer
This tool is for educational purposes only. Do not use it to audit passwords that do not belong to you or without permission.

### Author: Vivisect0r
