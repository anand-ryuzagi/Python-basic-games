import random

def guess(x):
    random_number = random.randint(1,x)
    guess_number = 0
    while guess_number != random_number:
        guess_number = int(input(f"enter the value between 1 and {x} : "))
        if(guess_number > random_number):
            print("Your guess is high")
        elif(guess_number < random_number):
            print("Your guess is low")
    print("Congrats you guess the correct number")

guess(10)
