
from game.console import Console
from game.roster import Roster
from game.guess import Guess
from game.player import Player

class Director:
    def __init__(self):
        self.console = Console()
        self.roster = Roster()
        self.keep_playing = True
        self.guess = None
    
    def start_game(self):
        self._prepare_game()
        while self.keep_playing:
=======
from game.board import Board
from game.console import Console
from game.move import Move
from game.player import Player
from game.roster import Roster

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        board (Hunter): An instance of the class of objects known as Board.
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        move (Rabbit): An instance of the class of objects known as Move.
        roster (Roster): An instance of the class of objects known as Roster.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        
        self._console = Console()
        self._keep_playing = True
        self._roster = Roster()
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self._prepare_game()
        while self._keep_playing:

            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _prepare_game(self):

        self.roster.add_player(Player(self.console.read("Enter player 1's name: ")))
        self.roster.add_player(Player(self.console.read("Enter player 2's name: ")))
        i = 3
        while self.console.read("Would you like to add another player? y/n ") == 'y':
            self.roster.add_player(Player(self.console.read("Enter player " + str(i) + "'s name: ")))
            i += 1
    
    def _get_inputs(self):
        self.console.write(self.roster.get_current().get_name() + "'s turn:")
        self.roster.get_current().set_guess(Guess(self.console.read_number("What is your guess? ")))
    
    def _do_updates(self):
        return None
    
    def _do_outputs(self):
        self.console.write("---------------")
        for i in self.roster.players:
            string = "Player "
            string += i.get_name()
            string += ": "

            if i.has_played:
                attempt = i.get_guess().get_guess().get_guess()
                string += str(attempt)
                string += " "
                string += i.make_guess()
            else:
                string += "---- ****"
            
            self.console.write(string)
        self.console.write("---------------")
        if self.roster.get_current().has_won():
            self.keep_playing = False
            self.console.write("Congratulations " + self.roster.get_current().get_name() + ", you have won!")
        self.roster.next_player()
=======
        """Prepares the game before it begins. In this case, that means getting the player names and adding them to the roster.
        
        Args:
            self (Director): An instance of Director.
        """
        for n in range(2):
            name = self._console.read(f"Enter a name for player {n + 1}: ")
            player = Player(name)
            self._roster.add_player(player) 
        add_player = "y"   
        while add_player is "y":
            self._console.read("Would you like to add another player? (y/n): ")
            if add_player == "y":
                name = self._console.read(f"Enter a name for the next player: ")
                player = Player(name)
                self._roster.add_player(player)
            else:
                break


            
    def _get_inputs(self, guess):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the move from the current player.

        Args:
            self (Director): An instance of Director.
        """
  
        # get next player's move
        player = self._roster.get_current()
        self._console.write(f"{player.get_name()}'s turn:")
        guess = self._console.read_number("Guess a number bewtween 1000 - 9999:  ")

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the board with the current move.

        Args:
            self (Director): An instance of Director.
        """
        player = self._roster.get_current()
        self._keep_playing = not player.has_won()
 
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring the winner.

        Args:
            self (Director): An instance of Director.
        """
        if self._player.has_won():
            winner = self._roster.get_current()
            name = winner.get_name()
            print(f"\n{name} won!")
            self._keep_playing = False
        self._roster.next_player()

     
       

