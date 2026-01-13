import random

words = ["python", "coding", "intern", "program", "alpha"]
word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("Welcome to Hangman Game!")
print("Guess the word, one letter at a time.")
print("_ " * len(word))

while incorrect_guesses < max_attempts:
    guess = input("\nEnter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print(" Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print(" You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print(" Good guess!")
    else:
        incorrect_guesses += 1
        print(f" Wrong guess! Attempts left: {max_attempts - incorrect_guesses}")

    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print(display_word)

    if "_" not in display_word:
        print("\n Congratulations! You guessed the word correctly.")
        break


if incorrect_guesses == max_attempts:
    print("\n You lost the game.")
    print("The word was:", word)
