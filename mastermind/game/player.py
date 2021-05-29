from game.code import Code
from game.guess import Guess

class Player:
    def __init__(self, name):
        self._name = name
        self._code = Code()
        self._guess = None
        self.has_played = False
    
    def get_name(self):
        return self._name
    
    def get_guess(self):
        return self._guess
    
    def set_guess(self, guess):
        if not self.has_played:
            self._guess = Guess(guess)
        else:
            self._guess.set_guess(guess)
        self.has_played = True
    
    def make_guess(self):
        return self._code.check_guess(self._guess)
    
    def has_won(self):
        return self._code.is_correct_guess(self._guess)