import random


def guess(x):
    randomNumber = random.randint(1, x)    
    guess = 0
    while guess != randomNumber:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < randomNumber:
            print('Sorry, guess again. Too low.')
        elif guess > randomNumber:
            print('Sorry, guess again. Too high')

    print(
        f'Yay, congrats. You have guessed the number {randomNumber} correctly')


guess(10)