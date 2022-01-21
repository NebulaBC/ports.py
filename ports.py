import os
import sys

if os.geteuid() != 0:
    exit("Please run this script as root!")
else:
    if sys.argv[1] == "open":
        print("Please enter the ports you wish to open as 1 2 3")
        ports = [int(x) for x in input().split()]
        times = len(ports)
        num = 0
        for i in range(0,times):
            os.system(f"iptables -A INPUT -p tcp --dport {ports[num]} -j ACCEPT")
            num=num+1
        os.system("netfilter-persistent save && netfilter-persistent reload")
        print(f"Port(s) {ports} successfully opened.")
    elif sys.argv[1] == "close":
        print("Please enter the ports you wish to close 1 2 3")
        ports = [int(x) for x in input().split()]
        times = len(ports)
        num = 0
        for i in range(0,times):
            os.system(f"iptables -A INPUT -p tcp --dport {ports[num]} -j DENY")
            num=num+1
        os.system("netfilter-persistent save && netfilter-persistent reload")
        print(f"Port(s) {ports} successfully closed.")
    else:
        print("Please follow up the command with open or close.")


