# ports.py

This script was made for a friend, and occasional personal use. Do not complain, or ask for support!

### info on how to use ubuntu-port-opener (because I'm nice)
this is made because UFW is a nightmare on *some* builds of Ubuntu 20.04, and sometimes its annoying to deal with IPTables.
1. `sudo su`
2. `apt update && apt upgrade`
3. `wget https://ports.neb.cx/ports.py`
4. `python3 ports.py firstrun` (make extra sure to enter your SSH port!)

After the first run of ports.py, you can run `python3 ports.py open` or `python3 ports.py close`.

ports.py is currently working. Feel free to use ports.py with the instructions above.