# https://www.youtube.com/watch?v=yVl_G-F7m8c

import random

number_to_guess = random.randint(1, 100)
while True:
    try:
        guess = int(input('Guess the number between 1 and 100: '))
        if guess < number_to_guess:
            print('Too Low!')
        elif guess > number_to_guess:
            print('Too High!')
        else:
            print('Congratulations! Guessed the correct number')
            break
    except ValueError:
        print('Please enter a valid number')