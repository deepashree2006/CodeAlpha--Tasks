# 🟢 Hangman Game
# Goal: Guess the hidden word letter by letter (6 attempts)

import random  # to choose a random word

# list of words
words = ["apple", "banana", "grape", "orange", "mango"]

# randomly select a word
word = random.choice(words)
guessed = "_" * len(word)  # hidden word display
attempts = 6  # limit incorrect guesses
guessed_letters = []  # to store guessed letters

print("🎯 Welcome to Hangman Game!")
print("Guess the word letter by letter.")
print(guessed)

# main game loop
while attempts > 0:
    letter = input("Enter a letter: ").lower()

    # if already guessed
    if letter in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(letter)

    # correct guess
    if letter in word:
        print("✅ Good guess!")
        guessed = "".join([l if l in guessed_letters else "_" for l in word])
    else:
        attempts -= 1
        print(f"❌ Wrong guess! Attempts left: {attempts}")

    print(guessed)

    # check if word is completely guessed
    if "_" not in guessed:
        print("🎉 Congratulations! You guessed the word:", word)
        break
else:
    print("😢 Out of attempts! The word was:", word)
