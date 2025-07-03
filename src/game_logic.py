# game_logic.py
import random

class GuessingGame:
    """
    Manages the core logic of the random number guessing game.
    """
    def __init__(self, lower_bound=1, upper_bound=100):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.secret_number = 0
        self.attempts = 0
        self.reset_game()

    def reset_game(self):
        """
        Resets the game by generating a new secret number and resetting attempts.
        """
        self.secret_number = random.randint(self.lower_bound, self.upper_bound)
        self.attempts = 0
        print(f"New game started! Guess a number between {self.lower_bound} and {self.upper_bound}.")
        print(f"(For debugging: Secret number is {self.secret_number})") # Remove in production

    def check_guess(self, guess):
        """
        Checks the user's guess against the secret number.

        Args:
            guess (int): The user's guessed number.

        Returns:
            str: A message indicating if the guess was 'too high', 'too low', 'correct',
                 or 'invalid_input'.
        """
        try:
            guess_int = int(guess)
        except ValueError:
            return "invalid_input"

        self.attempts += 1

        if guess_int < self.secret_number:
            return "too low"
        elif guess_int > self.secret_number:
            return "too high"
        else:
            return "correct"

    def get_attempts(self):
        """
        Returns the number of attempts made so far.
        """
        return self.attempts
