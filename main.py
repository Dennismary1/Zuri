import random

while True:
    choices = ["rock", "paper", "scissors"]

    CPU = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Enter your desired choice rock, paper or scissors?: ").lower()

    if player == CPU:
        print("CPU:", CPU)
        print("player:", player)
        print("IT IS A TIE")
    elif CPU == "rock":
        if player == "paper":
            print("CPU:", CPU)
            print("player:", player)
            print("You Lose")
        if CPU == "scissors":
            print("CPU:", CPU)
            print("player:", player)
            print("You Win")
    elif CPU == "scissors":
        if player == "rock":
            print("CPU:", CPU)
            print("player:", player)
            print("You Lose")
        if CPU == "paper":
            print("CPU:", CPU)
            print("player:", player)
            print("You Win")
    elif CPU == "paper":
        if player == "scissors":
            print("CPU:", CPU)
            print("player:", player)
            print("You Lose")
        if CPU == "rock":
            print("CPU:", CPU)
            print("player:", player)
            print("You Win")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break
    print("Thanks for playing")
