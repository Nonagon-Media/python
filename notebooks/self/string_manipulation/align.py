#A procedure to print the content of a list aligned to the left
def leftAlign(list):
  print("___________________")
  print("|                 |")
  
  for item in list:
    itemLength = len(item)
    spaces = " " * (15 - itemLength)
    print("| " + item + spaces + " |")
  print("|_________________|")
    
  
### MAIN PROGRAM STARTS HERE ####
capitals = ["Paris","Amsterdam","Oslo","London","Berlin","Vienna","Rome","Stockholm","Madrid"]
capitals.sort()

leftAlign(capitals)