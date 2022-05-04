# Treasure_Island

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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

where = input("left or right?\n").lower()
if where == "right":
    print("You fell in a hole, Game Over!")
else:
    lake = input("You are on the right track. You walk for a minute and reach a lake. Do you want to wait for Boat or swim on your own? \n Please write wait / swim for your choice.\n")
    if lake == "swim":
        print("You were eaten by a Crocodile, Game Over!")
    elif lake == "wait":
        print("Boat Ride was Smooth. Now you have reached the Treasure Island\n")
        color = input(
            "There are 3 doors in front of you, which one do you wish to open - red, blue or yellow\n")
        if color == "red":
            print("You were engulfed in Fire, Game Over!")
        elif color == "yellow":
            print("Woohooo! You have WON the Treasure!!!!")
        elif color == "blue":
            print("You unleashed a hungry beast. He will eat you in 2 bites, Game Over!")
        else:
            print("Game Over!")
    else:
        print("Game Over Baby!")
