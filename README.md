![screen](img/ubuntutouch.gif)

## Proof of Concept: Privilage escalation in Ubuntu Touch 16.04 - by PIN Bruteforce 

Ubuntu Touch allows you to "protect" devices with a 4-digit passcode. Such a code was set in a demonstration device. The problem is that the same 4-digit passcode then 
becomes a password that we can use with the sudo command and gain root privileges.

This means that a malicious application can do us double harm:
1. Easy escalation of permissions and taking control of the device.
2. Give the screen unlock passcode to a third party.

My PoC file is trivial but it perfectly illustrates the essence of the problem.


![screen](img/screen2.png)

![screen](img/screen3.png)


## Contact

Feel free to contact me on [Twitter @FilipKarc](https://twitter.com/FilipKarc).

Be sure to follow me on LinkedIn: [LinkedIn](https://www.linkedin.com/in/filip-karczewski/).


  
