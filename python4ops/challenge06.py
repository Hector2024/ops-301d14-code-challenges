
#imports os
import os 

#variables

name = os.popen("whoami").read().strip()
address = os.popen("ip a ").read().strip()
hardware = os.popen("lshw -short ").read().strip()

#output

print(name)
input("press enter to continue. . .")

print(address)
input("press enter to continue. . .")

print(hardware)
input("press enter to continue. . .")

print("FIN")
