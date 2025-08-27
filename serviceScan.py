#!/bin/python3

'''

Check for the service that is running on the provided open port.

'''

import socket
from threading import Lock
from concurrent.futures import ThreadPoolExecutor, as_completed
import portScanner



def getServiceBanner(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        sock.connect((host, port))
        sock.send(b"GET / HTTP/1.1\r\nHost: " + host.encode() + b"\r\n\r\n")
        result = sock.recv(1024)
        sock.close()
        return result.decode('utf-8', errors='ignore')
    except Exception as e:
        print("Exception:", e)
        return None



if __name__ == "__main__":

    subnet = "192.168.1.0"
    mask = "24"
    openPorts = portScanner.getOpenPortsInNetwork(subnet, mask)

    for host, ports in openPorts.items():
        print(f"Scanning for host {host}:\n")
        for port in ports:
            banner = getServiceBanner(host, int(port))
            print(f"Port {port}:\n{banner}\n")
        print("\n\n\n")

    