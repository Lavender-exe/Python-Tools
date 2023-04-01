#!/usr/bin/python3
import sys
import socket
import pyfiglet

ip = f"{sys.argv[1]}"
open_ports = []
ports = range(1000, 65535)

print(f"\n[i] Starting Port Scan on {ip}\n")
def probe_port(ip, port, result = 1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        r = sock.connect_ex((ip, port))
        if r == 0:
            result = r
            sock.close()
    
    except Exception as e:
        pass

    return result

for port in ports:    
    sys.stdout.flush()
    response = probe_port(ip, port)
    
    if response == 0:
        open_ports.append(port)

if open_ports:
    print ("[+] Open Ports: ")
    print (sorted(open_ports))

else:
    print ("[X] No Closed Ports")
