class Guess:
    def __init__(self, guess):
        self._guess = guess
    def get_guess(self):
        return self._guess
    def set_guess(self, guess):
        self._guess = guess