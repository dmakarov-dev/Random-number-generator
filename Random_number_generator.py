import random

secret_number = random.randint(1, 10)

print("I'm thinking of a number between 1 and 10. Can you guess what it is?")
guess = int(input())

while guess != secret_number:
    if guess < secret_number:
        print("Too low. Guess again.")
    else:
        print("Too high. Guess again.")
    guess = int(input())

print("Congratulations! You guessed the number.")
