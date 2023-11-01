import random

class HangmanGame:
    def __init__(self):
        self.word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
        self.word_to_guess = random.choice(self.word_list)
        self.guesses_left = 4
        self.correct_guesses = set()
        self.incorrect_guesses = set()

    def display_word(self):
        displayed_word = ""
        for letter in self.word_to_guess:
            if letter in self.correct_guesses:
                displayed_word += letter
            else:
                displayed_word += "_"
        return displayed_word

    def display_game_state(self):
        print(f"Word: {self.display_word()}")
        print(f"Guesses left: {self.guesses_left}")
        print(f"Incorrect guesses: {' '.join(sorted(self.incorrect_guesses))}")

    def make_guess(self, guess):
        if guess in self.correct_guesses or guess in self.incorrect_guesses:
            print("You already guessed that letter.")
            return

        if guess in self.word_to_guess:
            self.correct_guesses.add(guess)
        else:
            self.incorrect_guesses.add(guess)
            self.guesses_left -= 1

    def is_game_over(self):
        if self.guesses_left == 0:
            print("You ran out of guesses! The word was:", self.word_to_guess)
            return True
        elif set(self.word_to_guess) == self.correct_guesses:
            print("Congratulations! You guessed the word:", self.word_to_guess)
            return True
        return False

    def play(self):
        print("Welcome to Hangman!")
        while not self.is_game_over():
            self.display_game_state()
            guess = input("Guess a letter: ").lower()
            if len(guess) == 1 and guess.isalpha():
                self.make_guess(guess)
            else:
                print("Invalid guess. Please enter a single letter.")
        print("Game over. Thanks for playing!")

# Main function to start the game
if __name__ == "__main__":
    game = HangmanGame()
    game.play()
