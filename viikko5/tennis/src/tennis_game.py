class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0
        self.scores = ["Love", "Fifteen", "Thirty", "Forty"]

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_points += 1
        else:
            self.player2_points += 1

    def get_score_when_not_equal_points(self):
        return f"{self.scores[self.player1_points]}-{self.scores[self.player2_points]}"

    def get_score_when_advantage_or_win(self):
        difference = self.player1_points - self.player2_points
        if difference == 1:
            return f"Advantage {self.player1_name}"
        elif difference == -1:
            return f"Advantage {self.player2_name}"
        elif difference >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"

    def get_score_when_equal_points(self):
        if self.player1_points < 3:
            return self.scores[self.player1_points] + "-All"
        else:
            return "Deuce"

    def get_score(self):
        if self.player1_points == self.player2_points:
            return self.get_score_when_equal_points()
        if self.player1_points >= 4 or self.player2_points >= 4:
            return self.get_score_when_advantage_or_win()
        else:
            return self.get_score_when_not_equal_points()
