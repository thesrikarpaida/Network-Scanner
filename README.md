# Network Scanner in Python

This is a network scanner written in Python that provides a list of live hosts and their open ports if provided with a subnet and a mask. Each port runs on a service, so this program can also do a service scan on the open ports after detecting those open ports on each of those live hosts.


### Install

```
git clone https://github.com/thesrikarpaida/Network-Scanner.git 

cd Network-Scanner

chmod +x install.sh

./install.sh
```

The final program is currently in `portScanner.py`. It will accept a subnet and a mask, and will call the `liveHosts.py` to search for the hosts that are live in the network using an ICMP ping request.

This is designed for Linux environments, so the `install.sh` file can be run in Linux operating systems before executing the network scanner. It includes all the software and libraries required for running this without errors.


---
---
---


_***This project is still a work in progress. I'm trying to add OS fingerprinting as well as more structure to the code if possible._

