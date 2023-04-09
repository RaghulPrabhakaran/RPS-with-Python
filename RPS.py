import random

def R():
    Player = "Rock"
    return Player

def P():
    Player = "Paper"
    return Player

def S():
    Player = "Scissors"
    return Player




print("\nHello, Please select options from below,\n")
print("R -> Rock \nP -> Paper\nS -> Scissors\n")



Player = input("Select one [R,P,S]: ")


if Player == "R" or Player == "r":
    Player = "Rock"
    print("\nPlayer Selected: Rock\n")

elif Player == "P" or Player == "p":
    Player = "Paper"
    print("\nPlayer Selected: Paper\n")

elif Player == "S" or Player == "s":
    Player = "Scissors"
    print("\nPlayer Selected: Scissors\n")

else:
    print("\nNot a vailid input, Please select from R,P,S only\n")
    


Bot_Options = ["Rock" ,"Paper" ,"Scissors"]
Bot = random.choice(Bot_Options)
print(f"Bot selected: {Bot}\n")

"""conditions

        Draw,
        Rock / Rock
        Paper / Paper
        Scissors / Scissors

        Player win,
        Rock / Scissors
        Paper/ Rock
        Scissors / Paper

        Bot wins,
        Rock / Scissors
        Paper / Rock
        Scissors / Paper
"""

if Player == "Paper" and Bot == "Paper" or Player == "Rock" and Bot == "Rock" or Player == "Scissors" and Bot == "Scissors":
    print("It's a Draw!\n")
elif Player == "Rock" and Bot == "Scissors" or Player == "Paper" and Bot == "Rock" or Player == "Scissors" and Bot == "Paper":
    print("Player Wins!\n")
elif Player == "Rock" and Bot == "Scissors" or Player == "Paper" and Bot == "Scissors" or Player == "Rock" and Bot == "Paper":
    print("Bot Wins!\n")
else:
    print("Error in input, Please Try Again!")



