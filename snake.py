# Importing a function to generate random numbers for the dice
from random import randint as rd

start = 0
current = start
final = 100
dice = 0
print("Your Position is: ", current)
condition = True
while(condition):
    dice = rd(1,6) # Rolls a dice and assigns the value to the variable dice
    current += dice # Moving the pawn to a new position according to the value on dice
    
    # Checking if the pawn is at a snake!
    if(current == 10):
        print("Snake!")
        current = 4
    elif(current == 38):
        print("Snake!")
        current = 25
    elif(current == 80):
        print("Snake!")
        current = 13
    elif(current == 98):
        print("Snake!")
        current = 45

    
    # Checking if the pawn is at a ladder
    elif(current == 15):
        print("Ladder!")
        current = 43
    elif(current == 28):
        print("Ladder!")
        current = 33
    elif(current == 36):
        print("Ladder!")
        current = 84
    elif(current == 84):
        print("Ladder!")
        current = 95

    # Checking if the pawn has reached or crossed hundred
    if(current >= 100):
        condition = False

    print("Current Position is: ",current)

# Finishing the game!
print("You won!")