import os
import sys

if os.geteuid() != 0:
    exit('Please run this script as root!')
else:
    if sys.argv[1] == 'firstrun':
        if os.path.exists("/etc/portctl.firstrun") == False:
            print('Please enter the ports you wish to open as 1 2 3 (REMEMBER TO INCLUDE YOUR SSH PORT!!1!)')
            print('This command will also drop all previous ports opened, so remember to re-open them.')
            ports = [int(x) for x in input().split()]
            times = len(ports)
            num = 0
            os.system('iptables -F')
            os.system('iptables -P INPUT DROP')
            for i in range(0,times):
                os.system(f'iptables -A INPUT -p tcp --dport {ports[num]} -j ACCEPT')
                num=num+1
            os.system('netfilter-persistent save && netfilter-persistent reload')
            os.system('touch /etc/portctl.firstrun')
            print(f'Port(s) {ports} successfully opened. From now on run python3 ports.py open')
        else:
            print("You have already run firstrun, please run open")
    elif sys.argv[1] == "open":
        if os.path.exists("/etc/portctl.firstrun") == True:
            print('Please enter the ports you wish to open as 1 2 3')
            ports = [int(x) for x in input().split()]
            times = len(ports)
            num = 0
            for i in range(0,times):
                os.system(f'iptables -A INPUT -p tcp --dport {ports[num]} -j ACCEPT')
                num=num+1
            os.system('netfilter-persistent save && netfilter-persistent reload')
            print(f'Port(s) {ports} successfully opened.')
        else:
            print('You have not run ports.py before! Please run it with the argument firstrun instead of open')
    elif sys.argv[1] == 'close':
        print('Please enter the ports you wish to close 1 2 3')
        ports = [int(x) for x in input().split()]
        times = len(ports)
        num = 0
        for i in range(0,times):
            os.system(f'iptables -A INPUT -p tcp --dport {ports[num]} -j DENY')
            num=num+1
        os.system('netfilter-persistent save && netfilter-persistent reload')
        print(f'Port(s) {ports} successfully closed.')
    else:
        print('Please follow up the command with open or close.')
