#This script takes a directory and optional keyword search to find filename(s) as input and outputs a .txt report about what's in that directory and finds filenames based on keyword.
import os
from pathlib import Path
directory_path = Path(input("Folder : "))
filename  = input("Enter filename to view file contents or just hit enter to leave blank : ")

filesfound = []
total_files_found = 0
 
for item in directory_path.iterdir():
    item = item.relative_to(directory_path)
    print(item)
    if filename in str(item):
        filesfound.append(item)
        total_files_found += 1
print("===========================")
print("total files found based on the keyword: ", total_files_found)
for file in filesfound:
    print(file,"\n")
    
 
