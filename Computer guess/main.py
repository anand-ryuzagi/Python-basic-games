import random

def c_guess(x):
    low =1
    high =x
    feedback = ''
    print('Guess a number!!')
    while feedback != 'correct':
        c_guess = random.randint(low,high)
        
        feedback = input(f"Is {c_guess} high or low or correct : ").lower()

        if feedback == 'high':
            high = c_guess-1
        elif feedback == 'low':
            low = c_guess+1

    print(f"Yay! computer guess the answer correctly... Number is {c_guess}")

c_guess(10)
