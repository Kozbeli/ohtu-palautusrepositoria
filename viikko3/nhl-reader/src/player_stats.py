from player import Player


class PlayerStats:
    def __init__(self, reader):
        self.players = reader.players

    def top_scorers_by_nationality(self, nationality):
        finnish_players = list(filter(lambda player: player.nationality == nationality, self.players))
        sorted_by_score = list(sorted(finnish_players, key=lambda player: player.points, reverse=True))
        return sorted_by_score