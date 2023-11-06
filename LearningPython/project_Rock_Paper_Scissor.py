#**************** CREATING A BASIC GAME OF ROCK, PAPER, SCISSOR**********************
import random
#let's add a feature where we will ask players if they would like to play again.

#write the code below in a while loop

while True:


    choice= ["rock", "paper", "scissors"] #starting off by creating a list of 3 choices that we have.
    computer = random.choice(choice) #then we are creating a variable names computer, that will use the random.choice method from module random to pick a random value from the 3 that we have given above.
# we need to make sure that the player only picks from one choice and not anything random, so we will add while loop
    player = None
    while player not in choice:
        player = input("rock, paper or scissors?: ").lower() #this will convert any uppercase input into lower case input.


    if player == computer:
        print("it is a tie")
        print("computer: ", computer)
        print("player: " + player)
    elif player == "rock":
        if computer == "paper":
            print("you lose")
            print("computer: ", computer)
            print("player: " + player)
        if computer == "scissors":
            print("you win")
            print("computer: ", computer)
            print("player: " + player)
    elif player == "paper":
        if computer == "rock":
            print("you win")
            print("computer: ", computer)
            print("player: " + player)
        if computer == "scissors":
            print("you lose")
            print("computer: ", computer)
            print("player: " + player)
    elif player == "scissors":
        if computer == "rock":
            print("you lose")
            print("computer: ", computer)
            print("player: " + player)
        if computer == "paper":
            print("you win")
            print("computer: ", computer)
            print("player: " + player)

    play_again = input("play again? (yes/no").lower()

    if play_again != 'yes':  #!= this means does not equal
        break
print("bye")




