import random
import time 

options = ["rock","paper", "scissors"]

computer = options[random.randint(0,2)]

Player = False
while Player == False:
    Player = input(("What do you choose? rock, paper or scissors?"))
    if Player == computer:
        print("It's a tie!")
    elif Player == "rock":
        if computer == "paper":
            print("Computer chose", computer)
            time.sleep(1)
            print("You lose!")
        else:
            print("Computer chose", computer)
            time.sleep(1)
            print("You win!")
    elif Player == "paper":
        if computer == "scissors":
            print("Computer chose", computer)
            time.sleep(1)
            print("You lose!")
        else:
            print("Computer chose", computer)
            time.sleep(1)
            print("You win!")
    elif Player == "scissors":
        if computer == "rock":
            print("Computer chose", computer)
            time.sleep(1)
            print("You lose!")
        else:
            print("Computer chose", computer)
            time.sleep(1)
            print("You win!")
    else:
        print("Invalid choice ._.")
        Player = False
    Player = False
    computer = options[random.randint(0,2)]