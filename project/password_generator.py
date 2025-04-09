import random

print("Welcome to your password generator")
Chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(),.?'
number = input("Amount of password to generate: ")
number = int(number)
length = input("Input your password length")
length = int(length)
print("\nHere are your password: ")
for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(Chars)
    print(passwords)