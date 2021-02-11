#color print; time and sleep; plus clear
from termcolor import cprint; import time; from time import sleep; import os

#clear used for frames !3!
def clear():
    os.system("clear")
    
#tile show !2!
def screen():
    print("-"*len(tiles[0]))
    for i in tiles:
        print("".join(i))
    print("-"*len(tiles[0]))

taking_inp=False
def ask(a):
    taking_inp = a

#engine stuff

#5 horizontal, 5 vertical so 5x5 but looks like
#*****
#*****
#*****
#*****
#*****
#on deafult... !4!
tiles=[
    ["*","*","*","*","*","*"],
    ["*","*","*","*","*","*"],
    ["*","*","*","*","*","*"],
    ["*","*","*","*","*","*"]
]
#values in memory, thinking of an adapted brainf as programing lang for this engine
#20 str values
memory=[
    "","","","","","","","","","","","","","","","","","","",""
]

#frame loop !1!
while True:
    screen()
    print(time.ctime(time.time()))
    #if input requested
    if taking_inp == True:
        in_channel=input("> ")
    sleep(0.5)
    clear()
    