class Player:
    def __init__(
      self, 
      name,
      nationality, 
      team,
      goals,
      assists,
      penalties,
      games
      ):
        self.name = name
        self.nationality = nationality
        self.team = team
        self.goals = goals
        self.assists = assists
        self.penalties = penalties
        self.games = games
        self.points = goals + assists
    
    def __str__(self):
        return f"{self.name:20} team {self.team} goals {self.goals} assists {self.assists}"
