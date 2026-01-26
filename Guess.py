import random

print("🎯 Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")
print("Try to guess it!\n")

number_to_guess = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Enter your guess: ")

    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < number_to_guess:
        print("Too low! Try again.\n")
    elif guess > number_to_guess:
        print("Too high! Try again.\n")
    else:
        print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
        break
