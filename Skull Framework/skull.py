import os
import time
import sys
import traceback
print('''Welcome to framework

     _          _ _  __                                             _
    | |        | | |/ _|                                           | |
 ___| | ___   _| | | |_ _ __ __ _ _ __ ___   _____      _____  _ __| | __
/ __| |/ / | | | | |  _| '__/ _` | '_ ` _ \ / _ \ \ /\ / / _ \| '__| |/ /
\__ \   <| |_| | | | | | | | (_| | | | | | |  __/\ V  V / (_) | |  |   <
|___/_|\_\\__,_|_|_|_| |_|  \__,_|_| |_| |_|\___| \_/\_/ \___/|_|  |_|\_\

         ---developed by evilhacker53''')

choice = input('''Enter your choice [1-3] :
               1.Install Tools
               2.See your IP Address
               3.Enter Hacking framework
              ''')
choice = int(choice)


if choice == 1:
    os.system("python3 tools.py ")
elif choice == 2:
    os.system("ifconfig")
elif choice == 3:
    os.system("python3 run.py")
