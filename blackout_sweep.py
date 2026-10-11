#!/usr/bin/env python3
import os
import sys
import requests

# 1. Accept target input from the terminal interface
target_domain = input("Enter target domain (e.g., example.com): ").strip()

# 2. Accept the custom wordlist file path from the user
wordlist_path = input("Enter path to wordlist file: ").strip()

# Validate if the wordlist file actually exists on the system
if not os.path.exists(wordlist_path):
    print(f"\n[-] Error: Wordlist file not found at '{wordlist_path}'")
    sys.exit(1)

print(f"\n[*] Launching automated scanning pipeline against: {target_domain}")
print(f"[*] Parsing wordlist entries from: {wordlist_path}\n")

# 3. Read the wordlist line by line to check all entries
try:
    with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as file:
        for line in file:
            # Strip whitespace and trailing newlines
            word = line.strip()
            
            # Safely skip empty lines or wordlist comment lines (#)
            if not word or word.startswith("#"):
                continue
                
            # Construct the full subdomain address
            subdomain = f"{word}.{target_domain}"
            url = f"http://{subdomain}"
            
            try:
                # Issue HTTP request and timeout quickly if the server doesn't respond
                response = requests.get(url, timeout=1.5)
                
                # Capture and output the active HTTP door targets
                if response.status_code == 200:
                    print(f"[+] Active Subdomain Identified: {url}")
                    
            except requests.ConnectionError:
                # Dead subdomains throw an error; catch it silently and keep looping
                pass
                
except KeyboardInterrupt:
    print("\n[-] Scan execution canceled by user (Ctrl+C). Exiting.")
    sys.exit(0)

print("\n[*] Scan execution sequence complete.")
