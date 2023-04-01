#!/usr/bin/python3
import requests,sys,os

def domain_scan(domain_name,dir_names):
    print('\n----URL after scanning subdomains----\n')

    for directories in dir_names:
        url = f"http://{domain_name}/{directories}.html"
        
        r = requests.get(url)
        if r.status_code==404:
            pass
        else:
            requests.get(url)
            print(f'[+] {url}')

if __name__ == '__main__':
    dom_name = input("Enter a Domain: ")
    
    wordlist = input("Enter a Wordlist Path: ")
    with open (wordlist, 'r') as file:
        name = file.read()
        dir_dom = name.splitlines()

    domain_scan(dom_name,dir_dom)
