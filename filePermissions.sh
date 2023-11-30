#!/bin/bash

# Script Name:                  file
# Author:                       Hector Cordova
# Date of latest revision:      11/28/2023
# Purpose:                      cp /var/log/syslog to pwd and Appends the 
#                               current date and time to the file name 'syslog.txt'

# Make the script itself executable using sudo


# Prompts user for input directory path.

echo "Please input directory path."
read directory_path
echo "You entered $directory_path"

# Prompts user for input permissions number (e.g. 777 to perform a chmod 777)

echo "Please input permission number."
read permission_number 

# Navigates to the directory input by the user and changes all files inside it to the input setting.

cd "$directory_path"
chmod -R --no-preserve-root "$permissions_number" "$directory_path" . 


# Prints to the screen the directory contents and the new permissions settings of everything in the directory.

ls -l "$directory_path"

# End