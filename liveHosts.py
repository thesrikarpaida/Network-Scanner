#!/bin/python3

'''

Checking for live hosts in the provided subnet and mask.
An ICMP ping request is sent to each host in the provided subnet for checking if the host is live or not.

'''

import os
from netaddr import IPNetwork
from scapy.all import sr1, IP, ICMP

from threading import Lock
from concurrent.futures import ThreadPoolExecutor, as_completed



def pingHost(host):
    response = sr1(IP(dst=str(host))/ICMP(), timeout=2, verbose=False)
    if response is not None:
        return str(host)
    return None


def pingSweep(subnet, mask):
    if not mask:
        print("Invalid subnet mask provided. Provide a valid integer between 1 and 31")
        exit(1)
    liveHosts = []
    
    possibleHosts = 0
    scannedHosts = 0

    network = IPNetwork(subnet + "/" + mask)

    for host in network.iter_hosts():
        possibleHosts += 1
    
    threads = os.cpu_count()
    lock = Lock()
    
    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = []
        for host in network.iter_hosts():
            future = executor.submit(pingHost, host)
            futures.append(future)
        
        for future in as_completed(futures):
            scannedHosts += 1
            result = future.result()
            with lock:
                print(f"Scanning {scannedHosts} / {possibleHosts}", end="\r")
                if result is not None:
                    print(f"Host {result} is live.")
                    liveHosts.append(str(result))
    
    return liveHosts




if __name__ == "__main__":

    subnet = "192.168.128.0"
    mask = "24"
    liveHosts = pingSweep(subnet, mask)

    if not liveHosts:
        exit(0)
    
    print("Finished scanning the subnet.")
    print("The following hosts are active in the provided subnet:\n", ", ".join(liveHosts))
