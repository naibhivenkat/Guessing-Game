# app.py
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER, BOLD

# Import the game logic
from game_logic import GuessingGame

class GuessingGameApp(toga.App):
    """
    Toga-based GUI application for the Guessing Game.
    """
    def startup(self):
        """
        Construct and show the Toga main window.
        """
        self.game = GuessingGame(1, 100) # Initialize the game logic
        self.game_started = False

        # Main box to hold all content
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10, alignment=CENTER))

        # Title Label
        self.title_label = toga.Label(
            "Number Guessing Game",
            style=Pack(font_size=24, font_weight=BOLD, padding_bottom=20, text_align=CENTER)
        )

        # Instructions Label
        self.instructions_label = toga.Label(
            f"Guess a number between {self.game.lower_bound} and {self.game.upper_bound}.",
            style=Pack(font_size=16, padding_bottom=15, text_align=CENTER)
        )

        # Input field for guess
        self.guess_input = toga.TextInput(
            placeholder="Enter your guess",
            style=Pack(width=200, padding_bottom=15, text_align=CENTER)
        )

        # Guess Button
        self.guess_button = toga.Button(
            "Guess",
            on_press=self.check_guess,
            style=Pack(padding=10, background_color="#4CAF50", color="white", border_radius=5)
        )

        # Feedback Label
        self.feedback_label = toga.Label(
            "",
            style=Pack(font_size=18, padding_top=15, padding_bottom=15, text_align=CENTER)
        )

        # Attempts Label
        self.attempts_label = toga.Label(
            "Attempts: 0",
            style=Pack(font_size=14, padding_bottom=20, text_align=CENTER)
        )

        # New Game Button
        self.new_game_button = toga.Button(
            "New Game",
            on_press=self.start_new_game,
            style=Pack(padding=10, background_color="#2196F3", color="white", border_radius=5)
        )

        # Add components to the main box
        main_box.add(self.title_label)
        main_box.add(self.instructions_label)
        main_box.add(self.guess_input)
        main_box.add(self.guess_button)
        main_box.add(self.feedback_label)
        main_box.add(self.attempts_label)
        main_box.add(self.new_game_button)

        # Create the main window
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

        # Start a new game immediately on startup
        self.start_new_game(None)

    def check_guess(self, widget):
        """
        Event handler for the Guess button. Checks the user's guess.
        """
        if not self.game_started:
            self.feedback_label.text = "Please start a new game first!"
            return

        guess_text = self.guess_input.value.strip()
        if not guess_text:
            self.feedback_label.text = "Please enter a number!"
            return

        result = self.game.check_guess(guess_text)
        attempts = self.game.get_attempts()
        self.attempts_label.text = f"Attempts: {attempts}"

        if result == "correct":
            self.feedback_label.text = f"Congratulations! You guessed it in {attempts} attempts!"
            self.feedback_label.style.color = "green"
            self.game_started = False # Disable game until new game is started
            self.guess_input.enabled = False
            self.guess_button.enabled = False
        elif result == "too high":
            self.feedback_label.text = "Too high! Try again."
            self.feedback_label.style.color = "red"
        elif result == "too low":
            self.feedback_label.text = "Too low! Try again."
            self.feedback_label.style.color = "red"
        elif result == "invalid_input":
            self.feedback_label.text = "Invalid input. Please enter a number."
            self.feedback_label.style.color = "orange"

        self.guess_input.value = "" # Clear the input field

    def start_new_game(self, widget):
        """
        Event handler for the New Game button. Resets the game.
        """
        self.game.reset_game()
        self.feedback_label.text = "Game started! Make your first guess."
        self.feedback_label.style.color = "black"
        self.attempts_label.text = "Attempts: 0"
        self.guess_input.value = ""
        self.guess_input.enabled = True
        self.guess_button.enabled = True
        self.game_started = True

def main():
    return GuessingGameApp('Guessing Game', 'com.example.guessinggame')

if __name__ == '__main__':
    main().main_loop()
