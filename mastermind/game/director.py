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