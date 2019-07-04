import os
import time
import sys

time.sleep(1)
print('''
      Hacking framework
      ''')
choice = input('''
               1.Nmap
               2.Ghost-phisher
               3.Metasploit
               4.Aircrack-ng
               5.WebSploit
               6.sqlmap
               7.THC-Hydra
               8.John the Ripper
               9.Go Anonymous using tor
               Select your choice of tool:
               ''')
choice = int(choice)


if choice == 1:
    os.system("nmap")
elif choice == 2:
    os.system("ghost-phisher")
elif choice == 3:
    os.system("./msfconsole")
elif choice == 4:
    os.system("aircrack-ng")
elif choice == 5:
    os.system("websploit")
elif choice == 6:
    os.system("sqlmap")
elif choice == 7:
    os.system("hydra-gtk")
elif choice == 8:
    os.system("john ")
elif choice == 9:
    os.system("tor")
