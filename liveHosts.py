#!/bin/python3

'''

Checking for live hosts in the provided subnet and mask.
An ICMP ping request is sent to each host in the provided subnet for checking if the host is live or not.

'''

import sys
from netaddr import IPNetwork
from scapy.all import sr1, IP, ICMP


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
    
    for host in network.iter_hosts():
        scannedHosts += 1
        print(f"Scanning: {scannedHosts}/{possibleHosts} hosts...", end="\r")
        
        response = sr1(IP(dst=str(host))/ICMP(), timeout=1, verbose=0)
        if response is not None:
            liveHosts.append(str(host))
            print(f"Host {host} is online.")
    
    return liveHosts




if __name__ == "__main__":

    subnet = "10.173.154.95"
    mask = "24"
    liveHosts = pingSweep(subnet, mask)

    if not liveHosts:
        exit(0)
    
    print("Finished scanning the subnet.")
    print("The following hosts are active in the provided subnet:\n", ", ".join(liveHosts))