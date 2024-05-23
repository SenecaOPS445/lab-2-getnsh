#!/usr/bin/env python3
#Author: Geetansh Chawla 
#Author ID: 177726213
#Date Created: 2024/05/22

import sys

if len(sys.argv)!= 2:
    timer = 3
    while timer > 0:    
        print(timer)
        timer = timer - 1
    print ("blast off!")
    sys.exit()
else:
    timer = int(sys.argv[1])

while timer > 0:
    print(timer)
    timer = timer - 1
    
print("blast off!")
sys.exit()