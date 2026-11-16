"""
PS No. 56 - Hangman Game
Concepts: Strings, Lists, Loops, Random
"""

import random

WORDS = ["python", "java", "coding", "program", "computer", "keyboard",
         "variable", "function", "loop", "string"]
MAX_WRONG = 6

# Set True for testing (secret word fixed to 'python').
# Set False to pick a random word from the list.
TESTING = True


def choose_word():
    """Return the secret word."""
    if TESTING:
        return "python"
    return random.choice(WORDS)


def show_progress(word, guessed):
    """Return the word with unguessed letters as underscores."""
    return " ".join(ch if ch in guessed else "_" for ch in word)


def play():
    word = choose_word()
    guessed = []          # list of all letters already guessed
    wrong = 0

    print("=== HANGMAN ===")
    print(f"Guess the word. You get {MAX_WRONG} wrong guesses.")
    print("Progress:", show_progress(word, guessed))

    while wrong < MAX_WRONG:
        guess = input("Enter a letter: ").strip().lower()

        # Validate: single alphabetic letter only
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Enter a single letter.")
            continue

        # Repeated letter: no attempt lost
        if guess in guessed:
            print(f"You already guessed '{guess}'. Try another letter.")
            continue

        guessed.append(guess)

        if guess in word:
            print(f"{guess}: Correct")
        else:
            wrong += 1
            print(f"{guess}: Wrong ({wrong}/{MAX_WRONG})")

        print("Progress:", show_progress(word, guessed))

        # Win check
        if all(ch in guessed for ch in word):
            print(f"You won! The word was {word}.")
            print(f"Wrong guesses: {wrong}/{MAX_WRONG}")
            return

    print(f"Game Over! The word was {word}.")


if __name__ == "__main__":
    play()