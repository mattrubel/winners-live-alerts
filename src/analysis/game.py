from src.analysis.head_to_heads import HeadToHeads
from src.analysis.spreads import Spreads
from src.analysis.totals import Totals


class Game:
    def __init__(self, game_id: str, home_team: str, away_team: str, commence_time: str):
        self.game_id = game_id
        self.home_team = home_team
        self.away_team = away_team
        self.commence_time = commence_time

        self.totals = Totals()
        self.spreads = Spreads()
        self.head_to_heads = HeadToHeads()
