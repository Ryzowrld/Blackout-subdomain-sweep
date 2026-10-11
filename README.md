# Automated Subdomain Brute-Forcer
> **Category:** Reconnaissance & Asset Management  
> **Target Environment:** Cross-Platform (Linux / macOS / Windows)  
> **License:** MIT License

---

## Project Overview

This repository contains a streamlined reconnaissance utility written in Python. The tool automates the passive asset-discovery phase of a security assessment by programmatically identifying unlinked subdomains (such as `://target.com` or `://target.com`) against a user-supplied wordlist.

---

## Core Technical Features

* **Dynamic File Streaming:** Reads wordlists line-by-line using buffered file streams to maintain a light memory footprint.
* **Dynamic Target Injection:** Accepts user input at runtime to target any specified domain and custom wordlist path.
* **Network Query Processing:** Leverages native HTTP protocol handling to request remote headers and evaluate structural server responses.
* **Exception Handling:** Implements robust connection error suppression to ensure the execution pipeline skips inactive endpoints without halting execution.

---

## Deployment & Usage

### 1. Prerequisites
Ensure the necessary HTTP request handling dependencies are present within your Python runtime environment:

```bash
pip install requests
```

### 2. Execution
Run the primary script module directly from the terminal interface:

```bash
python3 blackout_sweep.py
```

---

## Structural Execution Log Output

```text
Enter target domain (e.g., example.com): target.com
Enter path to wordlist file: wordlist.txt

[*] Launching automated scanning pipeline against: target.com
[*] Parsing wordlist entries from: wordlist.txt

[+] Active Subdomain Identified: http://://target.com
[+] Active Subdomain Identified: http://target.com
[*] Scan execution sequence complete.
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
*Disclaimer: This utility is developed exclusively for authorized, educational security evaluation purposes within controlled, local testing infrastructures.*
