"""Number guesser game.

Provides functions to generate a random secret number and compare guesses.
"""

import random


def generate_secret() -> int:
    """Generate a random secret number between 1 and 100 (inclusive).

    Returns:
        int: A random integer in the range [1, 100].
    """
    return random.randint(1, 100)


def check_guess(secret: int, guess: int) -> str:
    """Compare a guess against the secret number.

    Args:
        secret: The secret number to compare against.
        guess: The player's guess.

    Returns:
        str: 'too high' if guess > secret,
             'too low' if guess < secret,
             'correct' if guess == secret.
    """
    if guess > secret:
        return "too high"
    if guess < secret:
        return "too low"
    return "correct"


def main() -> None:
    """Run a short interactive demo of the number guesser game."""
    secret = generate_secret()
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    attempts = 0
    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        attempts += 1
        result = check_guess(secret, guess)
        print(result)

        if result == "correct":
            print(f"You got it in {attempts} attempt(s)!")
            break


if __name__ == "__main__":
    main()
