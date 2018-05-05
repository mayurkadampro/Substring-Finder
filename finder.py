import os
import sys

BLUE, RED, WHITE, YELLOW, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[32m', '\033[0m'

if len(sys.argv) < 2:
    sys.stdout.write(RED + """    
    
       ▄████████  ▄█  ███▄▄▄▄   ████████▄     ▄████████    ▄████████ 
      ███    ███ ███  ███▀▀▀██▄ ███   ▀███   ███    ███   ███    ███ 
      ███    █▀  ███▌ ███   ███ ███    ███   ███    █▀    ███    ███ 
     ▄███▄▄▄     ███▌ ███   ███ ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀ 
    ▀▀███▀▀▀     ███▌ ███   ███ ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
      ███        ███  ███   ███ ███    ███   ███    █▄  ▀███████████ 
      ███        ███  ███   ███ ███   ▄███   ███    ███   ███    ███ 
      ███        █▀    ▀█   █▀  ████████▀    ██████████   ███    ███ 
                                                          ███    ███ 
                                             
    """  + END + BLUE +
    '\n' + 'Matching String Finder'.format(RED, END).center(69) +
    '\n' + 'Made ^_^ by: {}Mighty Ghost Hack'.format(YELLOW, RED, YELLOW, BLUE).center(76) +
    '\n' + 'Version: {}1.0{}\n'.format(YELLOW, END).center(80) + '\n')
else:
    sys.exit('Usage: python finder.py')
    os.system("clear")


inputfile = input("  [+]Enter Your Input File Name :")
outputfile = input("  [+]Enter Your Output File Name :" )
searchstring = input("  [+]Enter Your SearchString : ")

print("\n  [+]Looking In ",inputfile+" \n  [+]Storing Result In ",outputfile + " \n  [+]Searching For", searchstring)
check = input("\n  [+]Proceed? (y/n) : ")

f1 = open(inputfile,"r")
f2 = open(outputfile,"a+")

if check == 'y':
    lines_seen = set()
    total_seen = 0
    for line in f1:
        if line not in lines_seen:
            if searchstring in line:
                f2.write(line)
                lines_seen.add(line)
                total_seen += 1

    print("\n  Total Password Found Here : ", total_seen)
    print("\n  Saved in : ",outputfile)
f1.close()
f2.close()
