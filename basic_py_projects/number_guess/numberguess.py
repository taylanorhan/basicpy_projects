import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

attempts = 0
max_attempts = 5

while attempts < max_attempts:
    guess = int(input("Guess the number (between 1 and 100): "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try a higher number.")
    elif guess > secret_number:
        print("Too high! Try a lower number.")
    else:
        print(f"Congratulations! You guessed the number ({secret_number}) correctly in {attempts} attempts.")
        break
else:
    print(f"Sorry, you've reached the maximum number of attempts. The number was {secret_number}. Try again!")
