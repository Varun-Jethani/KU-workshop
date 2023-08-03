#!/user/Varun/college/pythonnptel/ conda python3.9.13
"""
Created on Fri April 21 14:15:30 2023

@author:Varunjethani
"""

import random

door=[0]*3
goatdoor=[]
swap=0 #No of Swap wins
dont_swap=0 #no of Dont swap wins

for j in range(10):

    x=random.randint(0,2) #xth door will comprise of BMW
    for i in range(0,3):
        if i==x:
            door[i]="BMW"
        else:
            door[i]="Goat"
            goatdoor.append(i)
    choice = int(input("Enter your Choice:"))
    door_open=random.choice(goatdoor)
    while(door_open==choice):
        door_open=random.choice(goatdoor)
    ch = input("Do you want to swap? y/n : " )
    if ch=='y':
        if door[choice]=="Goat":
            print("Player wins")
            swap+=1
        else:
            print("Player lost")
    else:
        if door[choice]=="Goat":
            print("Player Lost")
        else:
            print("Player Wins")
            dont_swap+=1
print("Swapping Victories",swap)
print("Not Swapping Victories:",dont_swap)