# Network Scanner in Python

This is a network scanner written in Python that provides a list of live hosts and their open ports if provided with a subnet and a mask.


### Install

```
git clone https://github.com/thesrikarpaida/Network-Scanner.git 

cd Network-Scanner

chmod +x install.sh

./install.sh
```

The final program is currently in `portScanner.py`. It will accept a subnet and a mask, and will call the `liveHosts.py` to search for the hosts that are live in the network using an ICMP ping request.

This is designed for Linux environments, so the `install.sh` file can be run in Linux operating systems before executing the network scanner. It includes all the software and libraries required for running this without errors.



###


---
This project is still a work in progress. I'm trying to involve service fingerprinting as well as make the code more readable and capable of giving more details based on the scan.
---
