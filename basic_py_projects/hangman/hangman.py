import random

word_bank = ['a', 'b', 'c', 'd', 'e', 'f']  

def select_word():
    return random.choice(word_bank)

def display_word(word, guessed_letters):
    return ''.join(letter if letter in guessed_letters else '_' for letter in word)

def hangman():
    word_to_guess = select_word()
    guessed_letters = []
    attempts = 6 

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word_to_guess:
            guessed_letters.append(guess)
            print(display_word(word_to_guess, guessed_letters))
        else:
            attempts -= 1
            print(f"Incorrect! Attempts left: {attempts}")
            print(display_word(word_to_guess, guessed_letters))

        if '_' not in display_word(word_to_guess, guessed_letters):
            print("Congratulations! You guessed the word.")
            break

    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The word was {word_to_guess}.")


