from pathlib import Path
from pick import pick
import os
import platform

OS_TYPE = platform.system()
if OS_TYPE == "Windows":
  import msvcrt
else:
  import termios
  import tty

directory = Path(input("Enter file path"))
title = "select files for cleanup (press SPACE to mark, ENTER to continue)"
options = []

def deletion_keys():
  char = msvcrt.getch()
  print(f"Debug: Captured byte is {char}")

  if char == b'\r':
    return 'ENTER'
  elif char == b"\x1b":
    return 'ESC'
  try:
    return char.decode("utf-8")
  except UnicodeDecodeError:
    return str(char)
for file in directory.iterdir():
    options.append(str(file))
    
selected = pick(options,title,multiselect=True, min_selection_count = 1)
print(type(selected))
print("Warning! Deleting files: ", selected, "\n")
print("Should I proceed with the deletion")

while True:
  key = deletion_keys()
  if key == "ENTER":
    print("\nAction: Proceeding with deletion")
    for file in selected:
      print("file object type: ", type(file))
      os.remove(file[0])
      print("deleted : ", file,"\n")
    break

  elif key == "ESC":
    print("\nAction: Process Stopped. Unselecting files for deletion")
    selected.clear()
    break
    
  else:
    print("Press ENTER or ESC")




    
    
    
  