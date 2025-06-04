import time
print("welcome to treasure island")
time.sleep(1)
print("we hope you find the treasure")
time.sleep(2)
d=input("Do You Want To Go To Right Or Left :")
if d=='Left':
    time.sleep(1)
    print("Game Over You Fell In A Ditch")
elif d=='Right':
    time.sleep(1)
    sw=input("Do You Want To Swim Or Do You Want To Wait:")
    if sw=='Swim':
        print("Game Over You Died Of Shark Attak")
    elif sw=='Wait':
        time.sleep(1)
        g=input("choose a gate (RED,BlUE,GREEN):")
        if g=='RED':
            print("You Fell Into Lava")
            time.sleep(1)
            print( "Game Over....")
        elif g=='GREEN':
            print("You Fell Into A Ravine")
            time.sleep(1)
            print("Game Over....")
        elif g=='BLUE':
            print("Treasure Has Been Found")
            time.sleep(1)
            print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
        else:
            time.sleep(2)
            print("Gods wraths game over")
    else:
        time.sleep(2)
        print("Gods wraths game over")
else:
    time.sleep(2)
    print("Gods wraths game over")   