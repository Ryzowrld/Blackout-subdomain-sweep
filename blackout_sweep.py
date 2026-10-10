import os
import sys
import requests

target_domain = input("Enter your target url: ").strip()

print("\n[▪] Default BlackArch Wordlist: /usr/share/wordlists/subdomains.txt")
wordlist_path = input("Enter wordlist path (Press Enter to use default): ").strip()

if not wordlist_path:
    wordlist_path = "/usr/share/wordlists/subdomains.txt"

if not os.path.exists(wordlist_path):
    wordlist_path = "subdomains.txt"
    if not os.path.exists(wordlist_path):
        print("[-] Error: No wordlist file found. Create 'subdomains.txt' or specify a valid path.")
        sys.exit(1)
print(f"\n[*] Starting automated subdomain sweep on: {target_domain}")
print(f"[*] Utilizing wordlist profile: {wordlist_path}\n")