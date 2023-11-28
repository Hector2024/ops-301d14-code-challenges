#!/bin/bash

# Script Name:                  challenge01
# Author:                       Hector Cordova
# Date of latest revision:      11/28/2023
# Purpose:                      cp /var/log/syslog to pwd and Appends the 
#                               current date and time to the file name 'syslog.txt'

# Make the script itself executable using sudo
sudo chmod +x "$0"

# Declaration of variables

# Declaration of functions

# Main

cat /var/log/syslog >> syslog.txt
mv syslog.txt "$(date +'%Y-%m-%d')_syslog.txt"





# End