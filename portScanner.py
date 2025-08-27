#!/bin/python3

'''

Checking for open ports in each of the live hosts.
This program might cause issues in Windows environments.
Windows by default has ransomware protection enabled and some Python programs may be considered as trouble even though they're not.

'''

import os
from scapy.all import sr1, IP, TCP
from threading import Lock
from concurrent.futures import ThreadPoolExecutor, as_completed

import liveHosts


def synScan(args):
    host, port = args
    response = sr1(IP(dst=host)/TCP(dport=port, flags="S"), timeout=2, verbose=False)
    if response is not None and response.haslayer(TCP) and response[TCP].flags == "SA":
        return port
    return None


def portScanner(host, ports):
    openPorts = []

    threads = os.cpu_count()
    print("Thread count: ", threads)
    lock = Lock()

    totalPorts = len(ports)
    scannedPorts = 0

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = []
        for port in ports:
            future = executor.submit(synScan, (host, port))
            futures.append(future)
        
        for future in as_completed(futures):
            scannedPorts += 1
            result = future.result()
            with lock:
                print(f"Scanning ports {scannedPorts} / {totalPorts}", end="\r")
                if result is not None:
                    print(f"Port {result} is open on host {host}")
                    openPorts.append(str(result))
    
    return openPorts


def getOpenPortsInNetwork(subnet, mask):

    getLiveHosts = liveHosts.pingSweep(subnet, mask)
    # getLiveHosts = ["192.168.1.0"]

    openPorts = {}
    ports = range(1, 1001)

    for host in getLiveHosts:
        openPorts[host] = portScanner(host, ports)
    
    return openPorts



if __name__ == "__main__":

    subnet = "192.168.1.0"
    mask = "24"
    openPortsList = getOpenPortsInNetwork(subnet, mask)


    print("The following are the open ports for each IP address:")
    for host, ports in openPortsList.items():
        print(host, ": ", ", ".join(ports))