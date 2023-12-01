#!/bin/bash

# Script Name:                  challenge04
# Author:                       Hector Cordova
# Date of latest revision:      11/30/2023
# Purpose:                      Conditionals in Menu Systems


# Create a bash script that launches a menu system with the following options:
run_it=true                                            # identifies the variable true
while $run_it; do                                      # intitiates an infinite loop. script continue to run until user exits.
# Menu System
    echo "Menu System:"
    echo "1. Hello world!"
    echo "2. Ping self"
    echo "3. IP info"
    echo "4. Exit"

# User input should be requested
    read -p "What shall you choose? (1-4): " choice     # -p is paired with read to show the user the prompt. the choice is then stored in the variable 'choice'

# Conditional statement evaluating the user input, then act accordingly to the choice
    case $choice in                                     # case performs conditional branching based on the input from user/value of variable. 
        1)
            echo "Hello world!"
            ;;                                              # double semi-colons are used to terminate each pattern block. when a pattern is matched, the command will execute until ;; is encountered
        2)
            ping -c 4 127.0.0.1                             # in the context of the ping command, -c specifies the number of ICMP echo requests (pings). in this case, that # is 4. 
            ;;
        3)
            ifconfig                                        # network adapter info will be printed if option 3 is selected
            ;;
        4)
            echo "Hasta la Pasta! See you soon."            # if option 4 selected, will be exiting.
            run_it=false                                    # when run_it=true, the loop will continue. when the user chooses exit, run_it=false which causes the loop to end.  
            ;;
        *)
            echo "You have not chosen wisely. Select a number between 1 and 4."
            ;;
    esac

# making it easier to read by introducing a break
    echo ""
done