class Roster:
    def __init__(self):
        self.current_player = 0
        self.players = []

    def add_player(self, player):
        if player not in self.players:
            self.players.append(player)

    def get_current(self):
        return self.players[self.current_player]

    def next_player(self):
        self.current_player = (self.current_player + 1) % len(self.players)