import os
import time
import sys

time.sleep(1)

print('''
      Install Tools
      1.Install TOR
      2.Install Nmap
      3.Install Ghost Phisher
      4.Install Aircrack-ng
      5.Install WebSploit
      6.Install sqlmap
      7.Install THC-Hydra
      8.Install John the Ripper
      9.Install Metasploit
            ''')
choice = input("Select your choice of tool:")
choice = int(choice)

if choice == 1:
    os.system("sudo apt-get install tor -y")
elif choice == 2:
    os.system("sudo apt-get install nmap -y")
elif choice == 3:
    os.system("sudo apt-get install ghost-phisher -y")
elif choice == 4:
    os.system("sudo apt-get install aircrack-ng -y")
elif choice == 5:
    os.system("sudo apt-get install websploit -y")
elif choice == 6:
    os.system("sudo apt-get install sqlmap -y")
elif choice == 7:
    os.system("sudo  apt-get install hydra-gtk -y")
elif choice == 8:
    os.system("sudo apt-get install john -y ")
elif choice == 9:
    os.system("curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall")
