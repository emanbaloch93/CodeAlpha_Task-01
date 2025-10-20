import random

# List of predefined words
word_list = ["apple", "banana", "grape", "orange", "peach"]

# Choose a random word from the list
secret_word = random.choice(word_list)
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

# Create a display version of the word with underscores
display_word = ["_" for _ in secret_word]

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have", max_incorrect, "incorrect guesses allowed.")
print(" ".join(display_word))

# Game loop
while incorrect_guesses < max_incorrect and "_" in display_word:
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetic character.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Good guess!")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        incorrect_guesses += 1
        print("Wrong guess! You have", max_incorrect - incorrect_guesses, "tries left.")

    print(" ".join(display_word))

# Game result
if "_" not in display_word:
    print("Congratulations! You guessed the word:", secret_word)
else:
    print("Game over! The word was:", secret_word)
