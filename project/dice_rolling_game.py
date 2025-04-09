import random

while True:
    Choice = input("Roll the dice? (y/n): ").lower()
    if Choice == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'({die1}, {die2})')
    elif Choice == 'n':
        print('Thanks for playing')
        break
    else:
        print('Invalid Choice')

