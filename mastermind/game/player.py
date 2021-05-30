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
=======

    """A person taking part in a game. The responsibility of Player is to keep track of their identity and last move.
   
    Stereotype:
        Information Holder

    Attributes:
        _name (string): The player's name.
        _move (Move): The player's last move.
    """
    def __init__(self, name): #poop
        """The class constructor.
       
        Args:
            self (Player): an instance of Player.
        """
        self._name = name
        self._code = Code()
        self._guess = None
   
    def get_name(self):
        """Returns the player's name.

        Args:
            self (Player): an instance of Player.
        """
        return self._name    
   
    def get_guess(self):
        """Returns the player's last guess (an instance of Move). If the player
        hasn't guessed yet this method returns None.

        Args:
            self (Player): an instance of Player.
        """
        return self._guess

    def check_guess(self, guess):
        """Returns guess (an instance of Move). If the player
        hasn't guessed yet this method returns None.

        Args:
            self (Player): an instance of Player.
        """
        return self._code.check_guess(self._guess)

   

    def set_guess(self, guess):
        """Sets the player's last move to the given instance of Move.

        Args:
            self (Player): an instance of Player.
            move (Move): an instance of Move
        """
        self._guess = guess


    def has_won(self):

        return self.code.is_correct_guess(self._guess)
