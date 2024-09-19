# Playing rock, paper and scissors against the computer.
# Here a player chooses his move and then computer randomly
# chooses his moves and decide who wins.
from random import randint

moves=["rock", "paper", "scissors"]

while True:
    computer= moves[randint(0,2)]
# the above code let the computer choose randomly from the list
# of moves
    player= input("rock, paper or scissors? (or end)").lower()
    if player == "end":
        print("then game is ended")
        break
    elif player == computer:
        print("Tie!")
    elif player =="rock":
        if computer == "paper":
            print("You lose!", computer, "beats", player)
        elif computer == "scissors":
            print("You win", player, "beats", computer)
    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "beats", player)
        elif computer == "rock":
            print("You win!", player, "beats", computer)
    elif player == "scissors":
        if computer == "rock":
            print("You lose!", computer, "beats", player)
        elif computer == "paper":
            print("You win!", player, "beats", computer)
    else:
        print("Check your spelling")






