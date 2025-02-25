# https://www.freecodecamp.org/news/python-projects-for-beginners/#heading-guess-the-number-game-python-project-computer

import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess!= random_number:
        guess = int(input("guess a number between 1 and x"))

        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")
    print(f'Congrats, You have guessed the number {random_number} correctly !')


guess(15)



