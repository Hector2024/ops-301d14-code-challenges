#!/bin/bash

# Script Name:                  challenge05
# Author:                       Hector Cordova
# Date of latest revision:      12/01/2023
# Purpose:                     

# Declaration of variables

# Declaration of functions

# Main

backup_dir="/var/log/backups"
timestamp=$(date +"%Y%m%d%H%M%S")

echo "Original File Sizes:"
du -h /var/log/syslog /var/log/wtmp

mkdir -p "$backup_dir"
gzip -c /var/log/syslog > "$backup_dir/syslog-$timestamp.gz"
gzip -c /var/log/wtmp > "$backup_dir/wtmp-$timestamp.gz"

echo "Compressed File Sizes:"
du -h "$backup_dir/syslog-$timestamp.gz" "$backup_dir/wtmp-$timestamp.gz"

sudo truncate -s 0 /var/log/syslog /var/log/wtmp

echo "Comparison:"
du -h /var/log/syslog /var/log/wtmp "$backup_dir/syslog-$timestamp.gz" "$backup_dir/wtmp-$timestamp.gz"


# End