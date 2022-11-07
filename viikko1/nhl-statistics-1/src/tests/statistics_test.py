import unittest
from statistics import Statistics
from player import Player
from player import SortBy

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_returns_none_if_player_not_found(self):
        self.assertEqual(None, self.statistics.search("Koivu"))

    def test_search_returns_player_if_player_found(self):
        player = self.statistics.search("Kurri")
        self.assertEqual("Kurri", player.name)

    def test_team_returns_empty_list_if_no_players_found(self):
        self.assertEqual([], self.statistics.team("WPG"))

    def test_team_returns_players_of_given_team(self):
        players = self.statistics.team("EDM")
        self.assertEqual(3, len(players))

        for player in players:
            self.assertEqual("EDM", player.team)

    def test_top_returns_players_in_order_of_points(self):
        players = self.statistics.top(3)
        self.assertEqual("Gretzky", players[0].name)
        self.assertEqual("Lemieux", players[1].name)
        self.assertEqual("Yzerman", players[2].name)

    def test_top_returns_players_in_order_of_goals(self):
        players = self.statistics.top(3, SortBy.GOALS)
        self.assertEqual("Lemieux", players[0].name)
        self.assertEqual("Yzerman", players[1].name)
        self.assertEqual("Kurri", players[2].name)

    def test_top_returns_players_in_order_of_assists(self):
        players = self.statistics.top(3, SortBy.ASSISTS)
        self.assertEqual("Gretzky", players[0].name)
        self.assertEqual("Yzerman", players[1].name)
        self.assertEqual("Lemieux", players[2].name)