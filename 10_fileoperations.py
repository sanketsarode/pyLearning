'''
fileObj = open(file_ame , [accessmode])

fileObj.write(string)
fileObj.read([count]) #count meaning number of characters to read from file, nothing means it will read all characters from file

os.rename(currentfile, newfilename) #reanme() is method from os module
os.remove(file_name)
'''

import os

newfile = open('fileoperations.txt', 'w+')

# will display the mode in which the file is opened
print(newfile.mode)

# will display the name of the file
print(newfile.name)

newfile.seek(0)
print(newfile.tell())

for i in range(0, 10):
    newfile.write('\nHello World! in side files')

newfile.close()

newfile = open('fileoperations.txt', 'r')
print(newfile.read())
newfile.close()

os.rename('fileoperations.txt', 'newfileoperations.txt')
os.remove('newfileoperations.txt')
