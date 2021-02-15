import random


def play():
    user = input("'r' for rock, 'p' for paper,'s' for scissor : ").lower()

    computer = random.choice(['r','p','s'])

    if user == computer:
        return "It is a tie"

    if (user == 'r' and computer == 's') or (user == 'p' and computer =='r') or (user == 's' and computer =='p'):
        print(f"computer chooses {computer} and You won!!!")
    
    else:
        print(f"computer chooses {computer} and You lost!!!")

play()
