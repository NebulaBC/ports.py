import os
import sys

# Alternate path as to going fully NCURSES, going no interaction terminal only.
if sys.argv[1] == "firstrun":
    continuescript = input("Are you sure you wish to run this script? [y/n] ")
    if continuescript.lower() == "n" or continuescript.lower() == "no":
        print("Quitting...")
        quit()
    elif continuescript.lower() == "y" or continuescript.lower() == "yes":
        sshport = input("What is your ssh port? ")
