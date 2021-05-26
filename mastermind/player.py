from game.code import Code
from game.guess import Guess

class Player:
    """A person taking part in a game. The responsibility of Player is to keep track of their identity and last move.
   
    Stereotype:
        Information Holder

    Attributes:
        _name (string): The player's name.
        _move (Move): The player's last move.
    """
    def __init__(self, name):
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

    def check_guess(self):
        """Returns guess (an instance of Move). If the player
        hasn't guessed yet this method returns None.

        Args:
            self (Player): an instance of Player.
        """
        return code.check.guess

   

    def set_guess(self, guess):
        """Sets the player's last move to the given instance of Move.

        Args:
            self (Player): an instance of Player.
            move (Move): an instance of Move
        """
        self._guess = guess


    def has_won(self):

        return self.code.is_correct_guess(self._guess)   