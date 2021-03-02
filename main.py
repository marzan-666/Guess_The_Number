
import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number :
        guess = int(input(f'Guess a number between 1 and {x}: '))
        #print(guess)
        if guess < random_number:
            print('Sorry! Guess Again.. To Low..')
        elif guess > random_number:
            print('Sorry! Guess Again.. To High..')

    print(f'Congratulations!!! You have Guessed the Number {random_number}. . .')


def computer_guess(x):
    low = 1
    high =x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high b/c low = high

        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yay...!!! Computer Guessed the Number, {guess}, Correctly')

guess(10)
computer_guess(10)
