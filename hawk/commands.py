# hawk/commands.py

import socket

def scan_ports(ip):
    print(f"Scanning ports on {ip}...")
    for port in range(20, 100):
        s = socket.socket()
        s.settimeout(0.5)
        try:
            s.connect((ip, port))
            print(f"Port {port} is OPEN")
        except:
            pass
        s.close()
        
def log(msg):
    print(f"[Hawk Log]: {msg}")
