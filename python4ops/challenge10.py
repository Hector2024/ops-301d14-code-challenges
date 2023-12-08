'''
Using file handling commands, 
create a Python script that creates a new .txt file, 
appends three lines, 
prints to the screen the first line,
then deletes the .txt file.

'''

# Open a new file in write mode ('w')
with open('NewText.txt', 'w') as file:
    # Append three lines to the file
    file.write('This is the first line.\n')
    file.write('This is the second line.\n')
    file.write('This is the third line.\n')

# Open the file in read mode ('r')
with open('NewText.txt', 'r') as file:
    # Read and print the first line
    first_line = file.readline()
    print('First line:', first_line)

# Delete the file
import os
os.remove('NewText.txt')

print('File deleted successfully.')