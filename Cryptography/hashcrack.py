#!/usr/bin/python3

import hashlib
import pyfiglet

print("=========== Hash Cracker ============")

wordlist_location = str(input('[+] Enter wordlist file location: '))
hash_input = str(input('[+] Enter hash to be cracked: '))

# hashtype = input("[+] Enter Hash Type:").lower()

with open(wordlist_location, 'r') as file:
    for line in file.readlines():

        # Replace Sha256 with a hash type
        hash_ob = hashlib.sha256(line.strip().encode())
        hashed_pass = hash_ob.hexdigest()
        if hashed_pass == hash_input:
            print('[!!] Found cleartext password! ' + line.strip())
            exit(0)
